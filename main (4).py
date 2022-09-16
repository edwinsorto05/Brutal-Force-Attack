#imports time and random
import time
import random

#characters equal 'abcdefgh' and are converted into a list
chars = 'abcdefgh'
chars_list = list(chars)

#asks user for a username and a 8-letter password
username = input('Enter a username: ')
password = input('Enter a password 8 characters in length, using only the lowercase letters a, b, c, d, e, f, g, h: ')
#user password converts into a list
#attempts keeps track of attempts until password is cracked
password = list(password)
guess = ''
attempts = 0
#starts time for program to crack the password
start_time = time.time()
#while guess is not equal to password
while guess != password:
  #guess will go randomly through characters list in relation to length of the password (which should be 8)
  guess = random.choices(chars_list, k=len(password))
  #prints each possible password
  print('<--' + str(guess) + '-->')
  attempts = attempts + 1
  #if guess finally equals the password
  if guess == list(password):
    #the time will stop
    end_time = time.time()
    #program tells what the user's password is after cracking it
    print('Your password is: ' + ''.join(guess))
    #prints out the number of seconds it took for the program to crack the password
    print(f"The total duration of time was: {end_time-start_time} seconds.")
    #prints the number of attempts it took
    if attempts > 1:
      print('This took a total of', attempts, 'attempts.')
    else:
      print('This took', attempts, 'attempt.')