from dotenv import load_dotenv
import os


if __name__ == "__main__":
    print(f"Hello Langchain")
    # load .env file
    load_dotenv()
    print(os.environ["OPENAI_API_KEY"])
