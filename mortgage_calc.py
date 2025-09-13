# A standard mortgage is paid monthly over 30 years. 
# This program is intended to output 360 payment coupons 
# for each new borrower at a mortgage company. 
# Each coupon lists the month number, year number, 
# and a friendly mailing reminder.

def main():
  #Constants
  MONTHS = 12
  YEARS = 30
  MSG = "Remember to allow 5 days for mailing"
  QUIT = 9999

  # Get first acount number
  acctNum = int(input(f"Enter account number or {QUIT} to quit: "))

  while acctNum != QUIT:
    #Generate 360 payment coupons (12 months x 30 years)
    for yearCounter in range(1, YEARS + 1):
      for monthCounter in range(1, MONTHS + 1):
        print(f"Account: {acctNum}, Month: {monthCounter}, Year: {yearCounter} -> {MSG}")

    # Ask for next account 
    acctNum = int(input(f"Enter account number or {QUIT} to quit: "))

  print("End of job")

# Run Program
main()
