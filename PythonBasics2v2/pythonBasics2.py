# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
   dictionary = {}
   count = 0
   for x in range(n):

    # Checks for each number and looks at sequence of numbers for each number
      if n in dictionary and n > 0:
        numbers = dictionary[x] % 3
      return dictionary[numbers]
  # Counts number of values each time x,y,z variables hit their target number in the sequence of numbers
      countNumberOfValues = countNumberOfValues + 1
      if count > countNumberOfValues :
        countNumberOfValues = count
      return count

      n2 = 0
      countNumberOfValues  = 0

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  dictionary = {}
  length = len(s)
  charCount = 0
  retStr = s[0]
  count  = 0

  for i in range(100):

      if (i < length - 1 and s[i] == s[i + 1]):

       count += 1

      else:

          if count > charCount:
              charCount = count
          retStr = s[i]
          count = dictionary.get(1)

          return retStr

















# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(string):
  # YOUR CODE HERE
  return string.lower().replace(" ", "") == string.lower().replace(" ", "")[::-1]


