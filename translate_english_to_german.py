import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser


# Load environment variables from .env file
load_dotenv()

# Now access the environment variable after loading it
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment variables or .env file")

# Set the environment variable in the system
os.environ["GROQ_API_KEY"] = api_key

# Preload some messages to set the context for the model
# This is a simple example of how to use the ChatGroq model for translation
messages = [
    SystemMessage(content="Translate the following from English into German"),
    HumanMessage(content="I'm John, nice and tall"),
]

# Create a ChatGroq model instance with the specified model and temperature
# The temperature parameter controls the randomness(creativity) of the output
llm = ChatGroq(model="llama-3.1-8b-instant",
                   temperature=0.1)

# Output parser to extract the string from the model's response
# This is necessary because the model's output is wrapped in a specific format
output_parser = StrOutputParser()

# The chain will first call the model and then parse the output using the parser
chain = llm | output_parser

# The invoke method will process the messages and return the translated text
# The output will be a string containing the translation
output = chain.invoke(messages)

print(output)