
from pathlib import Path
from src.llm.ollama_client import OllamaClient


class LuckyAssistant:
    def __init__(self):
        self.client = OllamaClient()

        prompt_path = (
            Path(__file__).parent
            / "prompts"
            / "system_prompt.txt"
        )

        self.system_prompt = prompt_path.read_text(
            encoding="utf-8"
        )

        self.history = []

    def respond(self, user_text):
        messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            },
            *self.history,
            {
                "role": "user",
                "content": user_text,
            },
        ]

        response = self.client.chat(messages)

        self.history.extend([
            {"role": "user", "content": user_text},
            {"role": "assistant", "content": response},
        ])

        # Keep the most recent 10 conversation turns.
        self.history = self.history[-20:]

        return response


assistant = LuckyAssistant()


def ask(user_text):
    return assistant.respond(user_text)
