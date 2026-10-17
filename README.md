\# 🤖 Lucky v0.1.0 — Your Local AI Assistant



> \*\*Building my own AI assistant, one prompt at a time.\*\*



What if you could build your own AI assistant instead of just using one?



\*\*Lucky\*\* is a Python-based personal AI assistant powered by a locally running language model through \[Ollama](https://ollama.com/). This project is my hands-on journey into \*\*prompt engineering, local LLM integration, and conversational AI development\*\*.



The goal isn't just to connect a model to Python. It's to explore how carefully designed instructions, modular code, and thoughtful experimentation can turn a language model into a useful assistant.



\## ✨ What Can Lucky Do Today?



\- 🧠 \*\*Local AI Integration\*\* — Generate responses using a language model running locally through Ollama.

\- 🎯 \*\*Prompt Engineering\*\* — Guide the model's behavior through a dedicated system prompt.

\- 💬 \*\*Interactive Conversations\*\* — Ask questions and receive responses through a command-line interface.

\- ⚙️ \*\*Configurable Setup\*\* — Choose the model and configure the local Ollama server URL.

\- 🔒 \*\*Local-First Design\*\* — Run inference locally instead of relying on a cloud LLM API.



\## 🧪 The Prompt Engineering Experiment



A language model's output depends not only on the model itself, but also on the instructions and context it receives.



Lucky uses an external system prompt to define the assistant's role, response style, and behavioral guidelines. Keeping the prompt separate from the application code makes it easier to refine instructions and experiment with different approaches.



\*\*Areas I want to explore:\*\*

\- Instruction clarity and constraint-following

\- Context-aware follow-up questions

\- Response consistency and reliability

\- Prompt evaluation using repeatable test cases



These experiments will help me understand where prompt design improves results—and where model limitations still matter.



\## 🏗️ How It Works



```text

User Input

&#x20;   |

&#x20;   v

Command-Line Interface

&#x20;   |

&#x20;   v

Assistant + System Prompt

&#x20;   |

&#x20;   v

Ollama API (Local)

&#x20;   |

&#x20;   v

Local Language Model

&#x20;   |

&#x20;   v

Generated Response

&#x20;   |

&#x20;   v

User

```



\## 🛠️ Tech Stack



| Technology | Purpose |

|---|---|

| Python | Application development |

| Ollama | Local LLM runtime |

| Qwen3 | Language model |

| Prompt Engineering | Assistant behavior and instructions |

| Git \& GitHub | Version control and project releases |



\## 🚀 Getting Started



\### Requirements



\- Windows, macOS, or Linux

\- Python 3.12 or later, subject to dependency compatibility

\- \[Ollama](https://ollama.com/)



\### 1. Download the model



Install Ollama, then run:



```bash

ollama pull qwen3:0.6b

```



\### 2. Clone the repository



```bash

git clone https://github.com/srinivas556/lucky-local-ai-assistant.git

cd lucky-local-ai-assistant

```



\### 3. Create a virtual environment



```bash

python -m venv .venv

```



Activate it on Windows:



```cmd

.venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Run Lucky



From the project root:



```bash

python -m src.main

```



Type your question and press Enter. Enter `exit` to quit.



\## 📁 Project Structure



```text

lucky-local-ai-assistant/

├── src/

│   ├── main.py

│   ├── assistant.py

│   ├── config.py

│   ├── llm/

│   ├── prompts/

│   ├── tools/

│   └── memory/

├── docs/

├── evaluation/

├── tests/

├── .env.example

├── .gitignore

├── requirements.txt

└── README.md

```



\## 🗺️ Development Roadmap



\- \[x] Local LLM integration

\- \[x] External system prompt

\- \[x] Text-based interaction

\- \[ ] Voice input and spoken responses

\- \[ ] Systematic prompt evaluation

\- \[ ] Functional tool calling

\- \[ ] Persistent local memory

\- \[ ] Safe computer automation



\## 🔐 Privacy



Lucky is designed around local inference through Ollama. In this version, prompts are sent to the locally configured Ollama server rather than a cloud LLM API. Network exposure and any additional integrations depend on the user's configuration.



\## 🎯 The Bigger Goal



I'm building Lucky to learn how AI assistants are designed—not just how to call an LLM, but how to guide its behavior, evaluate its responses, integrate it into software, and improve it through iterative development.



\*\*Version 1 is the foundation. Every future release will build on it.\*\*



\*Built with Python, curiosity, and a growing interest in prompt engineering and AI systems.\*

