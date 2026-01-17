---
title: Diabetes Prediction System
emoji: 🏥
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# Diabetes Prediction System

An AI-powered diabetes risk analysis tool using machine learning to predict diabetes based on the Pima Indians dataset.

## Features
- Interactive web interface built with Gradio
- Real-time diabetes risk prediction
- Professional UI with reference ranges
- Sample test cases included

## How to Use
1. Enter patient information in the form
2. Click "Analyze Risk" to get prediction
3. View confidence score and risk level

## Model Features
The model uses 8 key features:
- Pregnancies
- Glucose level
- Blood Pressure
- Skin Thickness
- Insulin level
- BMI
- Diabetes Pedigree Function
- Age

## Local Setup
```bash
pip install -r requirements.txt
python app.py
```