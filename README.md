# Langchain API with Ollama Model

This project provides a simple **API** built with **FastAPI** and the **LangChain** library using the **Ollama** model (`llama3.2:1b`). The API is capable of generating poems and having cheerful conversations based on user input.

## Features

- **Poem Generation**: Generate a poem about a specified topic for a 5-year-old child, with around 100 words.
- **Cheerful Conversations**: Engage in a positive and cheerful chat on a specific topic.

## Requirements

To get started with the project, you need the following installed:

- Python 3.7+
- FastAPI
- Uvicorn (for running the FastAPI app)
- Langchain
- Ollama (for language model interactions)
- dotenv (for loading environment variables)

## Setup

### Step 1: Clone the repository

Clone this repository to your local machine using Git.

```bash
git clone https://github.com/yourusername/Updated-Langchain.git
cd Updated-Langchain
```

### Step 2: Install dependencies

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 3: Set up environment variables

Make sure to create a `.env` file at the root of the project and add the following environment variables:

```bash
OPENAI_API_KEY=your-openai-api-key
```

Replace `your-openai-api-key` with your actual OpenAI API key if required.

### Step 4: Run the FastAPI server

To start the FastAPI server, run the following command:

```bash
python app.py
```

This will start the FastAPI server, which will be accessible at `http://localhost:8007`.

## API Endpoints

### 1. `/poem` - Generate a poem

**Method**: POST

**Description**: Generate a poem about a given topic for a 5-year-old child with approximately 100 words.

**Request body**:
```json
{
  "topic": "Your desired topic"
}
```

**Response**:
```json
{
  "output": "Generated poem content here."
}
```

**Example**:
```bash
curl -X 'POST' \
  'http://localhost:8007/poem' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "nature"
}'
```

### 2. `/chat` - Engage in a cheerful conversation

**Method**: POST

**Description**: Initiate a cheerful chat on a given topic with positive words.

**Request body**:
```json
{
  "topic": "Your desired chat topic"
}
```

**Response**:
```json
{
  "output": "Generated cheerful conversation content here."
}
```

**Example**:
```bash
curl -X 'POST' \
  'http://localhost:8007/chat' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "friendship"
}'
```

## Running the Server

Once the server is running, you can interact with it by sending `POST` requests to the `/poem` or `/chat` endpoints.

To test the API locally, you can use **Postman** or **cURL** to send requests.

## Example cURL Commands

1. To generate a poem about "nature":

```bash
curl -X 'POST' \
  'http://localhost:8007/poem' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "nature"
}'
```

2. To engage in a cheerful chat about "friendship":

```bash
curl -X 'POST' \
  'http://localhost:8007/chat' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "friendship"
}'
```

## Conclusion

This project demonstrates how to build a simple API using FastAPI and LangChain's Ollama model for generating creative content like poems and positive chat conversations. The API can be extended to support additional prompts and models as needed.
