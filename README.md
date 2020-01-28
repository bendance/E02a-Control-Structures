
# E02a-Control-Structures

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
    
 

