# ************************ QUESTION 4 **************************
# check for perfect numbers
def question4(input_number):
    # ***** WRITE CODE HERE *****
    sum = 0
    for the_divisor in range(1, input_number):  # check all the divisor of the input number
        if input_number % the_divisor == 0:
            sum += the_divisor
    if sum == input_number:
        print("True")
    if sum != input_number:
        print("False")
