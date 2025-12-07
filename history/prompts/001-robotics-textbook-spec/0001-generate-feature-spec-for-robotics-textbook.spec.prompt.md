---
id: 0001
title: Generate Feature Spec for Robotics Textbook
stage: spec
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: 001-robotics-textbook-spec
branch: 001-robotics-textbook-spec
user: user
command: /sp.specify Generate a full feature specification for a textbook titled "Physical AI & Humanoid Robotics" based on the following inputs: 1. **Course Overview**: - 13-week capstone course bridging digital AI and physical humanoid robotics. - Focus on embodied intelligence, ROS 2, Gazebo, Unity, NVIDIA Isaac, and LLM-VLA integration. - Goal: Students apply AI knowledge to simulated and real-world humanoid robots. 2. **Modules & Weeks**: - Module 1: Robotic Nervous System (ROS 2) – Weeks 3-5 - Module 2: Digital Twin (Gazebo & Unity) – Weeks 6-7 - Module 3: AI-Robot Brain (NVIDIA Isaac) – Weeks 8-10 - Module 4: Vision-Language-Action (VLA) & Humanoids – Weeks 11-13 - Weeks 1-2: Introduction to Physical AI 3. **Weekly Topics**: Use the weekly breakdown provided (topics like ROS 2 nodes, physics simulation, Isaac ROS, cognitive planning, multi-modal interaction, etc.). 4. **Chapters**: - For each week, generate chapters with: - **Title** - 1–2 line **description** - **Prerequisites** - **Estimated time (hours)** - **Learning objectives** (2–4 measurable objectives) - Optional: `assessment_type` if relevant (project, lab, capstone) - `difficulty_level` (beginner/intermediate/advanced) 5. **Assessments**: - ROS 2 package project - Gazebo simulation implementation - Isaac perception pipeline - Capstone: Simulated humanoid with conversational AI 6. **Hardware Requirements & Labs**: - High-performance workstation (RTX GPU, Ubuntu 22.04, RAM, CPU) - Edge kit: Jetson Orin Nano, RealSense D435i, IMU, mic array - Optional physical robot: Unitree Go2, Hiwonder TonyPi Pro, or cloud-based alternative - Include lab setup options and notes about latency, cost, and minimum requirements. 7. **Learning Outcomes**: - Physical AI principles and embodied intelligence - ROS 2 mastery - Simulation with Gazebo & Unity - NVIDIA Isaac AI platform usage - Humanoid robot design and natural interaction - GPT/LLM integration for conversational robotics 8. **Functional Requirements (FRs)**: - Navigation (sidebar by module/week/topic) - Chapter frontmatter metadata (week, module, prerequisites, learning objectives, time) - Search (chapter + glossary) - Assessment integration (capstone, project rubrics) - Hardware setup guidance 9. **User Stories**: - At least 4 stories covering learner navigation, prerequisite visibility, teacher assignments, and topic search. 10. **Success Criteria (SC)**: - Measurable outcomes like 13-week coverage, search accuracy, functioning prerequisite links, hardware setup visibility. 11. **Key Entities**: - Module, Chapter, Assessment, Part, Glossary Entry, Hardware Setup Path 12. **Assumptions**: - Students have programming experience - Access to hardware/simulations - 13-week course timeline 13. **Scope Boundaries**: - In scope: chapter structure, metadata, navigation, assessments - Out of scope: full chapter content, embedded video, interactive simulations 14. **Dependencies**: - Docusaurus for deployment, hardware/software versions for simulation - Metadata schema validation 15. **Constitution Compliance Notes**: - Note deviations if any (e.g., embedded code snippets instead of `/examples` directories) and justifications 16. **Additional Notes / Risks**: - Hardware costs, latency issues, syllabus updates, cloud vs local deployment trade-offs Output must be a structured, markdown-ready specification suitable for `specs/book-master-plan/spec.md`, including tables, code blocks, and hierarchical lists where appropriate. Chapters, modules, and weeks must reflect the detailed course and hardware information provided.
labels: ["specification", "feature-development"]
links:
  spec: specs/001-robotics-textbook-spec/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-robotics-textbook-spec/spec.md
  - specs/001-robotics-textbook-spec/checklists/requirements.md
tests:
  - N/A
---

## Prompt

/sp.specify Generate a full feature specification for a textbook titled "Physical AI & Humanoid Robotics" based on the following inputs: 1. **Course Overview**: - 13-week capstone course bridging digital AI and physical humanoid robotics. - Focus on embodied intelligence, ROS 2, Gazebo, Unity, NVIDIA Isaac, and LLM-VLA integration. - Goal: Students apply AI knowledge to simulated and real-world humanoid robots. 2. **Modules & Weeks**: - Module 1: Robotic Nervous System (ROS 2) – Weeks 3-5 - Module 2: Digital Twin (Gazebo & Unity) – Weeks 6-7 - Module 3: AI-Robot Brain (NVIDIA Isaac) – Weeks 8-10 - Module 4: Vision-Language-Action (VLA) & Humanoids – Weeks 11-13 - Weeks 1-2: Introduction to Physical AI 3. **Weekly Topics**: Use the weekly breakdown provided (topics like ROS 2 nodes, physics simulation, Isaac ROS, cognitive planning, multi-modal interaction, etc.). 4. **Chapters**: - For each week, generate chapters with: - **Title** - 1–2 line **description** - **Prerequisites** - **Estimated time (hours)** - **Learning objectives** (2–4 measurable objectives) - Optional: `assessment_type` if relevant (project, lab, capstone) - `difficulty_level` (beginner/intermediate/advanced) 5. **Assessments**: - ROS 2 package project - Gazebo simulation implementation - Isaac perception pipeline - Capstone: Simulated humanoid with conversational AI 6. **Hardware Requirements & Labs**: - High-performance workstation (RTX GPU, Ubuntu 22.04, RAM, CPU) - Edge kit: Jetson Orin Nano, RealSense D435i, IMU, mic array - Optional physical robot: Unitree Go2, Hiwonder TonyPi Pro, or cloud-based alternative - Include lab setup options and notes about latency, cost, and minimum requirements. 7. **Learning Outcomes**: - Physical AI principles and embodied intelligence - ROS 2 mastery - Simulation with Gazebo & Unity - NVIDIA Isaac AI platform usage - Humanoid robot design and natural interaction - GPT/LLM integration for conversational robotics 8. **Functional Requirements (FRs)**: - Navigation (sidebar by module/week/topic) - Chapter frontmatter metadata (week, module, prerequisites, learning objectives, time) - Search (chapter + glossary) - Assessment integration (capstone, project rubrics) - Hardware setup guidance 9. **User Stories**: - At least 4 stories covering learner navigation, prerequisite visibility, teacher assignments, and topic search. 10. **Success Criteria (SC)**: - Measurable outcomes like 13-week coverage, search accuracy, functioning prerequisite links, hardware setup visibility. 11. **Key Entities**: - Module, Chapter, Assessment, Part, Glossary Entry, Hardware Setup Path 12. **Assumptions**: - Students have programming experience - Access to hardware/simulations - 13-week course timeline 13. **Scope Boundaries**: - In scope: chapter structure, metadata, navigation, assessments - Out of scope: full chapter content, embedded video, interactive simulations 14. **Dependencies**: - Docusaurus for deployment, hardware/software versions for simulation - Metadata schema validation 15. **Constitution Compliance Notes**: - Note deviations if any (e.g., embedded code snippets instead of `/examples` directories) and justifications 16. **Additional Notes / Risks**: - Hardware costs, latency issues, syllabus updates, cloud vs local deployment trade-offs Output must be a structured, markdown-ready specification suitable for `specs/book-master-plan/spec.md`, including tables, code blocks, and hierarchical lists where appropriate. Chapters, modules, and weeks must reflect the detailed course and hardware information provided.

## Response snapshot

Generated feature specification for "Physical AI & Humanoid Robotics" textbook, available at `specs/001-robotics-textbook-spec/spec.md`. Checklist `specs/001-robotics-textbook-spec/checklists/requirements.md` created and validated.

## Outcome

- ✅ Impact: Feature specification for robotics textbook created and validated.
- 🧪 Tests: N/A
- 📁 Files: Created `specs/001-robotics-textbook-spec/spec.md` and `specs/001-robotics-textbook-spec/checklists/requirements.md`.
- 🔁 Next prompts: User can proceed with `/sp.plan`.
- 🧠 Reflection: Successfully generated feature specification and associated checklist. Faced initial issues with PowerShell script for feature creation, which were resolved by manually executing steps.

## Evaluation notes (flywheel)

- Failure modes observed: Initial failure of `create-new-feature.ps1` due to argument parsing, circumvented by manual steps.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
