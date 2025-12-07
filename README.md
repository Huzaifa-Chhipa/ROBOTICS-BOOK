# Physical AI & Humanoid Robotics Textbook

This repository hosts the official textbook for "Physical AI & Humanoid Robotics", built using [Docusaurus](https://docusaurus.io/). This textbook provides a comprehensive guide to intelligent embodied systems, covering theoretical foundations, practical implementations, and cutting-edge research in robotics and artificial intelligence.

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