# Robotics Book RAG Chatbot

This project has been restructured into separate frontend and backend components.

## Project Structure

```
├── frontend/           # Docusaurus frontend
│   ├── package.json           # Dependencies and scripts
│   ├── package-lock.json      # Locked dependency versions
│   ├── tsconfig.json          # TypeScript configuration
│   ├── docusaurus.config.ts   # Docusaurus configuration
│   ├── sidebars.ts           # Sidebar navigation configuration
│   ├── docs/                 # Documentation content
│   ├── plugins/              # Docusaurus plugins
│   │   └── docusaurus-plugin-robotics-chatbot/ # Chatbot plugin
│   ├── pages/                # Docusaurus pages
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── theme/            # Docusaurus theme customization
│   │   ├── css/              # CSS files
│   │   └── static/           # Static assets
│   └── static/               # Static assets (images, etc.)
├── backend/            # FastAPI backend
│   └── src/
│       ├── main.py     # FastAPI application entry point
│       ├── routes/     # API routes
│       ├── services/   # Business logic
│       ├── models/     # Data models
│       ├── agents/     # AI agents
│       ├── utils/      # Utility functions
│       └── config.py   # Configuration
├── tests/              # Test files
├── run_backend.py      # Helper script to run backend from root
└── ...                 # Other root files
```

## Running the Application

### Backend (FastAPI)

To run the backend server:

```bash
# Option 1: Run from the backend directory
cd backend
python -m src.main

# Option 2: Use the helper script from the root directory
python run_backend.py src.main
```

To run the backend with uvicorn:

```bash
# From the backend directory
cd backend
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Or using the helper script (you'll need to modify run_backend.py for uvicorn)
cd backend
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend (Docusaurus)

```bash
cd frontend
npm install
npm start
```

## Running Tests

Tests have been updated to work with the new structure. You may need to run them from the root directory with the Python path set appropriately:

```bash
# Make sure backend is in the Python path
export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}./backend/src"
python -m pytest tests/
```

## Running Ingestion

To run the content ingestion:

```bash
# From the backend directory
cd backend
python -m src.services.ingestion_service

# Or using the helper script
python run_backend.py src.services.ingestion_service
```