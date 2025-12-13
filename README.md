# Physical AI & Humanoid Robotics Textbook

This repository hosts the official textbook for "Physical AI & Humanoid Robotics", built using [Docusaurus](https://docusaurus.io/). This textbook provides a comprehensive guide to intelligent embodied systems, covering theoretical foundations, practical implementations, and cutting-edge research in robotics and artificial intelligence.

## AI Chatbot Integration

This textbook features an integrated AI chatbot that allows students and researchers to ask questions about the robotics content. The chatbot uses Retrieval-Augmented Generation (RAG) to provide accurate answers based on the textbook content, ensuring all responses are grounded in the actual book material.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Local Development](#local-development)
- [Building the Site](#building-the-site)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

This textbook is designed for advanced undergraduate, graduate students, and researchers in robotics and AI. It covers 4 modules and 13 weeks of content, including topics such as robot kinematics, dynamics, sensing, perception, motion planning, control, human-robot interaction, learning in robotics, humanoid design, and ethical considerations.

## Installation

To set up the development environment, ensure you have Node.js (v18 or higher recommended) and npm installed.

```bash
npm install
```
This command installs all necessary project dependencies.

## Local Development

To start the local development server and view the website in your browser:

```bash
npm start
```
This command starts a local development server and opens a browser window. Most changes are reflected live without having to restart the server.

## Building the Site

To generate static content for production deployment:

```bash
npm run build
```
This command bundles your website into static files in the `build` directory. This output can then be served using any static content hosting service (e.g., GitHub Pages).

## Deployment

If you are using GitHub Pages for hosting, you can use the following command to build the website and push it to the `gh-pages` branch (ensure your Docusaurus configuration is set up for GitHub Pages deployment):

```bash
GIT_USER=<Your GitHub username> npm run deploy
```
For SSH deployment, use:
```bash
USE_SSH=true npm run deploy
```

## Project Structure

The key directories and files in this project are:
- `docs/`: Markdown files for chapters, modules, weeks, labs, assessments. Organized by `moduleX/weekY/chapter-name.md`.
- `src/`: Custom React components, Docusaurus plugins/theme overrides.
- `static/`: Static assets (images, logos, favicons, raw data for charts).
- `specs/`: Feature specifications, plans, tasks.
- `contracts/`: API contracts (e.g., for external assessment systems, if any).
- `quickstart/`: Quickstart guide for developers/contributors.
- `workflows/`: GitHub Actions workflows for build, deploy, validation (e.g., Lighthouse CI, Broken Link Check).
- `docusaurus.config.ts`: Main Docusaurus configuration file.
- `sidebars.ts`: Docusaurus sidebar configuration (modules, weeks, chapters).
- `package.json`: Project dependencies and scripts.

## Backend and Chatbot Setup

To run the full application with the AI chatbot functionality:

### Prerequisites
- Python 3.9+
- Node.js 18+
- API keys for Gemini, Cohere, and Qdrant

### Running the Application

1. **Backend Setup**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python -m src.main
   ```

2. **Frontend Setup**:
   ```bash
   # In the main project directory
   npm install
   npm start
   ```

The chatbot will be available as a floating widget on all pages of the textbook website.

### Important: Running Both Services

For the chatbot to work properly, you need to run both services:

1. **Backend**: Start the Python backend server first
   ```bash
   cd backend
   python -m src.main
   ```
   This starts the backend on `http://localhost:8000`

2. **Frontend**: In a separate terminal/command prompt, start the frontend:
   ```bash
   npm start
   ```
   This starts the frontend on `http://localhost:3000` with automatic proxy to the backend

The frontend will automatically proxy API requests from `http://localhost:3000/api/v1/` to `http://localhost:8000/api/v1/`.

For detailed setup instructions, see [CHATBOT_SETUP.md](CHATBOT_SETUP.md).

## Deployment

For production deployment:

### Option 1: Separate Backend and Frontend (Recommended)
1. Deploy the backend to a Python-compatible platform (Render, Railway, etc.)
2. Deploy the frontend to Vercel/Netlify with `REACT_APP_API_URL` environment variable pointing to your backend

### Option 2: Combined Deployment (Advanced)
1. Use the provided `vercel.json` configuration to deploy both together
2. Ensure all dependencies in `requirements.txt` are compatible with the deployment platform

## Contributing

We welcome contributions to this textbook! If you find errors, have suggestions for improvements, or want to add new content, please consider contributing.

### How to Contribute

1.  **Fork** this repository.
2.  **Clone** your forked repository to your local machine.
3.  Create a new **branch** for your changes.
4.  Make your **modifications** or add new content.
5.  **Commit** your changes with clear, descriptive messages.
6.  **Push** your branch to your forked repository.
7.  Open a **Pull Request (PR)** to the `main` branch of this repository.

Please ensure your contributions adhere to the existing style and content guidelines. For more detailed contribution guidelines, please see [CONTRIBUTING.md](CONTRIBUTING.md).