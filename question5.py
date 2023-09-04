# ************************ QUESTION 5 **************************
# print the 3 last characters of the str in upper upper case
def question5(my_string):
    # ***** WRITE CODE HERE *****
    if len(my_string) <= 3:
        print(my_string)
    else:
        upper_my_string_last_3 = my_string[-3:].upper()
        cut_my_string_last_3 = my_string[:-3]
        my_new_string = cut_my_string_last_3 + upper_my_string_last_3
        print(my_new_string)
