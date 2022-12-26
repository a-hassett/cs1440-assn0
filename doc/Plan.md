# Software Development Plan

## Phase 0: Requirements Specification *(10%)*

**Deliver:**

* A detailed written description of the problem this program aims to solve.
* Describe what a *good* solution looks like.
    * List what you already know how to do.
    * Point out any challenges that you can foresee.

In this program, I will be decoding an encrypted message from
"Duckiecrypt" to regular ASCII characters so that it's readable to humans.
The original encrypted text will be in separate files, so I have to open
the files in the program that the user chose and then analyze the 
Duckiecrypt characters and find the corresponding ASCII characters. 

A good solution to this problem would be one with minimal bugs, so invalid
inputted file names would not crash the program. It will also have good
formatting. To me, this means no extra lines but still plenty of white space
so it continues to be readable. I also want the code to be written as
efficiently as possible with descriptive variable names and comments.

In the lessons for this assignment, I learned how to read in text files
to a program with the os library. I know how to translate between two linked
lists using their indices. I think that'll be the best way to switch back
and forth between Duckiecrypt and ASCII. I also learned how to split the words
in a string into an array. This will help me break up the Duckiecrypt symbols
so I can analyze them one at a time.

Though I have learned how to open and close outside files, it will still
take me a while to figure out how to format it well, because I did struggle
with that in Lesson 2. I think my strategy will be using linked lists, but
I want to find a faster way to get to the uppercase and lowercase alphabetic
letters, because they're so similar.
* Is the purpose of the convertUpper and convertLower to help form a sentence
with the right punctuation? 
* I'll use the convertUpper and convertLower when the flag is ^ or _
* I'll use the convert to specialChar when the flag is +
* I ended up changing my mind about the linked list. See my new plan in Phase 1.
---

## Phase 1: System Analysis *(10%)*

**Deliver:**

* List all of the data that is used by the program, making note of where it comes from.
* Explain what form the output will take.
* Describe what algorithms and formulae will be used (but don't write them yet).

The getFile function uses os.getcwd to tell the reader what working directory
they are in. Then it takes input from the user to choose what file we will be
reading. If the path is valid, it returns an open file to "file" in the __name__ 
function. Once we've established that it's an open file, we can use the readLine
part of the library to read each line at a time. This will return a string that
you can put in the decryptLine function. In this function, you'll want to use 
the string.split function to make the words on the line an array of strings. 
Then we can use a for loop to read the first character in each string in the array
which will be the flag. Once we've identified which of the three flags the
Duckiecrypt character has, we will send the string to be decoded in one of three
functions: convertToUpper, convertToLower, or convertToSpecialChar. Since all
of the characters are in the same order as the ASCII characters in their respective
groups, I can easily convert from the number part of the Duckiecrypt character to
regular characters. That means I have to identify what group the special characters
are from (A, B, or C) before converting to letters. The "convertTo..." functions
will all return a string to the decryptCharacter function which will return a 
string to the decryptLine function. That function will take the decrypted character
from decryptLine and add it to a new string that contains the decrypted line. This
function will return a string to __name__ where it gets printed to the console.
Then I'll close the file and exit. I also need to add somewhere that checks if
the inputted file exists. I think I'll add it to the getFile function and only
return a file if it exists. If it doesn't I'll use the sendError function and
exit the program. I also need to make sure that invalid characters don't crash
the program. With the logic I've set up, invalid Duckiecrypt characters will
still produce a valid keyboard character, but it may be an "imaginary" one.


## Phase 2: Design *(30%)*

**Deliver:**

* Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
* Pseudocode that captures how each function works.
    * Explain what happens in the face of good and bad input.
    * Write a few specific examples that occurred to you.

In the below examples, I print <invalid> and return an empty string if there is a "bad" Duckiecrypt character.
A bad one is one that doesn't translate to one of the given characters. A "bad" file
just terminates the whole program. 

Examples of how the code should handle bad Duckiecrypt characters if it works right:
* "$24" prints "<invalid flag>"
* "+A88" prints "<invalid numeric character code for Special>"
* "+C2" prints "<invalid character code for Special>"

Practice pseudocode:

```python
#getFile asks for a file from the user and provides it to the main function
def getFile():
    print("location: {os.cwd}")  #let the user know what working directory they're in
    filePath = input("Please enter a path: ")  #take user input to get a file
    if os.access(filePath, os.F_OK):  #if the file is good
        file = open(filePath)
        return file  #returns an open file
    else:  #if the file is bad, we don't want to crash the program
        sendError()  #terminates the program and sends an error message
```
```python
#if the file is bad, sendError runs. sends an error message and exits the program
def sendError(msg=None):
    print("The entered file is not valid")
    return exit(0)
```
```python
#decryptLine breaks down a line of text into an array of Duckie characters,
#translates the characters, then builds a string of translated characters
def decryptLine(line):
    charsInLine = line.split()  #break the line into an array
    decryptedLine = ""  #this will be the translated string of characters
    for i in len(charsInLine):  #for every Duckie character in the line we're looking at
        decryptedLine += decryptChar(charsInLine[i])  #decrypt it and add it to the final string
    return decryptedLine  #returns string of translated characters
```
```python
#decryptChar pushes Duckie characters into categories based on their flag symbol
#and returns them after decrypted
def decryptChar(character):
    if character[0] == "^":  #flag identifying uppercase letters
        return convertToUpper(character[1:])  #return string of uppercase letter
    elif character[0] == "_":  #flag identifying lowercase letters
        return convertToLower(character[1:])  #return string of lowercase letter
    elif character[0] == "+":  #flag identifying special characters
        return convertToSpecialChar(charater[1:]) #return string of special character
    else:  #if the flag is not one of the three
        print("<invalid flag>")  #print an error message
        return ""  #return an empty string instead of decrypted character
```
```python
#if the flag identifies the character as uppercase, we will use the ASCII chart
#shift the character's number value to fit the ASCII chart
#and check if it's a valid character to be decrypted
def convertToUpper(charCode):  #we use the character_code of the DuckieCrypt
    if charCode.isnumeric():  #if the character_code is a number
        if int(-1 < charCode < 26):  #we put this on a separate line to avoid errors
            #we want to translate the character code to an integer so we can use ASCII
            return chr(int(charCode) + 65)  #uppercase A in ASCII is 65
        else:  #if the number is not one of the alphabet
            print("<invalid numeric character code for Upper>")  #print error msg
            return ""  #return an empty string
    else:  #if it's not a number, it doesn't translate out of DuckieCrypt
        print("<invalid character code for Upper>")  #print error msg
        return ""  #return an empty string
```
```python
#if the flag identifies the character as lowercase, we will use the ASCII chart
#shift the character's number value to fit the ASCII chart
#and check if it's a valid character to be decrypted
def convertToLower(charCode):  #we use the character_code of the DuckieCrypt
    if charCode.isnumeric():  #if the character code is a number
        if int(-1 < charCode < 26):  #we put this on a separate line to avoid errors
            #we want to translate the character code to an integer so we can use ASCII
            return chr(int(charCode) + 97)  #lowercase a in ASCII is 97
        else:  #if the number is not in the range of the alphabet
            print("<invalid numeric character code for Lower>")
            return ""  #return an empty string
    else:  #if the character code isn't a number, we can't decode it
        print("<invalid character code for Lower>")
        return ""  #return an empty string
```
```python
def convertToSpecialChar(charCode):  #we use the character_code of the DuckieCrypt
    if charCode[0] == "A":
        #group A
        if charCode[1:].isnumeric():
            if int(-1 < charCode < 33):  #we put this on a separate line to avoid errors
                return chr(int(charCode) + 32)  #"space" in ASCII is 32
            else:  #if the number is out of range, it won't decrypt
                print("<invalid numeric character code for Special>")  #print error msg
                return ""  #return an empty string
        else:  #if the character code isn't a number after the group letter
            print("<invalid character code for Special>")  #print error msg
            return ""  #return an empty string
    elif charCode[0] == "B":
        #group B
        if charCode[1:].isnumeric():
            if int(-1 < charCode < 6):  #we put this on a separate line to avoid errors
                return chr(int(charCode) + 91)  #left bracket in ASCII is 91
            else:  #if the number is out of range, it won't decrypt
                print("<invalid numeric character code for Special>")  #print error msg
                return ""  #return an empty string
        else:  #if the character code isn't a number after the group letter
            print("<invalid character code for Special>")  #print error msg
            return ""  #return an empty string
    elif charCode[0] == "C":
        #group C
        if charCode[1:].isnumeric():
            if int(-1 < charCode < 4):  #we put this on a separate line to avoid errors
                return chr(int(charCode) + 123)  #left curly brace in ASCII is 123
            else:  #if the number is out of range, it won't decrypt
                print("<invalid numeric character code for Special>")  #print error msg
                return ""  #return an empty string
        else:  #if the character code isn't a number after the group letter
            print("<invalid character code for Special>")  #print error msg
            return ""  #return an empty string
    else:  #if the group letter is not A, B, or C
        print("<invalid character code for Special>")  #print error msg
        return ""  #return an empty string
```


## Phase 3: Implementation *(15%)*

**Deliver:**

* (More or less) working Python code.
* Note any relevant and interesting events that happened while you wrote the code.
    * e.g. things you learned, things that didn't go according to plan

My code worked surprisingly well. I just copied and pasted from Phase 2 mostly.
Most of it worked. The only thing I had issues with was forgetting
some formatting changes. I wrote the line "if int(-1 < charCode < 4):" and similar
ones, but they ended up looking like "if -1 < int(charCode[1:]) < 4):" in the
convertToSpecialChar and "if -1 < int(charCode) < 4:" in convertToUpper and
convertToLower. I also got the formatting wrong when I checked the working directory



## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

* A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
* Write your test cases in plain language such that a non-coder could
* run them and replicate your experience.

I ran ../src/duckieDecrypter.py and entered ../data/msg2 as the file. I got an 
error telling me that I couldn't compare a string (charCode) with the integers
-1 and 26. I had to convert charCode to an integer while comparing it to 1 and 26
to fix this. This happened everywhere there was a similarly written line. Then in the 
convertToSpecialChar function, it wouldn't convert the charCode to an integer
because the charCode included a number. To do this, I instead compared the
second and after characters of the char code so that the letter indicating
the group wouldn't be included. 


## Phase 5: Deployment *(5%)*

**Deliver:**

*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Review the project to ensure that all required files are present and in correct locations.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
    *   Run through your test cases to avoid nasty surprises.


## Phase 6: Maintenance

**Deliver:**

* Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    * What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    * Will your documentation make sense to
        *   anybody besides yourself?
        *   yourself in six month's time?
    * How easy will it be to add a new feature to this program in a year?
    * Will your program continue to work after upgrading
        * your computer's hardware?
        * the operating system?
        * to the next version of Python?

* The order of the functions is a bit hard to understand, and it might take a minute to figure out my variable names
  * I'm not really sure how setting a new variable equal to open(file) makes a file variable, but I don't think it would even be considered a file variable.
  * I think I could fix any undiscovered bugs pretty easily. I understand all of my code, because I wrote it in this document before using an IDE.
* Will it make sense:
  * I think the only part that might get a bit confusing to read for other people was my reporting bugs section. There weren't any bugs caused by weird input, just bad syntax, so I didn't have much to share.
  * It'll make sense to me later. All I did was write out my thought process and logic before starting. But I think I'll be annoyed with myself if I look at the pseudocode part, because the comments make it look very messy.
* It will be easy to add a feature to this program, because of the functions. It's all very integratable.
* Will the program work:
  * My program doesn't rely on my computer's hardware much. The file input that it asks for can be written from the base directory C.
  * There might be issues with a Mac because of the types of slashes (forward or back), but the rest is pretty simple.
  * Unless they change the names of features and what library certain features are found in, newer versions of Python should work just fine.
