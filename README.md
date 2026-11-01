# Comparative Evaluation of Clean-Trained and Noise-Augmented 1D-CNN Models for ECG Arrhythmia Classification

## Overview

This project develops a One-Dimensional Convolutional Neural Network (1D-CNN) for ECG heartbeat classification and investigates its robustness against different types of signal noise.

Two models will be compared:
- A baseline model trained on clean ECG signals.
- A noise-augmented model trained using clean and artificially corrupted ECG signals.

Their performance will be evaluated under clean and noisy testing conditions.

## Dataset

- MIT-BIH Arrhythmia Database
- Source: PhysioNet

## Objectives

- Explore and preprocess ECG recordings.
- Extract individual heartbeats using ECG annotations.
- Implement an AAMI-style five-class heartbeat classification system.
- Train a baseline 1D-CNN on clean ECG signals.
- Introduce controlled noise into training and testing signals.
- Train a noise-augmented 1D-CNN.
- Compare both models across different noise types and signal-to-noise ratios (SNRs).
- Evaluate performance using accuracy, precision, recall, F1-score and confusion matrices.

## Noise Conditions

The planned noise types include:
- Gaussian noise
- Baseline wander
- Power-line interference
- Electrode-motion-like artifacts

## Experimental Comparison

The project will compare:
1. Clean-trained model on clean ECG data.
2. Clean-trained model on noisy ECG data.
3. Noise-augmented model on clean ECG data.
4. Noise-augmented model on noisy ECG data.

Patient-independent data splitting will be used to reduce the risk of patient-level data leakage.

## Technologies

- Python
- NumPy and Pandas
- Matplotlib
- SciPy
- WFDB
- TensorFlow / Keras
- Scikit-learn
- Streamlit (planned demonstration interface)

## Expected Deliverables

- ECG preprocessing and classification pipeline.
- Two trained 1D-CNN models.
- Comparative evaluation tables and visualizations.
- Noise robustness analysis.
- Reproducible notebooks and documented source code.
- Interactive demonstration interface (planned).

## Project Status

Initial setup and dataset exploration phase.