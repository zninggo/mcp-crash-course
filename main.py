import os

from dotenv import load_dotenv

load_dotenv(override=True)

print(os.getenv('OPENAI_BASE_URL'))

def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    main()
