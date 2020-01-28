
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
This exercise assumes that you have already installed Python, GitHub Desktop, and VS Code, and that you have already created a GitHub account. If that is not the case, please refer to previous exercises.

This repository contains several files that you will need to alter to complete the assignment. Fork this repository (instructions below) and edit the files. Commit and push the changes back to GitHub and turn in the URL to your repository on Canvas.

Comments in Python are marked by a # sign (for single-line comments) or three matching quotation marks (''' or """) if a comment requires more than one line. They should also appear in a different color in VS Code. The Python Interpreter ignores comments, so you can safely include any information you want there.

*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
    I expect this file to print out “Greetings” and proceed to ask me their favorite color.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    Upon running the Python file, the terminal prints out “Greetings” and asks me their favorite color.
  - What do you think the program did with what you typed in answer to the question?
    The program didn’t do anything with what I typed in the terminal. This set of code isn’t set up to be receptive to responses.
- Open main02.py. Before running it, describe how this is different than main01.py.
    This program will also print out “Greetings” and proceed to ask me their favorite color. It’s different from main01 because, based       on my input, the program will print out what I have typed in.
  - What do you think the color = input() will do? 
    The color=input() function will use my input as a variable. This variable will then be printed back to me once I run the program.
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    The program did as expected and printed my color variable back to me.
- Open main03.py. Before running it, describe how this is different than main02.py.
    This program is different from main02 because there is an “if/else” function included within the file.
  - What is happening on lines 9–12?
    On these lines, an “if/else” function has been written. This function states that if the user guesses red, the statement “Correct!”     is printed out. Otherwise, the program prints out “Sorry, try again.”
  - Why are lines 10 and 12 indented?
    Because both of the "print" functions are children of the "if/else" function.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
    If I don’t capitalize “Red,” then the program registers my input as a false answer.
  - What does this tell you about "color"?
    This tells me that “color” is a variable that is sensitive to capitalization.
- Open main04.py. Before running it, describe how this is different than main03.py.
    This program is different from main03 because it allows both “Red” and “red” to be correct.
  - What problem is this trying to solve?
    This allows “red” to be recognized as another correct answer.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    If you use some other capitalization, the program still recognizes it as a wrong answer.
- Open main05.py. What do you expect line 9 to do?
    I expect line 9 to interpret the user’s input as lowercase and then make “red” the correct answer.
  - What problem is it trying to solve?
    This added line attempts to solve the capitalization issue with “Red.” 
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    If you add spaces before or after the word “Red,” then the program interprets this as an incorrect answer.
 - Open main06.py. How is line 9 different than in main05.py?
     There is a .strip() function added to the line.
   - What would you guess .strip() is doing?
     The .strip() function removes the whitespace from a user’s input. 
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
     If you put spaces between each letter of the word, then the program will still recognize it as an incorrect answer.
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
     I expect this program to be different since it recognizes pink as a color that’s “close.”
   - What is happening on line 12?
     On line 12, an elif function has been written that states if the user enters “pink” then the program will print out the statement        “Close!”
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
     On line 9, the program states that while color is not equal to red, this program will run. This allows the function to be ran            repeatedly. 
   - Why are lines 10–17 indented?
     Lines 10-17 are indented because they function as conditions for what will happen when the while() function runs.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
     I’m guess if you moved line 10 before line 9, whatever the player entered would become the color variable.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
     After doing this, the program repeats the else function indefinitely.
 - Open main09.py. What is happening on line 13?
     On line 13, one count is added every time the user makes an input.
   - What is the purpose of “count”?
     The purpose of count is to show how many times the player guessed a color before getting it correct.
   - What is happening on line 22?
     On line 21, the program prints out how many guesses the player made before getting the answer correct.
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it is doing (a comment follows a pound sign [#]).
     I have made commentary on every line in the code. Please check the file for details.
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
     In lines 6-11, the game is making it so that the last chosen color is not picked as a random color again.
Commit your changes and push them back to the repository.
 

---

Instructions for forking this repository:
 
Log into your account on [github.com](https://github.com)

Go to the [exercise template page](https://github.com/BL-MSCH-C220-S20/E02a-Control-Structures) on GitHub

There is a button in the top right corner of the page labeled "Fork". Press that now

This will create an independent copy of this repository in your account that you can control and edit

Go to your GitHub home page, and select the new E02a-Control-Structures repository

On that page, you will see a green button labeled "Clone or download". Press that now. You will see a drop down box. Press the "Open in Desktop" button.

This should launch GitHub Desktop. It will ask you for a location (on your computer) where the repository may be cloned (downloaded). Choose a location that will be easy for you to find, and press the blue "Clone" button.

Once GitHub Desktop has cloned (downloaded) the code, it will be responsible for keeping the code on your local computer synchronized with the repository in your GitHub account. Now, open Visual Studio Code, and choose File->Open. Find the folder of the cloned repository and select Open.

In the left (File Explorer) panel, you should see a list of files that comprise this repository

First, edit the file called LICENSE. Replace year and name with the current year and your name. Save this file

Then open README.md. Feel free to remove any extraneous information, and then answer the questions posed in the file. You can add your answers after each question

When the time comes for you to run any of the python files, you can do so by clicking the green arrow in the top right corner of the window or by right-clicking on the code and selecting "Run Python File in Terminal". The results will appear at the bottom. If you don't see "Run Python File in Terminal" in the contextual menu, that is because VS Code doesn't have the Python extension installed. You can do that here: [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

When you are done editing the files, return to GitHub Desktop. In the left panel, you should see a list of the files that have changed

At the bottom of the leftmost area, you should see a text box labeled "Summary (required)". Add a message that describes what you have done; these messages are typically stated in the active-present tense. For example, "Updates the LICENSE, README.md, and completes the assignment." Push the blue "Commit to master" button

In the top bar of the window, you should see a button that is labeled "Push origin", push that now

Check out your page on GitHub. You should see the changes you made reflected there, Repeat steps 10 through 16 as necessary

When you are satisfied with your efforts, turn in a URL to your repository on Canvas

---
If you try to push your changes, and you receive a permission error, it is likely that you are trying to edit the BL-MSCH-C220-S20 copy of the repository rather than your own. Make sure you don't skip the step of forking your own copy and cloning that.

---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
