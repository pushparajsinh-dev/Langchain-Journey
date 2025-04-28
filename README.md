# Langchain 

This project includes my joruney in learning with Langchain, will provide updates periodically.

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

## Installation

To get started, you need to follow these few simple steps:

1. **Clone this repository**:

    Open terminal and type:
    ```bash
    git clone https://github.com/pushparajsinh-dev/LangChain.git
    ```

2. **Create a virtual environment**(Optional but recommended for best coding practice):
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

To able to run this code, create a `.env` file to store your API in the root directory. This is necessary to run LLM models.

Create a `.env` file and add the following line:

```plaintext
GROQ_API_KEY='your_groq_api_key'
```
Replace 'your_groq_api_key' with your Groq API key.

Note:If you're using a different LLM, refer to the Langchain documentation and adjust the code as needed.

## Usage

You can the individual files with the following command:
```bash
python [file_name.py]
```



A Special thanks to dev-arctik for their guidance and help in making this journey easy!