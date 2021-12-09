__author__ = 'Sharayah Reyes'
# Program will calculate the down-payment cost for a house

# Input List: downpayment_percentage, cost_of_house
# Output List: downpayment_percentage, cost_of_house, downpayment_cost

# Declare Real downpayment_percentage
# Declare Integer cost_of_house
# Declare Real downpayment_cost

# Display welcome message

# Display "What is your down-payment percentage?"
# Input downpayment_percentage
# Display "What is the cost of the house?"
# Input cost_of_house
# Set downpayment_cost = downpayment_percentage * cost_of_house
# Display 'Your', downpayment_percentage, '% down-payment on', 'a $', cost_of_house,
#         'calculates to $', downpayment_cost

downpayment_percentage = 0.0
cost_of_house = 0
downpayment_cost = 0.0

print('Welcome to the House Down-Payment Calculator!')
print('Please enter your down-payment percentage (for example, .15 for 15%) along with the cost of the house')
print("and I'll calculate your down-payment.")

downpayment_percentage = float(input('What is your down-payment percentage? '))
cost_of_house = int(input('What is the cost of the house? '))
downpayment_cost = downpayment_percentage * cost_of_house
print('Your', downpayment_percentage, '% down-payment on', 'a $', cost_of_house,)
print('calculates to $', downpayment_cost)