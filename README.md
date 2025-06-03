# 🧠 Online Judge + AI Code Assistant 🖥️

Welcome to **Online Judge + AI Code Assistant**, a full-stack web application that functions as an online compiler, code runner, and judge system for popular programming languages, enhanced with AI-powered coding support.

---

## 🚀 Features

- ✅ **Multi-language Compiler Support**
  - Supports **C**, **C++**, **Python**, and **Java**
  - Secure, sandboxed code execution
  - Real-time output and error messages

- 🔐 **User Authentication System**
  - Login and registration using Django’s built-in auth system
  - User-specific code submission history (coming soon)

- 🤖 **AI-Powered Code Assistance**
  - Integrated with **Google Vertex AI / Gemini API**
  - Helps explain code, fix errors, and offer suggestions

- 📦 **Dockerized for Portability**
  - Fully containerized using Docker
  - Easy to run locally or deploy on cloud platforms

---

## 📸 Demo

> ![Screenshot 2025-06-03 173554](https://github.com/user-attachments/assets/65c69914-c7df-4926-a153-44d74ad6d598)
> ![Screenshot 2025-06-03 173945](https://github.com/user-attachments/assets/7edabf60-03a9-4ff7-8b57-81f189f69293)
> ![Screenshot 2025-06-03 174006](https://github.com/user-attachments/assets/f355b62a-8cdd-45c3-ac39-1f476556a7b6)




---

## 🛠️ Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- A [Google Cloud Service Account key JSON](https://cloud.google.com/docs/authentication/getting-started) with access to Vertex AI (if you want AI features)

### Clone & Run

```bash
# Clone the repository
git clone git@github.com:cosmic-ash18/My_Dev_Project.git
cd My_Dev_Project

# Build the Docker image
docker build -t oj_image .

# Run the container
docker run -it -p 8000:8000 \
  -v /full/path/to/onlinejudgellm-XXXXXX.json:/app/key.json \
  -e GOOGLE_APPLICATION_CREDENTIALS=/app/key.json \
  oj_image
