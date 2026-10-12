
from src.assistant import ask


def main():
    print("Lucky v0.1.0 - Local AI Assistant")
    print("Type your question. Enter 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {
                "exit", "quit", "goodbye", "stop", "close", "bye"
            }:
                print("Lucky: Goodbye!")
                break

            response = ask(user_input)
            print(f"Lucky: {response}\n")

        except KeyboardInterrupt:
            print("\nLucky: Goodbye!")
            break
        except Exception as error:
            print(f"Lucky: Something went wrong: {error}")


if __name__ == "__main__":
    main()
