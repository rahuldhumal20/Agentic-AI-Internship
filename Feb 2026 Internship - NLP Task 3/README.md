# 🤖 AI Chatbot using Transformers (DialoGPT)

A conversational AI chatbot built using **Hugging Face Transformers** and **Microsoft DialoGPT**, capable of generating human-like responses using deep learning.

---

## 🚀 Overview

This project demonstrates how to build a **context-aware chatbot** using a pre-trained transformer model. Unlike rule-based bots, this system leverages **state-of-the-art NLP models** to generate dynamic and meaningful conversations.

---

## 🧠 Key Features

- 💬 Human-like conversational responses using DialoGPT
- 🔄 Maintains conversation history (context-aware replies)
- ⚡ Built using PyTorch and Hugging Face Transformers
- 🧩 Simple and extendable architecture
- 🖥️ CLI-based real-time interaction

---

## 🛠️ Tech Stack

- **Language:** Python
- **Libraries:**
  - Transformers (Hugging Face)
  - PyTorch
- **Model Used:**
  - `microsoft/DialoGPT-medium`

---

## 🏗️ Architecture
User Input → Tokenization → Transformer Model (DialoGPT) → Response Generation → Output


- Input text is tokenized using a pretrained tokenizer
- Conversation history is preserved for context
- Model generates response using causal language modeling

---
## 🧩 Code Highlights
- Uses AutoTokenizer and AutoModelForCausalLM
- Maintains chat history with token concatenation
- Limits token size to avoid memory overflow


## ⚠️ Limitations
- May generate incorrect or generic responses
- No fine-tuning on custom dataset
- Runs on CPU by default (can be optimized with GPU)


## 🔮 Future Improvements
- Fine-tune on domain-specific datasets
- Add web interface (React + FastAPI)
- Integrate memory (vector DB like ChromaDB)
- Deploy as API or chatbot service
- Add streaming responses


## 📌 Learning Outcomes
- Practical understanding of transformer-based NLP
- Hands-on experience with Hugging Face ecosystem
- Context handling in conversational AI systems


## 👨‍💻 Author

Rahul Dhumal

