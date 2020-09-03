#Algorithm that finds the maximum positive integer input by a user.
bool_controller = True
max_int = 0
while bool_controller == True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    elif num_int < 0:
        bool_controller = False
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
