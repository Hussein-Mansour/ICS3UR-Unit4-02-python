#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/May12/2021
# This program uses a while loop


def main():
    # this function multiplies all the whole numbers up to that number

    # input
    positive_number = input("Enter a positive integer:")

    # process  & output
    try:
        positive_number_int = int(positive_number)

        if (positive_number_int < 0):
            print("you did not enter a positive integer.")
        elif(positive_number_int == 0):
            print("0 ! = 1")
        else:
            loop_counter = 1
            factorial = 1

            while (loop_counter <= positive_number_int):
                factorial = factorial * positive_number_int
                positive_number_int = positive_number_int - 1
                loop_counter = loop_counter

            print("{} ! = ".format(positive_number), factorial)
    except Exception:
        print("invalid input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
