# py_s2a2_compare_score_using_if_else -You are developing a program for a school competition where two students took a test. The school wants to know which student scored higher so they can announce the winner.
#
# Your task is to write a program that:
#
# Takes the scores of two students as input.
#
# Compares the scores using an if-else statement.
#
# Displays who scored higher or if it’s a tie.
score1 = int(input("Enter the score of Student 1: "))
score2 = int(input("Enter the score of Student 2: "))

if score1 > score2:
    print("Student 1 scored higher.")
elif score2 > score1:
    print("Student 2 scored higher.")
else:
    print("It's a tie!")
