# Data Model for Physical AI & Humanoid Robotics Textbook

This document defines the data model for the textbook content, outlining the key entities and their attributes.

## 1. Module

A logical grouping of related chapters, typically spanning multiple weeks.

-   **ID**: Unique identifier (e.g., `module-01-introduction`).
-   **Title**: Display name of the module (e.g., "Module 1: Introduction to Robotics").
-   **Description**: A brief overview of the module's content and learning goals.
-   **Duration**: Estimated time or number of weeks this module is expected to cover (e.g., "2 weeks").
-   **Associated Chapters**: List of chapter IDs belonging to this module.
-   **Learning Objectives**: High-level learning outcomes for the entire module.

## 2. Chapter

The core content unit of the textbook, covering specific topics.

-   **ID**: Unique identifier (e.g., `ch-01-kinematics-basics`).
-   **Frontmatter Metadata**: (Refer to `specs/001-robotics-textbook-spec/contracts/chapter-frontmatter.json` for detailed schema)
    -   **title**: Title of the chapter.
    -   **description**: Short summary.
    -   **slug**: URL-friendly identifier.
    -   **week**: Week number (1-13).
    -   **module**: Module title.
    -   **prerequisites**: Array of chapter slugs that are prerequisites.
    -   **learningObjectives**: Array of specific learning objectives.
    -   **estimatedTime**: Estimated time to complete in minutes.
    -   **difficultyLevel**: "Beginner", "Intermediate", or "Advanced".
    -   **assessmentType**: "Quiz", "Lab", "Project", "Exam" (optional, default "None").
    -   **sidebar_label**: Label for sidebar navigation.
    -   **position**: Order in sidebar.
-   **Content**: The main body of the chapter, written in Markdown/MDX, including text, images, code examples, and embedded components.

## 3. Assessment

Evaluative components used to gauge student understanding and progress.

-   **ID**: Unique identifier (e.g., `assessment-01-module1-quiz`).
-   **Title**: Name of the assessment (e.g., "Module 1 Quiz").
-   **Type**: "Quiz", "Lab", "Project", "Exam", "Homework".
-   **Description**: Details about the assessment, its purpose, and requirements.
-   **Associated Chapters/Modules**: Which content units this assessment covers.
-   **Due Date**: (If applicable)
-   **Rubric/Grading Criteria**: Guidelines for evaluation.
-   **External Link**: URL to an external assessment system (if integrated).

## 4. Glossary Entry

Definitions of key terms used throughout the textbook.

-   **Term**: The word or phrase being defined.
-   **Definition**: A clear, concise explanation of the term.
-   **Related Terms**: Other glossary terms that are related.
-   **References**: Sources for the definition (optional).

## 5. Hardware Setup Path

Detailed instructions for configuring specific hardware and software environments.

-   **ID**: Unique identifier (e.g., `hw-setup-path-ros-nvidia-jetson`).
-   **Title**: Descriptive name for the setup (e.g., "ROS Noetic on NVIDIA Jetson").
-   **Description**: Overview of the hardware and software involved.
-   **Required Components**: List of hardware components (e.g., "NVIDIA Jetson Nano", "USB Camera").
-   **Software Prerequisites**: List of software dependencies (e.g., "Ubuntu 20.04", "ROS Noetic").
-   **Step-by-Step Instructions**: Detailed, numbered steps for installation and configuration, including troubleshooting tips.
-   **Verification Steps**: How to confirm the setup is working correctly.
-   **Associated Chapters/Labs**: Which content units rely on this setup.
