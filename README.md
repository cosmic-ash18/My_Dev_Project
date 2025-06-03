# Online Judge + AI Code Assistant

This is a full-stack web application that works as an online compiler, code runner, and judge system. It also includes AI-based coding assistance using Google Vertex AI.

---

## Features

- Multi-language Compiler Support  
  Supports C, C++, Python, and Java with secure sandboxed execution and real-time output/errors.

- User Authentication System  
  Includes login and registration using Django’s built-in authentication. (User-specific history coming soon.)

- AI-Powered Code Assistance  
  Integrated with Google Vertex AI (Gemini API) for code explanations, error correction, and suggestions.

- Dockerized for Portability  
  Fully containerized using Docker. Can be run locally or deployed to cloud platforms.

---

## Demo

![Screenshot 2025-06-03 173554](https://github.com/user-attachments/assets/65c69914-c7df-4926-a153-44d74ad6d598)  
![Screenshot 2025-06-03 173945](https://github.com/user-attachments/assets/7edabf60-03a9-4ff7-8b57-81f189f69293)  
![Screenshot 2025-06-03 174006](https://github.com/user-attachments/assets/f355b62a-8cdd-45c3-ac39-1f476556a7b6)

---

## Getting Started

### Prerequisites

- Docker  
- A Google Cloud service account key JSON with access to Vertex AI  
  (See: https://cloud.google.com/docs/authentication/getting-started)

### Clone and Run

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
