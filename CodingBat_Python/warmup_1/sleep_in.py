#!/usr/bin/python

# The parameter weekday is True if it is a weekday, and the parameter vacation 
# is True if we are on vacation. We sleep in if it is not a weekday or we're 
# on vacation. Return True if we sleep in.
# Examples:
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
  result = False
  if not weekday or vacation:
    result = True
  else:
    if weekday and not vacation:
      result = False
  return result
