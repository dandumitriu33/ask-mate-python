# Codecool Educational Project - ASK MATE
Web and SQL with Python / 1st TW week / Ask Mate project
## Description
Small web project with a question and answer format. It is essentially an
 extremely simple Stack Overflow clone.  
## Main features:
- post questions, with question, detailed description and picture upload
- post answers to existing questions, with detailed descriptions and picture upload
- edit and delete both questions and answers
- sort the questions on the main page, ascending and descending, by date posted,
number of views, number of votes, question alphabetically and details alphabetically
- upvote or downvote questions and answers
## Installation
This installation guide is made for the Ubuntu operating system. Other operating 
systems have similar steps but please check the details on the web first.
1. Clone the project on your computer
        sudo apt-get update
        sudo apt-get install git
        git --version
        *navigate to the destination folder on your machine
        git clone https://github.com/dandumitriu33/ask-mate-python.git
2. Make sure you have pip3 installed for python
        pip3 --version
3. Install and activate the virtual environment in the git project folder (not 
where you ran git clone)
        pip3 install virtualenv
        virtualenv venv
        source venv/bin/activate
4. Run the project on the given 0.0.0.0:5000 address
        python3 server.py
Note: You might be able to access the site from other devices on the same network. 
If you aren't able to, check your local network or server computer firewall and 
other security settings and run the server accordingly. 
## How to use
Pretty intuitive UI, just like any other question/answer forum/board.
