#Program to check if a string is palindrome or not


my_str = 'aIbohPhoBiA'

#make it suitable for caseless comparison
my_str = my_str.casefold()

#reverse the string
rev_str = reversed(my_str)


#cgeck if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is apalindrome.")

else:
    print("The string is not a palindrome.")
