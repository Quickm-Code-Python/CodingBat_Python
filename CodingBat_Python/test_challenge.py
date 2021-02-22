#!/usr/bin/python
from Warmup_1.sleep_in       import sleep_in
from Warmup_1.monkey_trouble import monkey_trouble
from Warmup_1.sum_double     import sum_double
from Warmup_1.diff21         import diff21
from Warmup_1.parrot_trouble import parrot_trouble



def print_challenge_name(challenge_name):
    challenge = challenge_name
    print("Code Challenge: %s: " %(challenge))

def test_sleep_in():
  print_challenge_name("Sleep In")

  weekday   = False
  vacation  = False
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

  weekday   = True
  vacation  = False
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

  weekday   = False
  vacation  = True
  print("Input : Weekend: %r   Vacation: %r" %(weekday, vacation))
  print("Output: %r" %(sleep_in(weekday, vacation)))
  print()

def test_monkey_trouble():
  challenge = "Monkey Trouble"

  print("Code Challenge: %s: " %(challenge))

  a_smile   = True
  b_smile   = True
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

  a_smile   = False
  b_smile   = False
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

  a_smile   = True
  b_smile   = False
  print("Input : Weekend: %r   Vacation: %r" %(a_smile, b_smile))
  print("Output: %r" %(monkey_trouble(a_smile, b_smile)))
  print()

def test_sum_double():
  print_challenge_name("Sum Double")

  a = 1
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

  a = 3
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

  a = 2
  b = 2
  print("Input : First: %d   Second: %d" %(a, b))
  print("Output: %d" %(sum_double(a, b)))
  print()

def test_diff21():
  print_challenge_name("Difference 21")

  num = 19
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

  num = 10
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

  num = 21
  print("Input : %d" %(num))
  print("Output: %d" %(diff21(num)))
  print()

def test_parrot_trouble():
  print_challenge_name("Parrot Trouble")

  talking = True
  hour    = 6
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()

  talking = True
  hour    = 7
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()

  talking = False
  hour    = 6
  print("Input : Talking: %r   Hour: %d" %(talking, hour))
  print("Output: %r" %(parrot_trouble(talking, hour)))
  print()


