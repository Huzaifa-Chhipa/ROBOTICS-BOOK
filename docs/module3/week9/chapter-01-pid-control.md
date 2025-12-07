import PrerequisiteDisplay from '@site/src/components/PrerequisiteDisplay';

---
title: "PID Control"
description: "Basic feedback control for robots."
slug: "chapter-01-pid-control"
week: 9
module: "Module 3: Autonomous Navigation and Manipulation"
prerequisites: ["chapter-02-dynamic-trajectories"]
learningObjectives:
  - Understand pid control concepts.
estimatedTime: 45
difficultyLevel: "Intermediate"
sidebar_label: "1. PID Control"
position: 1
---

<PrerequisiteDisplay prerequisites={frontMatter.prerequisites} />

# PID Control

This chapter explores basic feedback control for robots, with a deep dive into the Proportional-Integral-Derivative (PID) controller. Building on the introduction from earlier, we will now examine the mathematical formulation of the PID controller and systematically analyze the impact of each of its three terms on system response: the proportional term for immediate error correction, the integral term for eliminating steady-state errors, and the derivative term for damping oscillations and predicting future errors. Various methods for tuning PID gains, such as the Ziegler-Nichols method and trial-and-error approaches, will be discussed. We will also address the limitations of classical PID control, particularly in highly nonlinear or uncertain robotic systems, setting the stage for more advanced control strategies. Practical examples of PID implementation in robot joints and end-effector control will be presented.
