# This program displays every combination of three digits

def main():
  for digit1 in range(10): # 0-9
    for digit2 in range(10): # 0-9
      for digit3 in range(10): # 0-9
        print(digit1, digit2, digit3)
main()        
