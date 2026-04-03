# 📌 BERT Sentiment Analysis (IMDB Dataset)

## 🚀 Overview  
This project demonstrates how to fine-tune a **BERT (Bidirectional Encoder Representations from Transformers)** model for sentiment analysis on the IMDB movie reviews dataset.  
The model classifies reviews as **positive** or **negative** using a transformer-based deep learning approach.

---

## 🎯 Objectives  
- Understand transformer-based NLP models  
- Perform text preprocessing and tokenization  
- Fine-tune a pre-trained BERT model  
- Evaluate performance using multiple metrics  

---

## 🧠 Key Concepts Covered  
- BERT Architecture  
- Tokenization using `bert-base-uncased`  
- Fine-Tuning with Hugging Face Transformers  
- PyTorch-based training pipeline  
- Evaluation Metrics:
  - Accuracy  
  - Precision  
  - Recall  
  - F1 Score  
  - Confusion Matrix  

---

## 📂 Dataset  
- **Dataset Used:** IMDB Movie Reviews  
- Contains labeled movie reviews:
  - Positive (1)  
  - Negative (0)  

👉 Download from Kaggle:  
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews  

---

## ⚙️ Tech Stack  
- Python  
- Hugging Face Transformers  
- PyTorch  
- Scikit-learn  
- Pandas  
- Google Colab  

---

## 🔄 Project Workflow  

Raw Data → Preprocessing → Tokenization → Model Training → Evaluation  

---

## 🏗️ Model Details  
- **Model Used:** `bert-base-uncased`  
- **Task:** Binary Text Classification  
- **Optimizer:** AdamW  
- **Learning Rate:** 2e-5  
- **Epochs:** 2  

---

## 📊 Evaluation Metrics  

| Metric      | Description |
|------------|------------|
| Accuracy   | Overall correctness |
| Precision  | Correct positive predictions |
| Recall     | Coverage of actual positives |
| F1 Score   | Balance of precision & recall |

---



## 🧪 Experiments  
- Fine-tuned full BERT model  
- (Optional) Freeze BERT layers  
- Compared performance across configurations  

---

