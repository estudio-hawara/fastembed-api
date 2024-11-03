# Fastembed API

## Overview

**Fastembed API** provides a straightforward way to generate text embeddings for paragraphs, making it easier to retrieve vector embeddings for downstream tasks like semantic search or text similarity.

### Context

It was developed as a companyon of [Boc·ajarro](https://github.com/estudio-hawara/boc-ajarro) which, as is written in PHP, needed some Python help in order to create text embeddings in order to feed a vector database.

As it's meant to be executed in a server without a graphic card, it doesn't rely on expensive (in terms of computation) Pytorch setups. Instead, it uses [FastEmbed](https://github.com/qdrant/fastembed/) so it can be executed in the CPU's of a standard Virtual Private Server.

### Limitations

- Currently, the API supports multilingual embeddings using the model [sentence-transformers/paraphrase-multilingual-mpnet-base-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2) and accepts text input one paragraph at a time.

- As it's meant to be executed in a private network, it does not implement any authentication (or authorization) mechanism.

## Installation

To get started, clone the repository:

```bash
git clone https://github.com/estudio-hawara/fastembed-api
cd fastembed-api
```

### Local Environment

For a local setup using a virtual environment:

```bash
# 1. Create a Python virtual environment
python -m venv .venv

# 2. Activate the Python virtual environment
source .venv/bin/activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Start the service
uvicorn main:app
```

The API should now be available at `http://localhost:8000`.

### Docker Environment

To use Docker, follow these steps:

```bash
# 1. Build the Docker Image
docker compose build

# 2. Start the Service as a Background Container
docker compose up -d
```

The API should now be available at `http://localhost:8000`.

## Endpoints

### `/embed` Endpoint

- **Method**: `POST`
- **Description**: Accepts a paragraph of text and returns vector embeddings for that text.

- **Request**:

  - Content-Type: `application/json`
  - JSON Body: `{ "paragraph": "Your paragraph here" }`

- **Response**:
  - JSON Body: `{ "embeddings": [ ... ] }`
  - The `embeddings` attribute contains an array with the embedding vectors.

### `/health` Endpoint

- **Method**: `GET`
- **Description**: Returns a 200 status if the service is up and ready.

#### Health Check in Docker Compose

The `docker-compose.yml` file includes the following `healthcheck` configuration to ensure the service is fully initialized:

```yaml
healthcheck:
  test: curl --fail http://localhost:8000/health || exit 1
  interval: 2s
  timeout: 5s
  retries: 3
  start_period: 5s
```

This configuration ensures that Docker waits until the service is ready before marking it as "healthy."

## Persistent Docker Volume

This project caches FastEmbed files in a temporary directory for quicker container restarts. The `.onnx` model and related files are stored in a Docker volume as specified in `docker-compose.yml`:

```yaml
volumes:
  - fastembed_cache:/tmp/fastembed_cache
```

Using this volume prevents repeated downloads of model files, speeding up restarts and preserving cache data between runs.

## Requirements

- **Python**: 3.12 (>=3.12 and <3.13)
- **Docker**: No specific version required.

## Testing

To run unit tests:

```bash
pytest
```

These tests ensure basic functionality. Benchmark tests will be added in future updates.

## License

This project is licensed under the MIT License.
