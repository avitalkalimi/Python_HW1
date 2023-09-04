# ************************ QUESTION 2 **************************
# print the prime number in the index of the input number
def question2(input_number):
    ### WRITE CODE HERE
    checking_number = 0
    generic_number = 1
    # making checks like the number in the input
    while checking_number < input_number:
        generic_number += 1
        # call for help function, to tell if he get prime number
        if the_prime_chek(generic_number) is True:
            checking_number += 1
    print(generic_number)
    return


# will tell you if you get prime number or not
def the_prime_chek(generic_number):
    # algorithm for chek prime numbers
    for divisor in range(2, int(generic_number ** 0.5) + 1):
        if generic_number == 2:
            return True
        if generic_number % divisor == 0:
            return False
    return True
