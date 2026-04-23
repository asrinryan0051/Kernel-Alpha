
# kernel Alpha

### Advanced Exam Intelligence System

**kernel-alpha** is a data-driven analytical engine designed to identify high-probability examination patterns using concept-based intelligence.

It transforms unstructured question papers into structured datasets and applies statistical and semantic analysis to extract important topics and questions.

---

## 🚀 Key Features

* **CORe Algorithm (Concept-Oriented Retrieval Engine):**
  A hybrid model combining concept-based grouping (`topic_id`) and clustering to identify important exam patterns.

* **Concept-Level Analysis:**
  Groups questions by underlying concepts instead of relying on exact wording.

* **Multi-Paper Intelligence:**
  Aggregates multiple exam papers to detect recurring patterns.

* **Structured Data Pipeline:**
  Converts raw question papers into a normalized relational database.

* **High-Speed Backend:**
  Built with FastAPI for efficient data processing.

* **Multi-Subject Support:**
  Works across subjects like DBMS, Algorithms, AI/ML, and Theory of Computation.

---

## 🧠 CORe Algorithm

The CORe Algorithm is the central intelligence layer.

### 🔹 Core Idea

Repeated concepts across multiple exam papers indicate higher importance.

---

### 🔹 Pipeline

Question Papers
↓
Structured Database
↓
Concept Mapping (topic_id)
↓
Clustering (semantic similarity)
↓
Frequency Analysis
↓
Scoring & Ranking
↓
Important Questions Output

---

### 🔹 Key Components

* **Concept Mapping (`topic_id`):**
  Groups semantically similar questions under a single concept. uses TF-IDF Vetorization

* **Clustering (Agglomerative):**
  Identifies variations in wording within the same concept.

* **Frequency-Based Scoring:**
  Measures how often a concept appears across papers.

* **Hybrid Approach:**
  Combines deterministic mapping with unsupervised learning.

---

## 🧱 Database Architecture

subjects
↓
units
↓
topics
↓
questions ← exam_papers

### Tables:

* `subjects` → subject metadata
* `units` → syllabus structure
* `topics` → concept layer (core to analysis)
* `exam_papers` → paper metadata
* `questions` → extracted dataset

---

## ⚙️ Tech Stack

* Language: Python 3.9+
* Backend: FastAPI
* Machine Learning: Scikit-learn (Agglomerative Clustering)
* Database: SQLite
* Frontend: HTML / CSS / Jinja2
* Deployment Ready: Vercel-compatible

---

## 📁 Project Structure

.
├── main.py
├── CORe_algorithm.py
├── projectx.db
├── requirements.txt
├── vercel.json
├── static/
└── templates/

---

## 🌐 Deployment

* Platform: Vercel
* Runtime: @vercel/python
* Database: SQLite (bundled as read-only)

---

## ⚡ Performance

* Efficient for 1000+ questions
* Optimized using indexing (paper_id, topic_id)
* Designed for read-heavy workloads

---

## 📌 Status

Production-ready system

---

## 📄 License

For educational and portfolio use. All rights reserved.
