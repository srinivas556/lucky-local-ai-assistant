

\# Lucky v0.1.0 — Local AI Assistant



Lucky is a Python-based personal AI assistant powered by a locally running language model through Ollama.



\## Features



\- Local language model integration

\- Configurable model and Ollama URL

\- System prompt loaded from an external file

\- Interactive text-based conversation

\- Simple command-line interface



\## Requirements



\- Windows, macOS, or Linux

\- Python 3.12 or later, subject to dependency compatibility

\- \[Ollama](https://ollama.com/)



\## Setup



Install Ollama and download the model:



```bash

ollama pull qwen3:0.6b

```



Create and activate a virtual environment:



```bash

python -m venv .venv

```



On Windows:



```cmd

.venv\\Scripts\\activate

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



Run Lucky from the project root:



```bash

python -m src.main

```



Type your question and press Enter. Type `exit` to quit.



\## Project Structure



```text

lucky/

├── src/

│   ├── main.py

│   ├── assistant.py

│   ├── config.py

│   ├── llm/

│   ├── prompts/

│   ├── tools/

│   └── memory/

├── evaluation/

├── tests/

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

```



\## Privacy



The language model runs locally through Ollama. This release is designed for local inference rather than cloud LLM API calls.



\## Roadmap



\- Voice input and spoken responses

\- Prompt evaluation

\- Tool calling

\- Persistent local memory

\- Safe computer automation



