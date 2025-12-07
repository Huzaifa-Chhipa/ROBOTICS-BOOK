# Contributing to Physical AI & Humanoid Robotics Textbook

We appreciate your interest in contributing to the "Physical AI & Humanoid Robotics" textbook! Your contributions help us improve the quality and expand the content of this valuable resource.

Please take a moment to review this document to understand our contribution guidelines.

## How to Contribute

The general workflow for contributions is as follows:

1.  **Fork the Repository:** Start by forking the main repository to your GitHub account.
2.  **Clone Your Fork:** Clone your forked repository to your local development machine.
    ```bash
    git clone https://github.com/YOUR_USERNAME/ROBOTICS-BOOK.git
    cd ROBOTICS-BOOK
    ```
    (Replace `YOUR_USERNAME` with your actual GitHub username.)
3.  **Create a New Branch:** Before making any changes, create a new branch from `main` for your specific contribution. Use a descriptive name for your branch (e.g., `feature/add-new-chapter`, `fix/typo-in-kinematics`).
    ```bash
    git checkout main
    git pull origin main # Ensure your main branch is up-to-date
    git checkout -b feature/your-feature-name
    ```
4.  **Make Your Changes:** Implement your bug fix, add new content, improve existing sections, etc.
    *   **Content:** Write your content in Markdown (`.md`) files following the existing structure (`docs/moduleX/weekY/chapter-name.md`).
    *   **Code:** If you are contributing code (e.g., Docusaurus components, scripts), ensure it follows the project's coding style and conventions.
5.  **Test Your Changes (if applicable):** If you've made changes to the Docusaurus site structure or added new components, run the local development server to ensure everything works as expected.
    ```bash
    npm install
    npm start
    ```
6.  **Commit Your Changes:** Commit your changes with a clear and concise commit message. A good commit message explains *what* was changed and *why*.
    ```bash
    git add .
    git commit -m "feat: Add new section on advanced control strategies"
    ```
    (Use conventional commits if possible, e.g., `feat:`, `fix:`, `docs:`, `chore:`)
7.  **Push to Your Fork:** Push your new branch to your forked repository on GitHub.
    ```bash
    git push origin feature/your-feature-name
    ```
8.  **Open a Pull Request (PR):** Go to your forked repository on GitHub and open a Pull Request to the `main` branch of the *original* repository.
    *   Provide a clear title and description for your PR, explaining the purpose and scope of your changes.
    *   Reference any related issues if applicable.

## Style and Content Guidelines

*   **Markdown:** Use standard Markdown syntax for all content files.
*   **Code Blocks:** Use fenced code blocks with language identifiers for code snippets.
*   **Language:** Maintain a clear, concise, and academic tone.
*   **Referencing:** Ensure proper citation or referencing for any external content or research.
*   **Docusaurus Specifics:** If you're modifying Docusaurus configuration or React components, adhere to Docusaurus best practices.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md) (if exists). By participating in this project, you agree to abide by its terms.

Thank you for your contributions!