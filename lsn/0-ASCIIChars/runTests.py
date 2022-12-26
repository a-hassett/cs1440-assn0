import sys
import unittest

import tests

class TermColor:
    BOLDRED = '\033[1;31m'
    BOLDGRN = '\033[1;32m'
    BOLDYLW = '\033[1;33m'
    BOLDCYAN = '\033[1;36m'
    ENDC = '\033[0m'
    WHITE = '\033[1;37m'
    YLW = '\033[33m'
    UNDERLINE = '\033[4m'

class TestContainer:
    def __init__(self, testClass, argName, title, desc="", silenced=False):
        '''
        testClass: Class -- Reference to TestCase Class to build the tests from
            OR  testClass may be a list of classes instead, if you want to group
                multiple TestCase objects together
        argName: String -- Name to be supplied to sys.argv
        title: String -- Title of the test
        desc: String -- Description of the TestCase class to be run
        silenced: Boolean -- If silenced is set to true, pre/post processes are
            skipped
        '''
        self.testClass = testClass
        self.argName = argName
        self.title = title
        self.desc = desc
        self.suite = None
        self.result = None
        self.pre = None
        self.post = None
        self.silenced = silenced

    def makeSuite(self):
        if self.suite:
            return self.suite

        # if the user provides multiple TestCase classes, place them all into a
        # suite
        elif isinstance(self.testClass, list) or isinstance(self.testClass, tuple):
            self.suite = unittest.TestSuite()
            for cls in self.testClass:
                self.suite.addTest(unittest.makeSuite(cls))
            return self.suite

        self.suite = unittest.makeSuite(self.testClass)
        return self.suite

    def runTest(self):
        '''
        Called to execute the test
        '''

        # Runs pre-test execution functions
        if not self.silenced:
            self.preTestPrint()
            if self.pre:
                for func in self.pre:
                    func()

        if not self.suite:
            self.makeSuite()
        self.runner = unittest.TextTestRunner(verbosity=2, stream=sys.__stdout__, )
        self.result = self.runner.run(self.suite)

        # Runs post-test execution functions
        if not self.silenced:
            self.postTestPrint()
            if self.post:
                for func in self.post:
                    func()

    def preTestPrint(self):
        '''
        Will be used to print something before a test is run
        '''
        print("=" * 70)
        print(f"{TermColor.BOLDYLW + TermColor.UNDERLINE}Tests for {self.title}{TermColor.ENDC}")
        if self.desc:
            print(f"{TermColor.YLW}{self.desc}{TermColor.ENDC}")
        print("=" * 70)

    def postTestPrint(self):
        '''
        Will be used to print something after a test is run
        '''
        print()

    def setPre(self, listOfFunctions):
        '''
        listOfFunctions: List of parameterless function references that are
        called before the test is run
        '''
        if isinstance(listOfFunctions, list):
            self.pre = listOfFunctions

    def setPost(self, listOfFunctions):
        '''
        listOfFunctions: List of parameterless function references that are
        called after the test is run
        '''
        if isinstance(listOfFunctions, list):
            self.post = listOfFunctions


def welcomeMessage(tests):
    msg = f"""\
Welcome to the DuckieCorp's automated testing system! Verify if you have
successfully completed the requested lesson exercises.
{TermColor.WHITE + TermColor.UNDERLINE}
You have requested tests on the following exercises:
{TermColor.ENDC}"""
    msg += TermColor.BOLDCYAN
    for test in tests:
        msg += f"    {test.title}\n"
    msg += TermColor.ENDC
    print(msg, end="")


def runTests(tests):
    welcomeMessage(tests)

    for test in tests:
        test.runTest()

    # Check All Results
    success = True
    for test in tests:
        result = test.result
        if not result.wasSuccessful():
            success = False
            break

    if success:
        print(f"""\
{TermColor.BOLDGRN + TermColor.UNDERLINE}\
SUCCESSFULLY PASSED ALL REQUESTED TESTS\
{TermColor.ENDC}
    Congratulations! Your code passes all of the tests that were ran. This
    likely means you will be receiving a good score when your code goes through
    the code review process.  However, be sure to double check that your work
    meets the requirements, to ensure that DuckieCorp code reviewers won't find
    something that these tests may have missed!{TermColor.ENDC}""")

    else:
        print(f"""\
{TermColor.BOLDRED + TermColor.UNDERLINE}\
DID NOT PASS ALL REQUESTED TESTS\
{TermColor.ENDC}
    One or more of your segments of code did not pass the tests. Check through
    the error logs above for a more detailed diagnosis of the problem. Sorry my
    friend, better luck next time.

    The following tests encountered an error or failed:{TermColor.BOLDRED}""")
        # LOG THE FAILURES/ERRORS TO THE USER:
        for test in tests:
            result = test.result
            if not result.wasSuccessful():
                print("    " * 2 + test.title)
                for err in result.errors:
                    print("    " * 3 + "ERROR: " + str(err[0]))
                for fail in result.failures:
                    print("    " * 3 + "FAILURE: " + str(fail[0]))
        print(TermColor.ENDC, end="")


ALL_TESTS = [
    TestContainer(testClass=tests.testEX0.ExerciseTests,
                  argName="0",
                  title="ASCII Characters Exercise 0",
                  desc="""\
    test_success:
        Verifies the existence and successful completion of the ex0.displayASCII
        function. Ensures the program does not crash upon it being called. It is
        the intern's duty to ensure the output is helpful and informative for
        the user."""),
    TestContainer(testClass=tests.testEX1.ExerciseTests,
                  argName="1",
                  title="ASCII Characters Exercise 1",
                  desc="""\
    test_emptyList:
        Tests that the function returns an empty list if an empty list is given.
    test_validity:
        Tests the validity of the output.
            EX: Ensures listOfChars([65, 66, 67]) == ['A', 'B', 'C']"""),
    # Demonstrate that the TestContainer can take multiple TestCase objects
    TestContainer(testClass=tests.testEX2.ExerciseTests,
                  argName="2",
                  title="ASCII Characters Exercise 2",
                  desc="""\
    test_emptyList:
        Tests that the function returns an empty list if an empty list is given.
    test_validityOfList:
        Tests the validity of the output with a list as input.
            EX: Ensures listOfASCIIInts(['A', 'B', 'C']) == [65, 66, 67]
    test_validityOfString:
        Tests the validity of the output with a string as input.
            EX: Ensures listOfASCIIInts('ABC') == [65, 66, 67]"""),
    TestContainer(testClass=tests.testEX3.ExerciseTests,
                  argName="3",
                  title="ASCII Characters Exercise 3",
                  desc="""\
    test_caseInsensitive:
        This test does not care about the validity of the result. Rather, it
        ensures that the word score is case insensitive by checking that the
        results of the same word--in different cases--is the exact same.
            EX: scoreWord('Queen') == scoreWord('queEN'): Can still pass
                even if scoreWord('Queen') != 57, the correct score
    test_emptyString:
        Verifies that the empty string returns a score of 0.
    test_validity_lettersOnly:
        This test ensures that the score of each word is summed up correctly.
        This test ommits special characters, and only tests alphabetic
        characters.
            EX: wordScore("ABC") == 3
    test_validity_mixedChars:
        This test ensures that the score of each word is summed up correctly.
        This test includes non-alphabetic characters, which should have a score
        of 0.
            EX: wordScore("A3BC") == 3
    test_validity_singleCharacter:
        This test ensures that the score of each single character is correct.
        Checks all alphabetic characters individually, lowercase and uppercase.
            EX: wordScore('A') == 0 and wordScore('Z') == 25"""),
]


def helpResponse(ALL_TESTS):
    '''
    To be invoked when the user asks for help with the program.
    Program quits with exit code 1
    '''
    print("""\
USAGE: $ python runTests.py [TESTS]

If [TESTS] is ommitted, the program will run all provided tests against the
exercises.

[TESTS] is an optional parameter of space separated integers. This is
provided only if the user wants to run specific tests. To run only tests
against exercises 0 and 3, one would input `python runTests.py 0 3`.

The following tests can be run:""")

    for test in ALL_TESTS:
        print("    " + test.argName + " : " + test.title)
    sys.exit(1)


if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv:
        helpResponse(ALL_TESTS)

    testsToRun = []
    if len(sys.argv) == 1:
        testsToRun = ALL_TESTS
    else:
        for test in ALL_TESTS:
            if test.argName in sys.argv[1:]:
                testsToRun.append(test)

    if len(testsToRun) == 0:
        helpResponse(ALL_TESTS)
    runTests(testsToRun)
