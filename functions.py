# ============================================================
# PYTHON FUNCTIONS
# ============================================================
# A function is a reusable block of code that performs a task.
#
# Basic syntax:
#
# def function_name():
#     # code
#
# function_name()


# ============================================================
# PARAMETER vs ARGUMENT
# ============================================================
# Parameter:
#   A variable listed inside the function definition.
#
# Argument:
#   The actual value passed when calling the function.
#
# Example:

def greet(name):       # name = parameter
    print("Hello", name)

greet("Alex")          # "Alex" = argument


# Easy way to remember:
#
# PARAMETER = placeholder
# ARGUMENT  = actual value


# ============================================================
# 1. NO ARGUMENT TAKEN, NO RETURN GIVEN
# ============================================================
# The function doesn't receive anything
# and doesn't return a value.

def greet():
    print("Hello!")


greet()


# ============================================================
# 2. NO ARGUMENT TAKEN, RETURNS SOMETHING
# ============================================================
# The function doesn't receive anything,
# but returns a value.

def get_name():
    return "Alex"


name = get_name()

print(name)


# ============================================================
# 3. TAKES ARGUMENT / ARGUMENTS, NO RETURN GIVEN
# ============================================================
# The function receives a value,
# but doesn't return anything.

def greet(name):
    print("Hello", name)


greet("Alex")


# ============================================================
# 4. TAKES ARGUMENT / ARGUMENTS, RETURNS SOMETHING
# ============================================================
# The function receives values
# and returns a result.

def add(a, b):
    return a + b


result = add(5, 3)

print(result)


