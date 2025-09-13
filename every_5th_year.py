# This program is supposed to display every fifth year
# starting with 2024; that is, 2024, 2029, 2034, 2039,
# and so on, for 30 years.

def main():
  START_YEAR = 2024
  FACTOR = 5
  END_YEAR = 2054

  year = START_YEAR

  while year <= END_YEAR:
    print(year)
    year += FACTOR #add 5 each time
#Run the program
main()
