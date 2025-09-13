# This code creates a report that contains an 
# apartment complex rental agent's commission. The 
# program accepts the ID number and name of the agent who 
# rented the apartment, and the number of bedrooms in the 
# apartment. The commission is $100 for renting a three-bedroom 
# apartment, $75 for renting a two-bedroom apartment, $55 for 
# renting a one-bedroom apartment, and $30 for renting a studio 
# (zero-bedroom) apartment. Output is the salespersons 
# name and ID number and the commission earned on the rental.

def main():
  #Commission constatns 
  COMM_3 = 100.00
  COMM_2 = 75.00
  COMM_1 = 55.00
  COMM_STUDIO = 30.00
  QUIT = 9999

  #Initail input
  salesPersonID = int(input(f"Enter salesperson ID or {QUIT} to quit: "))

  while salesPersonID != QUIT:
    salesPersonName = input ("Enter salesperosn name: ")
    numBedrooms = int(input("Enter number of bedrooms rented: "))

    # Determine commission
    if numBedrooms == 3:
      comissionEarned = COMM_3
    elif numBedrooms == 2:
      comissionEarned = COMM_2
    elif numBedrooms == 1:
      comissionEarned = COMM_1
    elif numBedrooms == 0:
      comissionEarned = COMM_STUDIO
    else:
      comissionEarned = 0.0 # handles invalid input

    # Output report for this agent
    print("\n--- Rental Report ---")
    print("Salesperson ID:", salesPersonID)
    print("Salesperson Name:", salesPersonName)
    print("Commission Earned: $", comissionEarned)
    print("----------------------\n")

    # Asks for next ID
    salesPersonID = int(input(f"Enter salesperson ID or {QUIT} to quit: "))

  print("End of report")

# Run the program
main()
