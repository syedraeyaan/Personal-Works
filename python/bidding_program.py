# Bidding program
# Take input as name & bid price
# Continue taking input until the user says no
# Check for the highest bid
# Print the name of bidder & their respective bid price

bid = {} # Empty bid dictionary

continue_bidding = True  # Assigned True boolean value to continue_bidding variable

while continue_bidding == True: # While loop runs when the statement passed is true and in this case continue_bidding is set to true.
   
   bidder = input("Enter your name: ") # Input as string
   bid_price = float(input("Enter the bid price: Rs")) # Price of bid in Rs
   
   bid[bidder] = bid_price # Assigns value to key

   bidding_process = input("Y - Continue Bid Process | N - Stop bid process: ")

   if bidding_process == 'Y':
      continue_bidding = True
   elif bidding_process == 'N':
      continue_bidding = False

print(bid)