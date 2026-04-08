# 🚀 GenAI Prompt Engineering with LangChain

### Mastering Prompt Templates & Dynamic Prompt Systems

---

## 📌 Project Overview

This project demonstrates how to build **dynamic and reusable prompt systems** using **LangChain PromptTemplate** instead of hardcoded prompts.

The goal is to simulate a **real-world prompt engineering pipeline**, where user inputs are validated and converted into structured prompts for AI models.

---

## 🎯 Objectives

* Replace hardcoded prompts with reusable templates
* Build multi-input prompt systems
* Create prompt variations (teaching, interview, storytelling)
* Implement chat-based prompt systems using roles
* Add input validation for robust prompt generation
* Design a modular prompt generator application

---

## 🛠️ Tech Stack

* Python 🐍
* LangChain
* Jupyter Notebook / Google Colab

---

## 🔥 Features Implemented

### ✅ Task 1: PromptTemplate (Basic)

* Converted hardcoded prompts into reusable templates

### ✅ Task 2: Multi-Input Prompt System

* Dynamic inputs: `topic`, `audience`, `tone`

### ✅ Task 3: Prompt Variations Engine

* Teaching → Step-by-step explanation
* Interview → Question generation
* Storytelling → Creative explanation

### ✅ Task 4: ChatPromptTemplate System

* Role-based prompting:

  * Teacher 👨‍🏫
  * Interviewer 🎯
  * Motivator 💡

### ✅ Task 5: Input Validation Layer

* Validates:

  * Audience → beginner, intermediate, expert
  * Tone → formal, casual, fun
* Handles invalid inputs with defaults

### ✅ Task 6: Prompt Generator App

* Combines all components into one function
* Generates structured prompts dynamically

### ✅ Task 7: Template Reusability Test

* Same template used with multiple inputs
* Demonstrates flexibility and scalability

---

## 🔄 Workflow

```
User Input 
   ↓
Validation Layer
   ↓
PromptTemplate
   ↓
Dynamic Prompt Generation
   ↓
Output
```

---

## 💻 Example Output

```
Input:
Topic = Neural Networks  
Audience = beginner  
Tone = fun  
Style = storytelling  

Output:
Explain Neural Networks as a story for beginner in a fun tone
```

---

## ⚠️ Important Rules Followed

* ❌ No hardcoded prompts
* ❌ No f-strings
* ✅ Used PromptTemplate
* ✅ Modular and reusable design
* ✅ Clean and structured code

---

## 📈 Learning Outcomes

* Understanding of prompt engineering concepts
* Ability to design reusable prompt systems
* Experience with LangChain PromptTemplate
* Real-world AI pipeline thinking

---




