# count_up.py
def count_up(start, end):
    """Print all numbers from start up to and including end."""
    for num in range(start, end + 1):
        print(num)

count_up(5, 10)

# in_range.py
def in_range(num, lower, upper):
    """Return True if num is in range [lower, upper], inclusive."""
    return lower <= num <= upper

print(in_range(5, 1, 10))
print(in_range(11, 1, 10))

# sum.py
def sum_nums(nums):
    """Return the sum of a list of numbers."""
    total = 0
    for num in nums:
        total += num
    return total

print(sum_nums([1, 2, 3, 4]))
print(sum_nums([]))

# any7.py
def any7(nums):
    """Return True if any of the numbers is a 7."""
    for num in nums:
        if num == 7:
            return True
    return False

print(any7([1, 2, 3, 4, 5, 6, 7]))
print(any7([1, 2, 3, 4, 5, 6]))

# convert.py
def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9.0/5.0) + 32
    return fahrenheit

print(f_to_c(100))
print(c_to_f(0))