## 1. System Overview
The **Bharat Citizen Assistant** is a specialized AI-powered multilingual system designed to help Indian citizens access information about government schemes and public services. The system processes user queries in Hindi, English, and regional Indian languages, understands citizen intent, identifies relevant government schemes, and provides clear information about eligibility, required documents, and application processes. Designed for users with low digital literacy and optimized for low-bandwidth environments.

---

## 2. System Architecture 

The following diagram represents the high-level architecture of the Bharat Citizen Assistant and illustrates how different components interact to serve Indian citizens.

+----------------------+
|    Citizen User      |
| (Text Input/Voice)   |
| Hindi/English/Regional|
+----------+-----------+
           |
           v
+----------------------+
|   Web Frontend UI    |
| (Responsive Design)  |
| (Low Bandwidth Opt.) |
+----------+-----------+
           |
           v
+----------------------+
|   Flask API Layer    |
| (Citizen Services)   |
+----------+-----------+
           |
           v
+----------------------+
| Language Detection   |
|   (fastText)         |
| (10 Indian Languages)|
+----------+-----------+
           |
           v
+----------------------+
| Intent Classification|
| (Scheme Inquiry/     |
| Eligibility/Process) |
+----------+-----------+
           |
           v
+----------------------+
| Government Schemes   |
| Knowledge Base       |
| (SQLite Database)    |
+----------+-----------+
           |
           v
+----------------------+
| Response Generation  |
| (Contextual/Simple)  |
+----------+-----------+
           |
           v
+----------------------+
| Multilingual Output  |
| (Same as Input Lang) |
+----------------------+

Supported Government Schemes:
-----------------------------
- PM-KISAN (Farmer Support)
- Ayushman Bharat (Health Insurance)
- MUDRA Yojana (Business Loans)
- Extensible for more schemes


## 3. Architecture Description

- The user interacts with the system through a web browser using text or voice input.
- The frontend sends the request to the backend API layer.
- The backend detects the input language using fastText.
- The query is translated into a standard processing language using multilingual translation models.
- NLP models analyze the intent and retrieve relevant information from the knowledge base.
- The response is generated and translated back into the user’s language.
- The final output is delivered as text or synthesized speech.
- AWS cloud services are optionally used for scalable deployment and centralized access.


## 4. Component Design

### 4.1 Web Interface
- Built using HTML, CSS, and JavaScript.
- Provides text input, voice input, and response display.
- Acts as the interaction layer between the user and backend.

---

### 4.2 Language Detection Module
- Uses **fastText** for identifying the language of user input.
- Automatically selects the appropriate processing flow.

---

### 4.3 Translation Module
- Uses **Meta AI M2M100** or **MarianMT** models.
- Converts user input into a standard language for processing.
- Translates responses back into the user’s original language.

---

### 4.4 NLP Processing Module
- Uses **XLM-Roberta / Multilingual BERT / Sentence Transformers**.
- Understands user intent and extracts meaning from queries.
- Matches queries with relevant knowledge base entries.

---

### 4.5 Knowledge Base
- Implemented using **SQLite or JSON files**.
- Stores predefined responses and information.
- Easily extendable for new domains.

---

### 4.6 Speech Processing (Optional)

#### Speech-to-Text
- Uses **Vosk** or **Whisper** to convert voice input into text.

#### Text-to-Speech
- Uses **Coqui TTS** or **pyttsx3** to convert responses into speech.

---

### 4.7 Cloud Integration (Optional)
- **AWS EC2**: Hosting the web application.
- **AWS S3**: Static assets and storage.
- **AWS Lambda**: Backend APIs.
- Enables scalability and centralized deployment.

---

## 5. Data Flow
1. Citizen submits query about government schemes via web interface.
2. Language detection identifies the input language (Hindi, English, or regional).
3. Intent classification determines query type (eligibility, application, documents, etc.).
4. System searches government schemes database for relevant information.
5. Response is generated with clear, actionable information.
6. Output is delivered in the citizen's original language.
7. Query is logged for analytics and system improvement (privacy-compliant).

---
