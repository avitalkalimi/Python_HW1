def question3(input_list):
    odd, even = [], [] #even - will contain all the even numbers in input_list (until 0) , odd is the same with odd numbers
    result = []
    for i in input_list:
        if (i == 0):  # run on list until 0 
            break
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    result.append(minimum(odd))
    result.append(minimum(even))

    odd.remove(minimum(odd))  #remove the number already added to result list 
    even.remove(minimum(even)) #same with even list

    result.append(minimum(odd)) 
    result.append(minimum(even))

    print (sum(result)/4) #print median

# this function use for found the minimun number in given list
def minimum(lst):
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

