__author__ = 'Sharayah Reyes'

import locale
locale.setlocale(locale.LC_ALL, '')

# This program calculates the down-payment percent of multiple houses of the users choice
# starting with the minimum value the user inputs and incrementing by 100,000 every iteration
# until reaching the maximum value the user enters

# Input List: price_min, price_max, percent
# Output List: first, price_min, price_ max, last


# Function Boolean is_valid_integer(String input_price)
#   Try float(input_string)
#       Return True
#   Except ValueError
#       Return False
# End Function

def is_valid_integer(input_price):
        try:
            int(input_price)
            return True
        except ValueError:
            return False


# Function Integer input_integer(String prompt)
#   Declare String input_price
#
#   While True
#       Display prompt
#       Input input_price
#       If input_price is valid Integer Then
#           If int(input_price) >= 100000 Then
#              Return input_price
#           End If
#       End If
#       Display "Looks like something went wrong, please re-enter your price."
#   End While
# End Function

def input_integer(prompt):
    while True:
        input_price = input(prompt)
        if is_valid_integer(input_price):
            if int(input_price) >= 100000:
                return int(input_price)
        print("Looks like something went wrong, please re-enter your price.")


# Function Integer get_house_price(String prompt)
#   Display prompt
#
#   Set house_price = input_integer("Please enter the cost of a house (do not include $ sign): ")
#   Return house_price
# End Function

def get_house_price(prompt):
    print(prompt)
    house_price = input_integer("Please enter the cost of a house (do not include $ sign): ")
    return house_price


# Function Boolean is_valid_float(input_percent)
#   Try float(input_percent)
#       Return True
#   Except ValueError
#       Return False
# End Function

def is_valid_float(input_percent):
    try:
        float(input_percent)
        return True
    except ValueError:
        return False


# Function Real input_float(String prompt)
#   Declare String input_percent
#
#   While True
#       Display prompt
#       Input input_percent
#       If input_percent is valid Real Then
#           If float(input_percent) >= 0 Then
#              Return input_percent
#                If float(input_percent) < 1 Then
#                   Return input_percent
#           End If
#       End If
#    End If
#    Display "Looks like something went wrong, please re-enter your percentage."
#   End While
# End Function

def input_float(prompt):
    while True:
        input_percent = input(prompt)
        if is_valid_float(input_percent):
            if float(input_percent) > 0:
                if float(input_percent) < 1:
                    return float(input_percent)
        print("Looks like something went wrong, please re-enter your percentage.")


# Function Real get_downpayment_percent()
#   Declare Real downpayment_percent
#
#   Set downpayment_percent = input_float("Please enter a down-payment percentage in the form of a decimal "
#                                        "(for example, .10 for 10%):  ")
#   Return downpayment_percent
# End Function

def get_downpayment_percent():
    downpayment_percent = input_float("Please enter a down-payment percentage in the form of a decimal "
                                "(for example, .10 for 10%): ")
    return downpayment_percent


# Module downpayment_costs(Integer price_min, Integer price_max,  Real percent)
#   Declare Real first
#   Declare Real last
#
#   Display ''
#   Display "House Price Ranges:", "        ","Down-payment of", "{0:.0%}".format(percent))
#           (locale.currency(price_min, grouping=True)), "-",
#           (locale.currency(price_max, grouping=True))
#   Display "-------------------------------------------------"

#   While price_min < price_max
#       Set first = price_min * percent
#       Display (locale.currency(price_min, grouping=True),"                ",
#               (locale.currency(first, grouping=True)))
#       price_min += 100000
#    Set last = price_max * percent
#    Display (locale.currency(price_max, grouping=True)),"                ",locale.currency(last, grouping=True)
#    Display ""
#    Display "Thank you for using the down-payment calculator! Good-bye!"
# End Module

def downpayment_costs(price_min, price_max, percent):
    print()
    print("House Price Ranges:", "        ","Down-payment of", "{0:.0%}".format(percent))
    print((locale.currency(price_min, grouping=True)), "-",
          (locale.currency(price_max, grouping=True)))
    print("-------------------------------------------------")

    while price_min < price_max:
            first = price_min * percent
            print((locale.currency(price_min, grouping=True)),"                ",
                  ((locale.currency(first, grouping=True))))
            price_min += 100000
    last = price_max * percent
    print((locale.currency(price_max, grouping=True)),"                ",locale.currency(last, grouping=True))
    print("Thank you for using the down-payment calculator! Good-bye!")


# Module main()
#   Declare Integer price_min
#   Declare Integer price_max
#   Declare Real percent
#
#    Display "Welcome to the house down-payment calculator! Please enter a minimum and maximum price of a house "
#            "and your down-payment percentage."
#    Display "From there, we will calculate your down-payment cost "
#            "starting from your listed minimum price and ending at your maximum price."
#    Display ""
#   Set price_min = get_house_price("What would you like your minimum house price to be (price "
#                                   "can be no less than $100,000)?")
#   Set price_max = get_house_price("What would you like your maximum house price to be?")
#   If price_min > price_max Then
#       Display "Uh-oh! Looks like something went wrong. Please re-read the instructions "
#               "and try again."
#       Return
#   End If
#   Set percent = get_downpayment_percent()
#   Call downpayment_costs(price_min, price_max, percent)
# End Module

def main():

    price_min = 0
    price_max = 0
    percent = 0.0

    print("Welcome to the house down-payment calculator! Please enter a minimum and maximum price of a house "
          "and your down-payment percentage.")
    print("From there, we will calculate your down-payment cost "
          "starting from your listed minimum price, and incrementing by $100,000, until your maximum price is reached.")
    print("")
    price_min = get_house_price("What would you like your MINIMUM house price to be (price "
                                "can be no less than $100,000)?")
    price_max = get_house_price("What would you like your MAXIMUM house price to be?")
    if price_min > price_max:
        print("Uh-oh! Looks like something went wrong. Please re-read the instructions "
              "and try again.")
        return
    percent = get_downpayment_percent()
    downpayment_costs(price_min, price_max, percent)

main()
