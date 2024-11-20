# Document QA Engine

A secure and private document question-answering system that runs entirely locally. This system allows you to query your documents using natural language while keeping your data completely private.

## Features

- 🔒 Fully local processing - no data leaves your machine
- 📄 Support for multiple document formats
- 💡 Natural language querying
- �� RAG (Retrieval Augmented Generation) implementation
- 📊 Document embedding and semantic search
- 🔍 Context-aware responses

## Project Structure

- `ingest.py`: Document ingestion and embedding
- `run_localGPT.py`: Main QA interface
- `run_localGPT_API.py`: API endpoint for integration
- `emailGPT/`: Email processing functionality

## Getting Started

1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Place your documents in the SOURCE_DOCUMENTS folder
4. Run `python ingest.py` to process documents
5. Run `python run_localGPT.py` to start querying

## License

See LICENSE file for details
