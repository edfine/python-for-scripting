# Creating and Handling Errors and Exceptions

Errors and exceptions are a special class of thing in programming. They typically occur when you ask the programing language to do something impossible. For example:

* Divide by zero.
* Attempt to access data from a collection that does not exist.
* Attempt to execute Python code that contains a syntax error.
* (there are many more)

Although the nomenclature is muddled, generally speaking an "error" is a situation that the program cannot possibly recover from (e.g. a syntax error, there is no way to run the code because the intepreter cannot understand it) and an "exception" is a situation that the program can recover from (e.g. if a program attempts to access non-existing data it might be reasonable to create that data in some special code).

Python has features that allow programmers to create errors and exceptions, as well as features to handle exceptions. 

## Prerequisite Expectations

* You understand the basic syntax of python, including function creation and execution.

## Learning Objectives

* Students can describe the purpose of exceptions and errors in programming.
* Students can use the `raise` keyword to create and raise exceptions.
* Students can use the `try/except` syntax to handle exceptions.


## Technology Requirements

* Python 3.x

## Pre-reading Material

* None

## Post-Lesson Resources

* [Real Python Introduction to Exceptions](https://realpython.com/python-exceptions/)
