from dice import Dice
import time

sp = 15
fp = 20

def main():
  dice = Dice(1, 6)
  money = 500
  secret_number = dice.roll()

  print("Roll a dice game...")
  print(f"You have $500. If you roll the correct number, you win ${sp}.")
  print(f"If you won't roll the correct number, you'll lose ${fp}.")
  print("If your money reaches 0, you lose the game.")
  time.sleep(5)

  play = input("Shall we play? (y/n): ").lower()
  if play == 'y':
    print(f"Correct number: {secret_number}")
    while True:
      if money <= 0:
        print("Whoops, you're out of money! XD")
        time.sleep(5)
        quit()

      req = input("Roll? (y/n): ").lower()

      if req == 'y':
        roll = dice.roll()
        print(f"Result: {roll}")
        if roll == secret_number:
          money += sp
          print(f"Success! ${sp} are transferred to your account!")
          print(f"Current funds: ${money}")
        else:
          money -= fp
          print(f"Failed. ${fp} are taken from your account.")
          print(f"Current funds: ${money}")
      elif req == 'n':
        quit()
      else:
        print("Invalid response.")
  elif play == 'n':
    quit()
  else:
    print("Invalid response.")
  
main()
