# List Comprehension
    # Faster
    # Readablity
'''
def valid(ages):
    valid_ages = [] # [18]
    for age in ages:
        if age >= 18:
            valid_ages.append(age)
            return valid_ages # Logic Error
'''
'''
def valid(ages):
    valid_ages = [] # []
    for age in ages:
        if age >= 18:
            valid_ages.append(age)
        return valid_ages # Logic Error
'''
'''
def valid(ages):
    valid_ages = [] # [18, 20, 33]
    for age in ages:
        if age >= 18:
            valid_ages.append(age)
    return valid_ages
'''
'''
def valid(ages):
    valid_ages = [age for age in ages if age >= 18] # List Comprehension # [18, 20, 33]
    return [age for age in ages if age >= 18]valid_ages
''' 
'''
def valid(ages):
    return [age for age in ages if age >= 18]

ages = [10, 3, 5, 7, 18, 20, 33]
print(valid(ages))
'''

numbers = [10.2, 5.3, 7.1, 9.9]
'''
float_nums = []
for num in numbers:
    float_nums.append(int(num))

print(float_nums) # [10, 5, 7, 9]
'''
'''
float_nums = [int(num) for num in numbers]
print(float_nums) # [10, 5, 7, 9]
'''

# Test the difference between the Normal and Comprehensive way:
import timeit

# Create a sample dataset of 1,000,000 numbers
numbers = list(range(1, 1_000_000))

# 1. The Traditional "For Loop" way
def loop_method():
    result = []
    for num in numbers:
        if num > 10:
            result.append(num)
    return result

# 2. The List Comprehension way
def comprehension_method():
    return [num for num in numbers if num > 10]

# Run each method 10 times and calculate the time taken
time_loop = timeit.timeit(loop_method, number=10)
time_comp = timeit.timeit(comprehension_method, number=10)

print(f"Traditional For Loop:  {time_loop:.4f} seconds")
print(f"List Comprehension:    {time_comp:.4f} seconds")


# Time for each:
# Traditional For Loop:  0.4215 seconds
# List Comprehension:    0.2810 seconds




















