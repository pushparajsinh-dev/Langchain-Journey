import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the e.env file
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment variables or .env file")

#Store the API key in the api_key variable
os.environ["GROQ_API_KEY"] = api_key

prompts = ChatPromptTemplate.from_messages([
    ("system", "You are required to translate the {input_language} to {output_language}."),
    ("human", "{input}"),
    ])

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1)

output_parser = StrOutputParser()

chain = prompts | llm | output_parser

output = chain.invoke({
    "input_language": "English",
    "output_language": "German",
    "input": "I'm John, nice and tall"
    })

print(output)

