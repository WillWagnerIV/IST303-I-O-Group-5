# IST303 I/O Group 5
# Abinash Adhikari, Chukwudi Oguejiofor, William Wagner, Siyu Xiang, Manar Al-kayed

'''
Week 3 Team Exercise

This is a team exercise. Submit the program in a file named team_ex3.py to Canvas. The program does the following:

    It accepts input from stdin.
    Program echoes the input and whether it’s an odd number or even number.
    The program repeats step 1 until it receives input that is not a nonnegative integer, in which case the program says “This program only accepts numbers as input.” And quits.

Examples of input and output:

Input
Output
1
1 is an odd number
2
2 is an even number
a
This program only accepts non_negative integers as input.
'''


# Main Loop
while True:

    print()
    numIn = input("Please enter a positive integer: ")

    try: 
        
        if int(numIn) < 0 :
            print("That was a negative integer.")
                
        elif int(numIn) % 2 == 0:
            print(numIn + " is an even number")

        else:
            print(numIn + " is an odd number")

    except ValueError:
        print("This program only accepts non-negative integers as input.")
        break