
import sys
import time
from pathlib import Path

import pyttsx3

# Add the original project root to Python's import path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.assistant import ask
from src.voice import listen


EXIT_WORDS = {
    "exit", "quit", "goodbye", "stop", "close", "bye"
}


def speak(engine, text):
    print(f"\nLucky: {text}\n")
    engine.say(text)
    engine.runAndWait()


def main():
    print("=" * 45)
    print("       LUCKY v0.3.0 - TALKING MODE")
    print("=" * 45)
    print("Speak after the listening message.")
    print("Say 'Lucky, stop' or press Ctrl+C to exit.\n")

    engine = pyttsx3.init()
    engine.setProperty("rate", 175)
    engine.setProperty("volume", 1.0)

    speak(engine, "Hello! I am Lucky. I am ready to talk with you.")

    try:
        while True:
            try:
                user_text = listen().strip()

                if not user_text:
                    print("I couldn't recognize that. Please try again.")
                    continue

                print(f"\nYou: {user_text}")

                # Check for exit phrases anywhere in the recognized text.
                words = set(user_text.lower().replace(".", "").replace(",", "").split())
                if words.intersection(EXIT_WORDS):
                    speak(engine, "Goodbye! It was nice talking with you.")
                    break

                print("Lucky is thinking...")
                response = ask(user_text)

                if response and response.strip():
                    speak(engine, response.strip())
                else:
                    speak(engine, "Sorry, I couldn't generate a response.")

            except KeyboardInterrupt:
                print("\nStopping Lucky...")
                break
            except Exception as error:
                print(f"Error: {error}")
                speak(engine, "Something went wrong. Please try again.")

    finally:
        engine.stop()
        print("Lucky has stopped.")


if __name__ == "__main__":
    main()

