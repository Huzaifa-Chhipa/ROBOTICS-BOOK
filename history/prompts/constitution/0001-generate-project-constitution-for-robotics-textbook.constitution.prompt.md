---
id: 0001
title: Generate Project Constitution for Robotics Textbook
stage: constitution
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: none
branch: master
user: user
command: /sp.constitution Generate a constitution for the "Physical AI & Humanoid Robotics" textbook project that establishes guiding principles, rules, and standards for all specification, planning, and task outputs. Include:

    1.  **Content Accuracy & Technical Rigor**
        - Must ensure all chapters, examples, and hardware specs are technically correct.
        - Citations, versioning, and validation requirements for code snippets and simulations.
    2.  **Educational Clarity & Accessibility**
        - Chapter templates must follow a consistent structure: Learning Objectives → Prerequisites → Content → Summary → Exercises → References.
        - Metadata must track prerequisites, estimated time, learning objectives, and difficulty.
    3.  **Consistency & Standards**
        - Frontmatter schema enforcement for all Markdown chapters.
        - Glossary and notation guides as single sources of truth.
        - Naming conventions for chapters, modules, files, and images.
    4.  **Docusaurus Structure & Quality**
        - Sidebar must reflect modules, weeks, and chapters with collapsible categories.
        - Images must be optimized with alt text.
        - Frontmatter must include required metadata fields.
    5.  **Code Example Quality**
        - Embedded code snippets must specify language, dependencies, and safety guidelines.
        - Deviations (e.g., no `/examples/` directories) must be justified.
    6.  **Deployment & Publishing Standards**
        - GitHub Pages deployment with build validation, broken link checks, Lighthouse CI (performance, SEO, accessibility).
        - Incremental publishing supported per week or module.
    7.  **Risk Management & Updates**
        - Must document risks like hardware cost, latency, and syllabus changes.
        - Plan for future updates as robotics software evolves.
labels: ["constitution", "initial-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - N/A
---

## Prompt

/sp.constitution Generate a constitution for the "Physical AI & Humanoid Robotics" textbook project that establishes guiding principles, rules, and standards for all specification, planning, and task outputs. Include:

1.  **Content Accuracy & Technical Rigor**
    - Must ensure all chapters, examples, and hardware specs are technically correct.
    - Citations, versioning, and validation requirements for code snippets and simulations.

2.  **Educational Clarity & Accessibility**
    - Chapter templates must follow a consistent structure: Learning Objectives → Prerequisites → Content → Summary → Exercises → References.
    - Metadata must track prerequisites, estimated time, learning objectives, and difficulty.

3.  **Consistency & Standards**
    - Frontmatter schema enforcement for all Markdown chapters.
    - Glossary and notation guides as single sources of truth.
    - Naming conventions for chapters, modules, files, and images.

4.  **Docusaurus Structure & Quality**
    - Sidebar must reflect modules, weeks, and chapters with collapsible categories.
    - Images must be optimized with alt text.
    - Frontmatter must include required metadata fields.

5.  **Code Example Quality**
    - Embedded code snippets must specify language, dependencies, and safety guidelines.
    - Deviations (e.g., no `/examples/` directories) must be justified.

6.  **Deployment & Publishing Standards**
    - GitHub Pages deployment with build validation, broken link checks, Lighthouse CI (performance, SEO, accessibility).
    - Incremental publishing supported per week or module.

7.  **Risk Management & Updates**
    - Must document risks like hardware cost, latency, and syllabus changes.
    - Plan for future updates as robotics software evolves.

## Response snapshot

Updated `.specify/memory/constitution.md` with initial project constitution (v1.0.0).

## Outcome

- ✅ Impact: Initial project constitution established.
- 🧪 Tests: N/A (no tests for constitution)
- 📁 Files: Created/updated `.specify/memory/constitution.md`.
- 🔁 Next prompts: User's next command.
- 🧠 Reflection: Successfully generated the initial project constitution based on user-provided principles and template.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A.
- Prompt variant (if applicable): N/A.
- Next experiment (smallest change to try): N/A.
