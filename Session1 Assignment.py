# py_s1a1_swap_two_numbers - You’re helping a school where students use digital lockers that require secret codes to open. Two students accidentally got each other’s locker combinations. You need to swap the two combinations so each student gets their correct code.
# Your task is
# To write a program that swaps two numbers using a temporary variable, simulating the process of swapping locker codes.

# Before Swapping
Student1_Lockercode=5679293
Student2_Lockercode=3929765
print(Student1_Lockercode)
print(Student2_Lockercode)

# After Swapping
Temp =Student1_Lockercode
print("Temp is:",Temp)
Student1_Lockercode = Student2_Lockercode
Student2_Lockercode= Temp
print(Student2_Lockercode,)
print(Student1_Lockercode,Student2_Lockercode)



