# 🚀 Fine-Tuning DistilBERT for POS Tagging & Chunking

## 📌 Overview

This project demonstrates how to fine-tune a transformer model (**DistilBERT**) for **token classification tasks**, specifically:

- 🧠 Part-of-Speech (POS) Tagging  
- 🧩 Chunking (Phrase Detection)

The goal is to understand how modern NLP models can perform **sequence labeling** and capture linguistic structure in text.

---

## 🎯 Objectives

- Perform POS tagging and chunking using transformer models  
- Handle tokenization and label alignment challenges  
- Train and evaluate models using Hugging Face Trainer  
- Compare performance using standard metrics  

---

## ⚙️ Tech Stack

- **Python**
- **Hugging Face Transformers**
- **DistilBERT**
- **NLTK (CoNLL-2000 dataset)**
- **SeqEval (Evaluation Metrics)**

---

## 📂 Dataset

- Used **CoNLL-2000 dataset (via NLTK)**
- Converted into Hugging Face format manually
- Contains:
  - Tokens
  - POS Tags
  - Chunk Tags

---

## 🔄 Workflow

Raw Data → Tokenization → Label Alignment → Model Training → Evaluation → Inference → Comparison

---

## 🔍 Key Concepts

### 🔹 POS Tagging
Assigns grammatical labels to each word.

Example:

John → NNP
works → VBZ


---

### 🔹 Chunking
Groups words into meaningful phrases.

Example:

John → B-NP
works → B-VP


---

## ⚠️ Challenges Faced

- Handling subword tokenization (Word → Subwords)
- Aligning labels correctly with tokens
- Managing dataset loading issues
- Ensuring label consistency across splits

---

## 📊 Results

| Metric | POS Tagging | Chunking |
|--------|------------|----------|
| Precision | 0.8916 | 0.8368 |
| Recall | 0.8918 | 0.8636 |
| F1 Score | 0.8917 | 0.8500 |

---

## ✅ Conclusion

- POS Tagging outperformed Chunking across all metrics  
- Word-level tasks are easier for models to learn  
- Chunking is more complex due to phrase-level structure  

---

## 💡 Insights

- Transformer models capture contextual relationships effectively  
- Proper preprocessing and label alignment are critical  
- Even small errors impact chunking performance significantly  

---

