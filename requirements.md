## 1. Functional Requirements

### 1.1 User Interaction
- The system shall allow users to enter queries via **text input** through a web interface.
- The system shall allow users to submit queries via **voice input** using **Vosk** or **Whisper** (Speech-to-Text).
- The system shall respond in the **same language** as the user input.
- The system shall support **text output** and optional **voice output** using **Coqui TTS** or **pyttsx3**.

---

### 1.2 Language Processing
- The system shall automatically **detect the input language** using **fastText Language Identification**.
- The system shall translate user queries into a common processing language using **Meta AI M2M100** or **MarianMT** models.
- The system shall translate system responses back into the user’s original language.
- The system shall support **up to 100 languages** through multilingual translation models.

---

### 1.3 Natural Language Understanding
- The system shall analyze user intent using **multilingual NLP models** such as **XLM-Roberta** or **Multilingual BERT (mBERT)**.
- The system shall retrieve the most relevant response using **Sentence Transformers (Multilingual MiniLM)** for semantic similarity.

---

### 1.4 Knowledge Base
- The system shall store predefined questions and answers in **SQLite** or **JSON-based storage**.
- The knowledge base shall be **modifiable, extendable, and domain-agnostic**.

---

### 1.5 Cloud Integration (Optional)
- The system shall support deployment on **AWS EC2** for web hosting.
- The system shall allow static asset storage using **AWS S3**.
- The system shall support scalable backend services using **AWS Lambda** if required.
- Cloud integration shall be optional and used primarily for scalability and centralized access.

---
