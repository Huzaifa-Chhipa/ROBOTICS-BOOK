"""
Content ingestion service for the Book RAG Chatbot.
Batch-optimized for Cohere free-tier and Qdrant.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from ..utils.embedding_utils import get_embeddings_batch
from qdrant_client import models
from .qdrant_service import qdrant, QDRANT_COLLECTION_NAME
import logging

logger = logging.getLogger(__name__)


def fetch_sitemap_urls(sitemap_url: str) -> List[str]:
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "xml")
        urls = [loc.text.strip() for loc in soup.find_all("loc")]

        # Fix incorrect domain in sitemap (placeholder URLs need to be corrected)
        corrected_urls = []
        for url in urls:
            # Replace placeholder domain with correct one
            corrected_url = url.replace("https://your-docusaurus-site.example.com", "https://robotics-book-gamma.vercel.app")
            corrected_urls.append(corrected_url)

        logger.info(f"Found {len(corrected_urls)} URLs in sitemap (corrected domain)")
        return corrected_urls
    except Exception as e:
        logger.error(f"Error fetching sitemap: {e}")
        raise


def fetch_page_content(url: str) -> Dict[str, Any]:
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        for script in soup(["script", "style"]):
            script.decompose()

        title = soup.title.string if soup.title else ""
        text_content = soup.get_text(separator=" ", strip=True)

        lines = (line.strip() for line in text_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = " ".join(c for c in chunks if c)

        return {
            "url": url,
            "title": title,
            "content": text_content,
        }

    except Exception as e:
        logger.error(f"Fetch error on {url} → {e}")
        return {"url": url, "title": "", "content": "", "error": str(e)}


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
        if start >= len(text):
            break

    return chunks


def store_in_qdrant(chunks: List[Dict[str, Any]]):
    text_list = [c["content"] for c in chunks]

    # ▶ BATCH embeddings — free-tier safe
    logger.info("Generating embeddings in batches...")
    embeddings = get_embeddings_batch(text_list, batch_size=50)

    points = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        point = models.PointStruct(
            id=i,
            vector=embedding,
            payload={
                "url": chunk["url"],
                "title": chunk["title"],
                "text": chunk["content"],
                "doc_id": chunk.get("doc_id", f"doc_{i}"),
                "chunk_id": chunk.get("chunk_id", f"chunk_{i}"),
                "source": "robotics_book",
            },
        )
        points.append(point)

    qdrant.upload_points(
        collection_name=QDRANT_COLLECTION_NAME,
        points=points
    )

    logger.info(f"Uploaded {len(points)} chunks → Qdrant")


def ingest_book_content(sitemap_url: str, batch_size: int = 5):
    logger.info(f"Starting ingestion → {sitemap_url}")

    urls = fetch_sitemap_urls(sitemap_url)
    all_chunks = []

    # Process URLs in batches to avoid timeout issues
    for batch_start in range(0, len(urls), batch_size):
        batch_urls = urls[batch_start:batch_start + batch_size]
        logger.info(f"Processing batch {batch_start//batch_size + 1}/{(len(urls)-1)//batch_size + 1} ({len(batch_urls)} URLs)")

        batch_chunks = []
        for i, url in enumerate(batch_urls):
            logger.info(f"Processing {batch_start + i + 1}/{len(urls)} → {url}")

            page = fetch_page_content(url)
            if page.get("error"):
                logger.warning(f"Skipping URL due to error: {url}")
                continue

            content_chunks = chunk_text(page["content"])

            for j, chunk in enumerate(content_chunks):
                batch_chunks.append({
                    "url": page["url"],
                    "title": page["title"],
                    "content": chunk,
                    "doc_id": f"doc_{batch_start + i}",
                    "chunk_id": f"chunk_{batch_start + i}_{j}",
                })

        if batch_chunks:
            all_chunks.extend(batch_chunks)
            logger.info(f"Completed batch, total chunks so far: {len(all_chunks)}")
        else:
            logger.warning(f"No chunks found in batch {batch_start//batch_size + 1}")

    if not all_chunks:
        logger.warning("No chunks found, aborting...")
        return

    logger.info(f"Processing complete. Total chunks: {len(all_chunks)}")
    store_in_qdrant(all_chunks)
    logger.info("Ingestion complete.")


if __name__ == "__main__":
    import sys
    DEFAULT_SITEMAP = "https://robotics-book-gamma.vercel.app/sitemap.xml"

    sitemap = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SITEMAP
    ingest_book_content(sitemap)
