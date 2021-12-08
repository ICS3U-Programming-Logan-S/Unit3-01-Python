#!/usr/bin/env python3
# Created By: Logan Sweeney
# Date: Dec. 7, 2021
# This program asks the user for the subtotal and the tax
# percentage. It then calculates and displays the HST
# and the total.
import constants
import time

def main():
    # get user input
    subtotal = float(input("Enter subtotal: $"))
    
    # calculate the tax amount and the total with tax
    tax = subtotal * constants.PROVINCIAL_TAX / 100
    total = subtotal + tax

    # display the tax amount and the total with tax
    print("")
    print("Adding up tax.")
    time.sleep(0.75)
    print("Adding up tax..")
    time.sleep(0.75)
    print("Adding up tax...")
    time.sleep(1)
    print("")
    print("You entered a subtotal of ${:.2f}".format(subtotal))
    print("The added tax is ${0:.2f} and the ultimate total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()
