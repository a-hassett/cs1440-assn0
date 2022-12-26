# CS 1440 Assignment 0 Hints
*   [Erik's Hints](#eriks-hints)
*   [Students' advice from last semester](#students-advice-from-last-semester)

## Erik's Hints

0. Familiarize yourself with the `demo/duckieEncrypter.py` file to assist you in understanding DuckieCrypt. When invoking the file, add the optional argument `-h` or `--help` for a detailed usage message.
1. ASCII characters were of significant importance in the creation of DuckieCrypt. In fact, the mapping of the integer portions of the character codes follow similar patterns as the mapping of ASCII characters. While trying to create the DuckieDecrypter and learning how to handle DuckieCrypt, keep your ASCII character table handy!
2. An average implementation of the DuckieDecrypter can be done in a relatively short amount of code (100-200 lines, or less). Don't over think the assignment and write redundant code that can be accomplished by Python's built in tools. "Why write many w
3. Familiarize yourself with these key functions, which are integral to completing the DuckieDecrypter, as well as completion of the learning exercises associated with this assignment.
    * `chr()`
    * `ord()`
    * `int()`
    * `len()`
    * `open()`
    * `close()`
    * `os.R_OK`
    * `os.access()`
    * `print()`
    * `str.split()`
    * `str.isdigit()`
    * and many more!
4.  Run `help([function_name])` in the REPL to learn more about the functions you will use:
    ```
    $ python -i
    >>> help(print)
    Help on built-in function print in module builtins:

    print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    ...

    >>> help(str.split)

    Help on method_descriptor:
    split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    ...
    ```
5. After you develop the logic looks at the flags to  determine the type of each DuckieCrypt character, how much different will it be to recognize the special characters group?
6. Be sure to test the DuckieDecrypter against invalid characters!  Run your program with the files `data/test/invalid0.txt`, `data/test/invalid1.txt`, and `data/test/invalid2.txt`. 


## Students' advice from last semester

*   Do the lessons, read the encrypter program, write your plan, then write the decrypter in that order
*   Look at the discord, other students have also probably faced the same problems.
*   Don’t procrastinate 
*   start sooner, use your resources.
*   Do all the lessons soon so you can start the project early and have time to reflect on how they relate. 
*   Write the plan. It may seem like extra work, but it does help make life a lot easier.
*   Do all examples in Lsn. They were very helpful.
*   Plan everything before hand. It's way easier to come up with ideas and think things through without having to worry about syntax.
*   Just follow the directions Professor Falor gives in the assignment, lectures, and notes, and everything will go smoothly.
*   Definitely use the interactive REPL to debug and ensure that your variables and functions are doing what they are supposed to be doing
*   Study more python, this course uses more than advertised.
*   Really understand how files work in python. Understand how to manipulate them in the way that you need to.
*   I would advice students to plan well for their assignments to make well organized code.
*   Read all of the documentation and play around in the REPL.  Make sure your program can handle all of the test files in Data
*   Do the lessons, perform tests on your code, never procrastinate.
*   Write the plan before you start.
*   Get a good plan started, spread your work out throughout the week/weeks you have. If you want the program to run/be tested easily, write out your plan in detail. The pseudocode part of the design is key, it sets out your thought process for the program. The implementation is almost automatic. 
*   Give yourself enough time to do the homework and sleep.
*   Start early and try and do things in a consecutive manner. Don't take long breaks.
*   Make sure you understand how you want the functions you design to work together before you define them.
*   Spend a lot of time trying to understand and plan out your program before you write a single line of code
*   Start early and pace yourselves
*   Understand Git, like asap, ask questions as soon as humanly possible about git.
*   Take an hour a day to just look at the code. Even if you aren't writing the code, just thinking about it and looking at it can make a difference. Also, work on the lessons before you work on the assignment. They both take up quite a bit of time and can make it hard to work on it in a single day. 
*   start early
*   Pay attention when learning about the software development plan
*   start on the assignment early
*   Start early, use discord & piazza to get help
*   Don't procrastinate! There will be set backs and tests that your code will fail that you didn't initially anticipate.
*   SDP and no procrastination = success
*   Make sure and do all of the tests with your code!
*   Use the full time to work on the assignment, even if it's only a few minutes each day. Also UTILIZE the coaching lab.
*   Start early and ask for help. 
*   Start early, debug often, run tests several times, plan first.
*   Even if you're tryna procrastinate like me and do it all in one day, at least read all of the instructions and complete all of the lessons the day before you attempt to crunch it. There's a lot.
*   Don't put working on the assignment off. If you have a good plan written somewhere, try to follow the plan instructions, but don't let that completely stop you in your progress. 
*   Give yourself ample time to sit with the problem, and be sure to understand and complete the Plan before writing any code.
*   the earlier you start the better.
*   Make sure to spread the assignment over more days so that you aren't as stressed. 
*   Work on it little by little over the span of many days. Spend more time on the plan than on the programming.
*   Make good plans
*   Just do a little each day so that it won't be a daunting task.
*   Make sure to read all provides materials for the assignments. README.md files, instructions, guides, rubrics, etc. all of the provided materials can help you and there is no reason not to utilize them. 
*   Be familiar with git and commits.
*   Take the time to do the lessons, it seems like a lot of work but if you spread it out it's not too bad and it makes the assignment a lot easier. A lot of the lesson stuff is pretty much exactly what you need to finish the assignment.
*   Read thoroughly through the README files as well as the instructions, and look at the design for the code 
*   At least familiarize yourself with the assignment as soon as you can, even if you don't start the plan or coding at all. 
*   Don't procrastinate it, not even with other assignments. Be on top of things, get started on Monday, be working on the DuckieDecrypter by Wednesday or Thursday.  Read through all the provided information on it, but don't worry if you don't understand it right away. It'll make more sense as you start working on the actual assignment.
*   SDP is important and inessential for Software documentation. I recommend to do more SDP  documentation.
*   I would say that they definitely should plan their first couple hours to get familiar with the assignment and where everything is located. Then I would say complete the lessons as fast as they can and then regroup again and write the software development plan for the actual assignment.  
*   Start right away it takes awhile to get it done.
*   Force yourself the week before the due date to get everything with the assignment (starter code) set up on your computer so you know everything is working properly). Also do the plan and read through all the files. I would also suggest to use paper and pencil (or whiteboard)--just something that is NOT the keyboard--to help in planning. For me, the process of using a medium besides a computer and keyboard helps me think through the problem easier. 
*   To start AND finish early, especially if it’s easy for them. No use waiting till the last second when you don’t need to. 
*   Start early, especially on the actual assignment.
*   Write as detailed of a plan as you can. Spend at least twice as long writing your plan as you do actually coding the assignment.
*   do the plan
*   Start on the lessons early!
*   Start early, follow the instructions, make sure to read the whole project description 
*   Make sure to have a good plan.
*   Do a lesson a day and make sure the files are updated frequently.
*   Spread it out across multiple days, and take your time to really experiment and learn from the lessons.
*   Make connections with your classmates and reach out to them for help. Start the assignment well in advance and do a little bit each day.
*   Read and think about what the assignment is asking for.
*   Read instructions carefully and look at the starter code before writing the plan
*   Make a good plan and stick to it
*   Plan on spending an inordinately long time on the SDP. And try to do it before you do the code.
*   Don't underestimate the assignment :). Even if you think you can hammer it out pretty quickly, give yourself as much extra time as possible.
*   Start sooner rather than later. 
*   Just get started on it early and work on it bit by bit.
*   Read the function templates first in the duckieDecrypter.py
*   Please start early. This is the kind of assignment that you can easily spend 10 hours on because of all the reading and lessons. Not to mention the assignment itself plus all the debugging that will need to be done.
*   Make a new project from scratch and test each function from the starter code in it, or if possible, your entire project.
*   Start really early on the assignments. Find new ways to practice git. Make friends to ask for help 
*   Make sure to understand the lessons before doing the assignment.
*   Start early and push yourself from the beginning.  If you need help, the tutoring center is amazing.  They are seriously so helpful.   Also the exercises are there to help.  I went through them first, before beginning the Duckie Decrypter, as per the assignment instructions and I am so grateful that I did.  It made writing the code so much easier. 
*   The lessons really aren't a large portion of the assignment, so make sure you get those done and can move on to the actual code and SDP as quickly as possible. And look up the example SDP in the lecture notes repository when you're writing your SDP - it doesn't quite line up with the outline of the SDP for this assignment, but it does make it a little clearer what most of the sections are asking for.
*   1. Do not procrastinate  2. If you aren't working on it right now, repeat step 1 as necessary
*   Start early, and find someone to talk to about your plan and high level concepts. It helps to talk things out to figure it out. 
*   Start early and thoroughly read all the documentation, it will make life much easier. Piazza was also very helpful and allowed me to get help quick and easily.
*   Start early
*   Use the plan, don't ignore it.
*   Work through the lessons, after reading the documentation.  Try to work on the SDP before starting to code the main program.
*   Start early, and actually do the SDP
*   Start the problem with dealing with invalid characters in mind. 
*   Start early but not before the assignment is given. Do thorough before turning it in testing. Don't over think it, it is a lot simpler than you might think.
*   start early and really try on your psuedocode
*   .split() does not like null returns, and a simple "" will save you a lot of hassle. Adding a lot of extra print statements while bug testing really helped me follow the data through the program, and also allowed me to see where it was being manipulated differently than I intended in my pseudocode. This may be obvious but a lot of the assignment can just be lifted from the lessons that you did before starting the decrypter. Also if you've taken 1400 and have some of your old homework, a brief look through of your old python code might be a good refresher on python syntax.
*   Start it early.
*   Start early. Plan well. And get done with plenty of time to spare so that you can run all the test cases and have time to tackle unforeseen bugs
*   If you spend the suggested time on the plan all you will have to do is copy, paste and fix a couple bugs.
*   Pick a solution and stick with it, this code doesn't have to be super optimal. 
*   Read all instructions thoroughly
*   Read how it expects the output for the lessons, it takes way to long to try and guess
*   start early
*   Look at the data type and know exactly what you're passing to each of your functions to make sure you get the correct output, and that your program will know what to do with those data types.
*   Do it.
*   Make sure to complete all the lessons before working on the decrypter
*   Follow the instructions.  Reading through the assignment description and then doing the lessons in order made the actual programming very manageable.
*   Take the lessons seriously and think through each one. If you genuinely get stuck ask for help. If you don't understand the instructions ask for help. The lessons prepare you well for the assignment. It's worth taking a while to really understand them in order to save time on the duckieDecrypter assignment.
*   Take some notes on the lessons, particularly when it comes to using files. It gets troublesome needing constantly navigate back and forth constantly.  Along with that, use physical paper to help plan. Physical paper is still produced for a reason.
*   Look at the starter code before doing the plan
*   Make sure to look at the assignment description very carefully and seek advice from classmates if you have trouble.
*   Read EVERYTHING before making a plan. Would have saved me some hassle. even though you already said to read everything, lol.
*   Start early
*   just run through the lessons and start your plan
*   Take your time to absorb the material because it is there to help you understand BASH.

Of the hints shared above, 26/100 of them suggest either "start early" or "don't procrastinate." Seems like there's a common thread in the advice from our previous interns...
