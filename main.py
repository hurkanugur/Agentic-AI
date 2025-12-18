from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
from groq import Groq

def main():
    load_dotenv()

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": "Design an autonomous research agent"}
        ]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
