import PrerequisiteDisplay from '@site/src/components/PrerequisiteDisplay';

---
title: "Dynamic Trajectories"
description: "Considering forces and inertias in motion."
slug: "chapter-02-dynamic-trajectories"
week: 8
module: "Module 3: Autonomous Navigation and Manipulation"
prerequisites: ["chapter-01-kinematic-trajectories"]
learningObjectives:
  - Understand dynamic trajectories concepts.
estimatedTime: 45
difficultyLevel: "Intermediate"
sidebar_label: "2. Dynamic Trajectories"
position: 2
---

<PrerequisiteDisplay prerequisites={frontMatter.prerequisites} />

# Dynamic Trajectories

This chapter explores considering forces and inertias in motion, moving beyond purely kinematic considerations to generate dynamic trajectories. While kinematic trajectories ensure smooth joint movements, dynamic trajectories take into account the robot's mass, inertia, and external forces, which is essential for high-speed or high-payload operations. We will delve into methods that incorporate the robot's dynamic model directly into the trajectory generation process, often involving optimization techniques to minimize energy consumption, execution time, or vibrations. Concepts such as inverse dynamics control and feedforward control based on dynamic models will be introduced. Understanding dynamic trajectories is crucial for achieving more precise, efficient, and robust robot control, especially in tasks requiring agile movements or interaction with the environment.
