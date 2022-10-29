"""
Write a function that takes a string of braces,
and determines if the order of the braces is valid.
It should return true if the string is valid, and false if it's invalid.
"""

def valid_braces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''




print(valid_braces( "([}{])" ) == False)
print(valid_braces( "{}({})[]" ) == True)
print(valid_braces( "{{()}}" ) == True)
print(valid_braces( ")(}{][" ) == False)