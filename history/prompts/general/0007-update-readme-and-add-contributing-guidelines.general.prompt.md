---
phr_id: 0007
phr_title: Update README and Add Contributing Guidelines
phr_stage: general
phr_date_iso: 2025-12-07
phr_surface: agent
phr_model: gemini-1.5-pro
phr_feature: none
phr_branch: main
phr_user: Huzaifa-Chhipa
phr_command: Physical AI & Humanoid Robotics Textbook ... Contributing ye de rha page pr tw
phr_labels: ["documentation", "contributing", "readme"]
phr_links:
  spec: null
  ticket: null
  adr: null
  pr: null
phr_files_yaml: |
  - README.md
  - CONTRIBUTING.md
phr_tests_yaml: |
  - null
phr_prompt_text: |
  Physical AI & Humanoid Robotics Textbook
  This repository hosts the official textbook for “Physical AI & Humanoid Robotics”, built using Docusaurus. This textbook provides a comprehensive guide to intelligent embodied systems, covering theoretical foundations, practical implementations, and cutting-edge research in robotics and artificial intelligence.

  Table of Contents
  Introduction
  Installation
  Local Development
  Building the Site
  Deployment
  Project Structure
  Contributing
  Introduction
  This textbook is designed for advanced undergraduate, graduate students, and researchers in robotics and AI. It covers 4 modules and 13 weeks of content, including topics such as robot kinematics, dynamics, sensing, perception, motion planning, control, human-robot interaction, learning in robotics, humanoid design, and ethical considerations.

  Installation
  To set up the development environment, ensure you have Node.js (v18 or higher recommended) and npm installed.

  npm install
  This command installs all necessary project dependencies.

  Local Development
  To start the local development server and view the website in your browser:

  npm start
  This command starts a local development server and opens a browser window. Most changes are reflected live without having to restart the server.

  Building the Site
  To generate static content for production deployment:

  npm run build
  This command bundles your website into static files in the build directory. This output can then be served using any static content hosting service (e.g., GitHub Pages).

  Deployment
  If you are using GitHub Pages for hosting, you can use the following command to build the website and push it to the gh-pages branch (ensure your Docusaurus configuration is set up for GitHub Pages deployment):

  GIT_USER=<Your GitHub username> npm run deploy
  For SSH deployment, use:

  USE_SSH=true npm run deploy
  Project Structure
  The key directories and files in this project are:

  docs/: Markdown files for chapters, modules, weeks, labs, assessments. Organized by moduleX/weekY/chapter-name.md.
  src/: Custom React components, Docusaurus plugins/theme overrides.
  static/: Static assets (images, logos, favicons, raw data for charts).
  specs/: Feature specifications, plans, tasks.
  contracts/: API contracts (e.g., for external assessment systems, if any).
  quickstart/: Quickstart guide for developers/contributors.
  workflows/: GitHub Actions workflows for build, deploy, validation (e.g., Lighthouse CI, Broken Link Check).
  docusaurus.config.ts: Main Docusaurus configuration file.
  sidebars.ts: Docusaurus sidebar configuration (modules, weeks, chapters).
  package.json: Project dependencies and scripts.
  Contributing ye de rha page pr tw
phr_response_text: |
  I have updated the `README.md` with a more detailed "Contributing" section that includes instructions for opening a pull request.
  I also created a new `CONTRIBUTING.md` file with comprehensive contribution guidelines.
  Both files have been committed and pushed to your repository.
---