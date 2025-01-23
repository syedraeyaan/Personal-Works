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
   
   bid[bidder] = bid_price # Assigns value (bid_price) to key (bidder)

   bidding_process = input("Y - Continue Bid Process | N - Stop bid process: ").lower()

   if bidding_process == 'y':
      continue_bidding = True
   elif bidding_process == 'n':
      continue_bidding = False
   else:
      print("Invalid Statement")
      continue_bidding = False

print("Do you want to know the highest bidder ?")

highest_bidder = input("y - to know the highest bidder | n - cancel: ").lower()

super_bidder = max(bid, key = bid.get)

if highest_bidder == 'y':
   print(f"Highest bidder is {super_bidder} with bid price = Rs {bid[super_bidder]}")
   print(bid)

elif highest_bidder == 'n':
   print(bid)

else:
   print("Invalid Input")