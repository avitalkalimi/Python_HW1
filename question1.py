# ************************ QUESTION 1 **************************
# calc the square root result of the number minus twenty
def question1(number):
    ### WRITE CODE HERE
    if number < 20:  # if the number is less then twenty it will print - imaginary result
        print("imaginary result")
    else:
        number -= 20  # if the number is bigger then twenty - print the result
        number = number ** 0.5
        print("{:.2f}".format(number))
