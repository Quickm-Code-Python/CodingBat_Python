#!/usr/bin/python
from  Warmup_1.sleep_in       import sleep_in
from  Warmup_1.monkey_trouble import monkey_trouble

def test_sleep_in():
  challenge = "Sleep In"

  print("Code Challenge: %s: " %(challenge))

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
