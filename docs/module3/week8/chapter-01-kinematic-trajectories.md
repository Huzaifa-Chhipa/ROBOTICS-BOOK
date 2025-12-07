import PrerequisiteDisplay from '@site/src/components/PrerequisiteDisplay';

---
title: "Kinematic Trajectories"
description: "Generating smooth robot movements."
slug: "chapter-01-kinematic-trajectories"
week: 8
module: "Module 3: Autonomous Navigation and Manipulation"
prerequisites: ["chapter-02-sampling-based-motion-planning"]
learningObjectives:
  - Understand kinematic trajectories concepts.
estimatedTime: 45
difficultyLevel: "Intermediate"
sidebar_label: "1. Kinematic Trajectories"
position: 1
---

<PrerequisiteDisplay prerequisites={frontMatter.prerequisites} />

# Kinematic Trajectories

This chapter explores generating smooth robot movements, focusing on kinematic trajectories. Once a path is determined by a motion planner, the robot needs to execute it with controlled velocity and acceleration. Kinematic trajectory generation involves computing the time history of joint positions, velocities, and accelerations that allow the robot to follow a given path while respecting its kinematic limits (e.g., maximum joint speeds and accelerations). We will delve into methods such as cubic and quintic polynomial interpolation, which are commonly used to create smooth and continuous joint trajectories. The importance of blending maneuvers and ensuring jerk-limited motions for safer and more efficient robot operation will also be discussed. Understanding kinematic trajectories is crucial for translating abstract paths into executable robot actions.
