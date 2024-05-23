README for Ranger's GPT-4 CLI Tool

Introduction
This project contains a command-line interface (CLI) tool to interact with OpenAI's GPT-3 and GPT-4 models. It allows users to send queries to the model and receive responses, all from the convenience of the command line. The tool also logs these interactions to a text file.

Prerequisites
Before you can use this tool, you need to install Python and Anaconda, as well as set up a few files.

Installing Python
Download Python:
Visit the official Python website (python.org) and download the latest version of Python.
Install Python:
Run the installer and follow the instructions. Ensure you check the box that says "Add Python to PATH" during installation.
Installing Anaconda
Download Anaconda:
Visit the Anaconda website (anaconda.com) and download the Anaconda installer for Python.
Install Anaconda:
Run the Anaconda installer and follow the on-screen instructions.
Setting Up the Project
Clone the Repository:

Clone this repository to your local machine or download the files directly.
Setting Up the Environment:

Open Anaconda Prompt and navigate to the project directory.
Create a new Conda environment with the required dependencies (if any).
Activate the new environment.
OpenAI API Key:

You need an API key from OpenAI to use their models. Sign up at OpenAI and access your API key.
Environment Variable for API Key:

Set up an environment variable named OPENAI_API_KEY with your OpenAI API key.
Prepare the Script Files:

README.txt
This document will guide you through the installation process for this script. Please follow the instructions carefully.

Prerequisites
Python: Our script is written in Python. So, first we need to install Python on your system.
Anaconda: Anaconda is a distribution of Python that comes with many useful packages pre-installed. We'll use it in this project.
.bat file: This is a batch file which is used to execute commands with a single click.
Installation
Install Python
If you haven't installed Python on your computer, please follow the instructions based on your OS:

For Windows users: Download the installer and run it.
For MacOS users: It's recommended to use Homebrew. If you have Homebrew, you can install Python by running brew install python in the terminal.
Install Anaconda
You can download Anaconda from here:Anaconda downloads page

Select the appropriate version for your OS and follow the on-screen instructions.

Creating a .bat file
To create a .bat file:

Open Notepad.
Write your desired commands.
Save the file with .bat extension (filename.bat).
For example, if your python script is located at C:\Users\Username\MyScript.py, you would write the following command in the .bat file:

python C:\Users\Username\MyScript.py
Then save the file as ScriptRunner.bat.

Add the .bat file into a folder
You can add the .bat file in any folder you like. But it is recommended to keep the file in the same folder as your Python script for ease of use.

Running the project
Once you've set up everything, you can run the .bat file with a double-click to execute your script.

PATH Environment Variable
If the python command is not recognized, you need to add Python to your PATH environment variable. In the Anaconda installer, there's an option which allows you to do this automatically.

Documentation
For more detailed information about this project and how it functions, please refer to the DOCUMENTATION.txt in the root directory of this project.

Ensure rgpt.py, rgpt.bat, and rgpt.txt are in the directory C:\Users\david\OneDrive\Documents\WindowsPowerShell\Scripts.
Add Script Directory to PATH:

Add C:\Users\david\OneDrive\Documents\WindowsPowerShell\Scripts to your system's PATH variable.

Creating the Batch File
Navigate to the Script Directory:

Go to C:\Users\david\OneDrive\Documents\WindowsPowerShell\Scripts.

Create rgpt.bat:
Open a text editor and create a new file.

Write the following lines in the file:

python rgpt.py %*

Save the file as rgpt.bat in the same directory as rgpt.py.

Usage

To use the CLI tool, open Command Prompt or PowerShell and type rgpt 'your query'.
For example: rgpt 'capital of France'.

The responses will be displayed in the command line and logged to rgpt.txt.
Documentation

The script can be used to interact with different versions of OpenAI's models by specifying the model version in the command.
