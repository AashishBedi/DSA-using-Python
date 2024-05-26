'''st = 'Print only the words that with s in this sentence'
#st.split()
print(st.split())'''
'''
# Taking input for a list of integers
input_string = input("Enter a list of integers separated by spaces: ")

# Splitting the input string into a list of strings
input_list_of_strings = input_string.split()

# Converting the list of strings to a list of integers
input_list_of_integers = [int(num) for num in input_list_of_strings]

print("Input list of integers:", input_list_of_integers)
'''

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("Fizzzbuzz")
    elif i%3 == 0:
        print("Fizzz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)