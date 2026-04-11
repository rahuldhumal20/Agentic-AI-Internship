# LangChain Deep Technical Blog — Code Implementation

> **Innomatics Research Labs | Data Science Internship — February 2026**  
> Assignment: GenAI – LangChain Deep Technical Blog

---

## 📌 Overview

This repository contains the complete working code implementation for the **LangChain Deep Technical Blog** assignment. It covers all core LangChain components with hands-on Python examples using the **Groq API** (OpenAI-compatible endpoint) and the **LLaMA 3.3 70B** model.

---

## 🧠 What's Covered

| Section | Concept |
|---|---|
| 1 | Basic LLM Call |
| 2 | Prompt Templates |
| 3 | LCEL Chain (Prompt → LLM) |
| 4 | Conversational Memory |
| 5 | Tools (Calculator Agent) |
| 6 | Modular / Factory Pattern |

---

## 🛠️ Tech Stack

- **Python 3.12**
- **LangChain 1.x** (`langchain`, `langchain-core`, `langchain-openai`)
- **Groq API** (OpenAI-compatible) — Model: `llama-3.3-70b-versatile`
- **Jupyter Notebook**

---

## 💡 Key Concepts Demonstrated

**LLMs & Chat Models** — Direct invocation of chat models via LangChain's unified interface.

**Prompt Templates** — Dynamic, reusable prompt construction using `PromptTemplate.from_template()`.

**LCEL Chains** — Composing components with the pipe (`|`) operator: `prompt | llm`.

**Memory** — Manual chat history management to simulate multi-turn conversational context.

**Tools** — Defining callable tools with the `@tool` decorator for agent use.

**Modular Pattern** — Factory functions for clean, scalable LangChain application design.

---


