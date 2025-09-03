#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  yourHour = input("Enter number of hours: ")
  yourHour = int(yourHour)
  #Ask user for minutes
  yourMinutes = input("Enter number of minutes: ")
  yourMinutes = int(yourMinutes)

  #Calculate the time after the user-supplied time has passed.
  futureMins = 3

  extrahour = currentMinute + yourMinutes

  futurehour = (currentHour + yourHour) % 24
  futureMin = (currentMinute + yourMinutes) % 60
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  if futureMins < 10:
    print(str(futurehour) + ":0" + str(futureMin))
  else:
    print(str(futurehour) + ":" + str(futureMin))

if __name__ == '__main__':
  main()
