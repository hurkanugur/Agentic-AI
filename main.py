from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
import os


def main():
    load_dotenv()

    person = "Hürkan Uğur"

    template = """
    You are an expert AI assistant helping {person} with Agentic AI.
    Provide detailed and accurate information in your responses.
    """

    prompt_template = PromptTemplate(
        input_variables=["person"],
        template=template
    )

    #llm = ChatOpenAI(
    #    model="llama-3.1-8b-instant",
    #    temperature=0.7,
    #    openai_api_key=os.getenv("OPENAI_API_KEY"),
    #    openai_api_base="https://api.groq.com/openai/v1"
    #)

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0.7,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base="https://api.groq.com/openai/v1"
    )

    test

    chain = prompt_template | llm

    response = chain.invoke({"person": person})

    print(response.content)


if __name__ == "__main__":
    main()
