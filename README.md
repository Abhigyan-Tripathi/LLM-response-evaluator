# LLM-response-evaluator

LLM-Judge is a lightweight system for evaluating which of two Large Language Model (LLM) responses is better, using a fine-tuned DeBERTa classification model.  
The project includes model training, an inference pipeline, a Flask backend server, and a minimal frontend UI.

---

## Overview

This repository provides:

- A fine-tuned preference model trained on the Kaggle "LLM Classification Finetuning" competition dataset.
- A Flask server exposing an API endpoint (`POST /judge`) to evaluate two responses.
- A simple HTML/JS frontend for interacting with the backend.
- A reproducible training notebook and inference scripts.

---

## Screenshot of working prototype
<img width="1438" height="779" alt="Screenshot 2025-12-19 at 7 13 03 PM" src="https://github.com/user-attachments/assets/0088d559-4c43-432d-8e20-0c6bf8d22c21" />

## Repository Structure
~~~
project/
│── README.md
│── requirements.txt # Python dependencies
│── inference.py # Inference pipeline for running the model
│── app.py # Flask backend server
│── index.html # Frontend interface
│── model_finetuning.ipynb # Kaggle notebook for training and exporting the model
~~~

## Installation steps

### 1. Clone the repository

~~~bash
git clone https://github.com/Abhigyan-Tripathi/LLM-response-evaluator.git
cd LLM-response-evaluator
~~~

### 2. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 3. Add your model

Place your fine-tuned model inside the model/ directory.
If using a zipped model from Kaggle, extract it into this folder.

### 4. Start the server:
~~~bash
python app.py
~~~

### 5. Running the frontend
Open index.html in your browser.
