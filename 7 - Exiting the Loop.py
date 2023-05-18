for i in range(11): 
    if i == 8:
        break
    #Note that print is being executed AFTER the if / break condition.
    #We need to go till i = 8 since we want to print till 7
    print(i)
