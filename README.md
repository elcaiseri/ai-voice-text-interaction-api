# AI Voice and Text Interaction API

This project is an AI model capable of understanding and responding to voice and text inputs related to specific business logic operations. The AI model interacts using HTTP protocol, receiving voice data as arrays of bytes and returning voice responses as arrays of bytes. Additionally, it handles text inputs and outputs in JSON format.

## Table of Contents

- [Overview](#overview)
- [Functional Requirements](#functional-requirements)
- [Endpoints](#endpoints)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Docker Setup](#docker-setup)
- [Testing the Application](#testing-the-application)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

Developed to handle business logic operations, this AI model supports voice and text interactions. It converts received voice data to text, understands the user's intent, processes the business logic, and generates an appropriate response.

## Functional Requirements

### Voice Interaction
- **Input**: Voice data received as an array of bytes.
- **Output**: Voice response as an array of bytes.
- **Process**: Convert the received voice data to text, understand the user's intent, and generate an appropriate voice response.

### Text Interaction
- **Input**: Text data received as JSON.
- **Output**: Text response in JSON format.
- **Process**: Understand the text input, process the business logic, and generate a relevant text response.

## Endpoints

- **GET `/`**: Welcome message.
- **GET `/health`**: Health check endpoint.
- **POST `/api/voice-input`**: Accepts voice data and returns a voice response.
- **POST `/api/text-input`**: Accepts text data and returns a text response.

## Setup and Installation

### Prerequisites

- Python 3.8 or above
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/elcaiseri/ai-voice-text-interaction-api.git
   cd ai-voice-text-interaction-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the application at `http://localhost:8000`.

### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t my-fastapi-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -d --name fastapi-container -p 8000:8000 my-fastapi-app
   ```

## Testing the Application

### Voice Input

Use the following `curl` command to test the `/api/voice-input` endpoint (ensure you have a `sample.wav` file):

```bash
curl -X POST "http://localhost:8000/api/voice-input" \
    -H "Content-Type: multipart/form-data" \
    -F "file_upload=@sample.wav;type=audio/wav" --output response.wav
```

### Text Input

Use the following `curl` command to test the `/api/text-input` endpoint:

```bash
curl -X POST "http://localhost:8000/api/text-input" -H "Content-Type: application/json" -d '{"input": "How many items do I have in location X?"}'
```

## Project Structure

```
ai_model
│
├── app
│   ├── main.py
│   ├── nlp.py
│   ├── voice.py
│   ├── business_logic.py
│   ├── responses.py
│   └── models
│       └── user_input.py
│
├── tests
│   ├── test_main.py
│   └── test_business_logic.py
│
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
