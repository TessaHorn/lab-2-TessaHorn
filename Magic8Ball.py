#Magic8Ball.py
#Name: Tessa Horn
#Date: 09/02/2025
#Assignment: Magic 8 Ball Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answer = ["Maybe", "Without a doubt", "Yes", "No", "Absolutely not", 
          "As I see it, yes", "Ask again later", "Better not tell you now",
          "Cannot predict now", "Concentrate and ask again", "Don't count on it", 
          "It is certain", "It is decidedly so", "Most likely", "My reply is no", 
          "My sources say no", "Outlook good", "Outlook not so good", "Reply hazy, try again", 
          "Signs point to yes", "Very doubtful", "You may rely on it"]
  #Answer question randomly with one of the options from your earlier list.
input("What is your question: ")
print("Magic 8 Ball says: ", random.choice(answer))

if __name__ == '__main__':
  main()
