#!/usr/bin/env python3
# RangerChat-GPT4 script by Ranger (rgpt4)

# This script is for Github.

# Created 16-01-2024
# Updated 18-05-2024
# New Version 2. 22-05-2024

# Version 2

# About:
# The rangerchat script will save all questions and answers into the text file called rgpt4.txt, if it is not there, the script will create one for you.
# This script enables you to chat with GPT-4 on the command line.
# It takes a query and sends it to the OpenAI Chat API.
# The response is then printed to the console and appended to a text file.
# This will add your question and answer to a rgpt4.txt file in the same directory as the script.
# You will need to add your own API key in the .env file. (https://platform.openai.com/api-keys)

# Instructions:

# Make sure to have the .env file with the OPENAI_API_KEY set. (https://platform.openai.com/api-keys)
# Install the required modules $ pip install -r requirements.txt 
# Run the script using the command: python rgpt4.py "query" : Replace "query" with your question or prompt
# Example: python rgpt4.py "What is the capital of Ireland?"
# Note: You can also run the script without the query and it will prompt you to enter one.

# Macbook and Linux users: 
# To make it easier to run, you can create an alias in your shell profile
# Make an Alias in the .bashrc or .zshrc file
#   alias rgpt='cd /Volumes/Personal/Programming/Projects_Mac/git_projects/chatgpt/rgpt/rgpt-github/rgpt && python rgpt4.py'
#   Usage:   $ rgpt "query"
#   Example: $ rgpt "What is the capital of Ireland"

# Modules to import
import os
import sys
from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# OpenAi_API_Key
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Set up the OpenAI API client
print()
print("\033[93mWelcome to RangerChat 💀 \033[0m")
print()
print()
print("\033[93mPlease wait for your answer 💀 \033[0m")

def openai_create(prompt):
    model_id = 'gpt-4o'
    response = client.chat.completions.create(engine=model_id,
    prompt=prompt,
    temperature=0.9,
    max_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.1,
    stop=[" Human:", " AI:"])

    return response.choices[0].text

def chat_gpt4(query):
    model_id = 'gpt-4o'
    conversations = [{'role': 'system', 'content': 'How may I help you?'}]

    with open('rgpt4.txt', 'a', encoding='utf-8') as file:
        file.write("=== GPT-4 Chat started at {} ===\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

        prompt = query
        conversations.append({'role': 'user', 'content': prompt})
        response = client.chat.completions.create(model=model_id,
        messages=conversations)
        response_content = response.choices[0].message.content.strip()
        conversations.append({
            'role': response.choices[0].message.role, 
            'content': response_content
        })

        print(f'\n{response.choices[0].message.role}: {response_content}\n')

        file.write("[{}] User: {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), prompt))
        file.write("[{}] 🤖 {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), response_content))

        file.write("=== GPT-4 Chat ended at {} ===".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))+ "\n\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: rgpt4 <query>")
        sys.exit(1)

    query = ' '.join(sys.argv[1:])
    chat_gpt4(query)

# Check if the user wants to ask another question
while True:
    another_question = input("Do you want to ask another question? (yes/no): ")
    if another_question.lower() in ["yes", "y"]:
        query = input("Enter your question: ")
        chat_gpt4(query)
    elif another_question.lower() in ["no", "n"]:
        print("\033[93mThank you for using RangerChat 💀 \033[0m")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
