#Write a program that asks the user for one or more sentences and then lets the user know if it is a palindrome.

#User's Input
palindrome_check = input("Enter a sentence that reads the same way, back to front.")
print(palindrome_check[:]) #allows user to see what they input

#the user's input reversed
revstr=(palindrome_check[: : -1])

#Check the string & deliver decision
if revstr == palindrome_check: #if the string entered is the string reversed it's a palindrome
  print("Nice job! That is in fact a palindrome!")

else: 
  print("Try again!")


#code works for words; not sentences. I think I need to use the items listed in the notes section to ignore spaes and punctuation to make sentences work, but no idea how to apply them: see below:
# Notes
# You may want to use the re.sub function to strip out punctuation and spaces. A regular expression you can use to match all space and punctuation is r'[^A-Za-z]'.