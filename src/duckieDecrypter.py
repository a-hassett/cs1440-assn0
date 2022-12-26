#!/usr/bin/env python
#                         ~
#                        (o)<  DuckieCorp Software License
#                   .____//
#                    \ <' )   Copyright (c) 2022 Erik Falor
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
# Permission is NOT granted, to any person who is NEITHER an employee NOR
# customer of DuckieCorp, to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

# Feel free to start from scratch, or repurpouse any of these suggested functions! The world is yours. 
#   Well, maybe that was a bit of an over exaggeration. The world isn't only *yours*, but this text file sure is. 


# Ally Hassett -- A02365310 -- CS 1440

import os


# sends an error message and exits the program
def sendError(msg=None):
    print("<The entered file is invalid>", end="")
    return exit(0)


# checks if Duckie terms starting with the "_" flag are valid. decrypts them if yes, prints an error message if no
def convertToLower(charCode):
    if charCode.isnumeric():
        if -1 < int(charCode) < 26:
            return chr(int(charCode) + 97)  # ASCII code for "a" is 97
        else:
            print("<invalid character code>", end="")
            return ""
    else:
        print("<invalid character code>", end="")
        return ""


# checks if Duckie terms starting with the "^" flag are valid. decrypts them if yes, prints an error message if no
def convertToUpper(charCode):
    if charCode.isnumeric():
        if -1 < int(charCode) < 26:
            return chr(int(charCode) + 65)  # ASCII code for "A" is 65
        else:
            print("<invalid character code>", end="")
            return ""
    else:
        print("<invalid character code>", end="")
        return ""


# checks if Duckie terms starting with the "+" flag are valid. decrypts them if yes, prints an error message if no
def convertToSpecialChar(charCode):
    if charCode[0] == "A":
        # group A
        if charCode[1:].isnumeric():
            if -1 < int(charCode[1:]) < 33:
                return chr(int(charCode[1:]) + 32)  # ASCII code for " " is 65
            else:
                print("<invalid character code>", end="")
                return ""
        else:
            print("<invalid character code>", end="")
            return ""
    elif charCode[0] == "B":
        # group B
        if charCode[1:].isnumeric():
            if -1 < int(charCode[1:]) < 6:
                return chr(int(charCode[1:]) + 91)  # ASCII code for "[" is 65
            else:
                print("<invalid character code>", end="")
                return ""
        else:
            print("<invalid character code>", end="")
            return ""
    elif charCode[0] == "C":
        # group C
        if charCode[1:].isnumeric():
            if -1 < int(charCode[1:]) < 4:
                return chr(int(charCode[1:]) + 123)  # ASCII code for "{" is 65
            else:
                print("<invalid character code>", end="")
                return ""
        else:
            print("<invalid character code>", end="")
            return ""
    else:
        print("<invalid character code>", end="")
        return ""


# open the file if it exists and send an error if it doesn't
def getFile():
    print(f"You are located at {os.getcwd()}")
    filePath = input("Please select a text file to parse: ")
    if os.access(filePath, os.F_OK):  # checks if the file exists
        file = open(filePath)
        return file
    else:
        sendError()


# reads the flags of Duckie terms to determine which group to send them to
def decryptCharacter(character):
    if character[0] == "^":
        return convertToUpper(character[1:])
    elif character[0] == "_":
        return convertToLower(character[1:])
    elif character[0] == "+":
        return convertToSpecialChar(character[1:])
    else:
        print("<invalid flag>", end="")
        return ""


# breaks a file line into an array that can be decrypted more easily
def decryptLine(line):
    duckieTermsInLine = line.split()
    decryptedLine = ""  # final string that will be produced
    for i in range(len(duckieTermsInLine)):
        decryptedLine += decryptCharacter(duckieTermsInLine[i])
    return decryptedLine


if __name__ == '__main__':
    file = getFile()
    for line in file.readlines():
        print(decryptLine(line))
    file.close()
