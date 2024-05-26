'''def check_even(num_list):

    for i in num_list:
        if i%2 == 0:
            return True
        else:
            pass

    return False

num_list = [1,4,7]
result = check_even(num_list)
print(result)'''

'''
def check_even(num_list):
#return all even numbers in list
    even_numbers = []

    for i in num_list:
        if i%2 == 0:
            even_numbers.append(i)
        else:
            pass

    return even_numbers

num_list = [1,43,25,6,72,27,22,56,68,74]
num_list.sort()
print(num_list)
result = check_even(num_list)
print(result)  '''

def emp_check(work_hours):
    current_max = 0
    emp_of_month = ''

    for i,j in work_hours: # i = employee, j = hours
        if j > current_max:
            current_max = j
            emp_of_month = i
        else:
            pass

    return (emp_of_month, current_max)


work_hours = [('Aashish', 300), ('Billy', 340), ('Cassie', 240)]
result = emp_check(work_hours)
print(result)