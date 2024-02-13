#!/usr/bin/env python3

if __name__ == "__main__":

    while True:
        pass_1 = input("Please input a new password: \n")
        pass_2 = input("Please input this password again: \n")

        if pass_1 != pass_2:
            print("Error: These passwords are incompatible. Try again. ")
        else:
            print('"Password Set"')
            break
