#!usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Oct 2019
# This program shows if a letter is a vowel or consanent

import constants


def main():
    letter = input("Enter an letter: ") 
    letter_upper = letter.upper()
    print("")
    
    if letter_upper == "A" or letter_upper == "E":
        print("The letter {} is a vowel.".format(letter))
    elif letter_upper == "Y":
        print("{} is sometimes a vowel or a consonant.".format(letter))
    else:
        if len(letter_upper) == 1:
            if letter_upper[0].isalpha() == True:
                print("The letter is a consonant.")
            else:
                print("Bad input.")
        else:
            print("Bad input.")


if __name__ == "__main__":
    main()
