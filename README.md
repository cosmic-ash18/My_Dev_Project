# Online Judge -> CodeUmpire

This is a full-stack web application in Django that works as an online compiler and judge system with both user inputs and test cases. It also includes AI-based coding assistance using Google Vertex AI.

---

## Features

- Multi-language Compiler Support  
  Supports C, C++, Python, and Java with secure sandboxed execution and real-time outputs.

- User Authentication System  
  Includes login and registration using Django’s built-in authentication.

- AI-Powered Code Assistance  
  Integrated with Google Vertex AI (Gemini API) for code explanations and suggestions.

### Prerequisites

- A Google Cloud service account key JSON with access to Vertex AI  
  (See: https://cloud.google.com/docs/authentication/getting-started)

### Clone and Run

```bash
# Clone the repository
git clone git@github.com:cosmic-ash18/My_Dev_Project.git
cd My_Dev_Project

# Build the Docker image
docker build -t oj_image .

```
Current deployment link: http://3.108.65.217:8000/
