# 🧠 Sentiment Analysis using NLP Pipeline & Machine Learning

## 📌 Project Overview
This project implements a complete **Sentiment Analysis system** using Natural Language Processing (NLP) techniques and Machine Learning models.

The objective is to transform raw text data into meaningful numerical features and classify sentiments as **Positive or Negative**.

This project is developed as part of a **Data Science Internship (February 2026)**.

---

## 🚀 Project Workflow

Raw Data → Text Preprocessing → Feature Engineering → Model Training → Evaluation → Comparison

---

## 📂 Dataset
- Source: Kaggle (IMDb Movie Reviews Dataset)
- Total Samples: 50,000 reviews
- Labels:
  - Positive
  - Negative

---

## 🔧 Technologies Used
- Python
- Pandas, NumPy
- NLTK (Natural Language Processing)
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

---

## 🔍 NLP Preprocessing Steps
The following preprocessing steps were applied:

- Lowercasing text
- Removing punctuation and special characters
- Removing stopwords
- Tokenization
- Lemmatization
- Removing URLs

Reusable preprocessing functions were created for clean and efficient processing.

---

## 📊 Feature Engineering

Two vectorization techniques were used:

### 1. Bag of Words (BoW)
- Converts text into frequency-based vectors
- Simple but ignores context

### 2. TF-IDF
- Assigns importance to words based on uniqueness
- Reduces noise from common words
- Performed better than BoW

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Naive Bayes (MultinomialNB)
- Decision Tree

---

## 📈 Model Performance

### Logistic Regression
- Accuracy: **86%**
- Balanced precision and recall
- Best overall performance

### Naive Bayes
- Accuracy: **86%**
- Fast and efficient
- Slightly higher false negatives

### Decision Tree
- Accuracy: **69%**
- Poor performance due to overfitting
- Not suitable for sparse text data

---

## 🔍 Confusion Matrix Insights

- Logistic Regression showed balanced predictions with fewer errors
- Naive Bayes had lower false positives but higher false negatives
- Decision Tree had high misclassification rates

---

## 🧪 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 📊 Key Insights

- TF-IDF outperformed Bag of Words for text classification
- Logistic Regression is the most reliable model for sentiment analysis
- Naive Bayes is a good choice for faster computation
- Decision Trees are not suitable for high-dimensional sparse data

---

## 🎯 Conclusion

This project demonstrates how raw text data can be processed and transformed into meaningful insights using NLP techniques and machine learning models.

Among all models, **Logistic Regression with TF-IDF** provided the best performance, making it the most suitable choice for this sentiment analysis task.

---

## 👨‍💻 Author
**Rahul Dhumal**  