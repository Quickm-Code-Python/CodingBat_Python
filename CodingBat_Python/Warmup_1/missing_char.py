# Given a non-empty string and an int n, return a new string where the char at 
# index n has been removed. The value of n will be a valid index of a char in 
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

# Examples:
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def missing_char(str, n):
  result = str
  size = len(str)
  if n > 0 and n < size-1:
    result = str[0:n] + str[n+1:]
  elif n ==0:
    result =  str[1:]
  elif n == size-1:
    result = str[0:size-1]
  return result

