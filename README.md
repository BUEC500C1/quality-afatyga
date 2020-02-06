# Continuous-Integration
Objective of this exercise is to learn continuous build process (CB) and continuous integration (CI). 
You are expected to: 

- Write python program to convert Arabic Numerals to Roman Numerals 
- Integrate Continuous Build Process to check if your software in each development stage passed the build process. 
- Integrate unit test and run the unit test in continuous integration process.

For more informaiton, please check the assignment presentation.

Deadline for completion of this project is January 29th, 2019. 
You are expected to show all aspects of your work. This includes results of build process. 
You are expected to use Github actively during this exercise.

# My Process
Started with creating a basic version of computing from arabic to roman numeral, added CB and CI, wrote tests for it and then worked on error checking!

# How to Use it
- clone the repo
- hw1.py has the function conversion which can be used to convert from arabic to numeral
- test_conversion.py has numerous tests for the function conversion
- run test_conversion.py to see the tests pass

# How it works
- conversion takes in an integer and returns a string of the corresponding roman numeral
- does not allow for an input that is not an integer
- can only convert up until 4000
