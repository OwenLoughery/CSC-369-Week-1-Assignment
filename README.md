# r/place 2022 Canvas Analytics

This repository contains projects for a CSC class of mine using the **r/place 2022** dataset. Across these projects, I built data pipelines, ran exploratory analysis, did ML modeling, and produced reproducible reports + interactive visualizations to answer specific questions about user behavior and canvas dynamics.

The point of working with this dataset was to do work on large scale datasets (as the r/place dataset is > 20 GB)

## What’s in this repo

### 1) Preprocessing + Basic Analysis
A preprocessing pipeline to reduce the raw dataset to a manageable format and compute baseline stats (color usage by distinct users, session length, pixels placed percentiles, first-time users, runtime).

Folder: `Preprocessing_Basic_Analysis/`

### 2) Irregular Activity Analysis (Bucketed Findings)
A task to identify "irregular" behavior (bot activity) and group findings into different **buckets** of this irregular activity:
- **Pixel warfare / territorial defense**
- **Low color diversity / task-specialized automation**
- **Mass first-time user spikes (often human coordination)**

Folder: `Irregular_Activity_Report/`

### 3) Predicting Pixel Survival (ML + Interpretation)
Tasked with finding anything interesting about the dataset. Decided to make a machine learning model to predict whether a pixel placement will **survive ≥ 30 minutes** using only information available at placement time. Includes feature engineering, time-based train/test split, model evaluation, and SHAP-based interpretation plus interactive plots.

Folder: `r_place_Find_Something_Interesting/`

## Interactive Visuals
Interactive HTML plots are included in `docs/` and are intended to be viewed via GitHub Pages.
