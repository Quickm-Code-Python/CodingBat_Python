# Given a string, return a new string where the first and last chars have been exchanged.

# Examples:
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  result = str
  if len(str) > 1:
    rev = str[::-1]
    result = rev[0:1] + str[1:len(str)-1] + str[0:1]
  return result

