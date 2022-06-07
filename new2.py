def efficientJanitor(weight):
    # Write your code here
    my_sum=0
    n=len(weight)
    for index,elem in enumerate(weight):
        if elem==3.0:
            my_sum+=1
        elif 1.01<=elem<=3.0:
            new_item=elem+weight[index+1]
            if 1.01<=new_item<=3.0:
                my_sum+=1
                weight.remove(weight[index+1])
            else:
                my_sum+=1
        weight.remove(elem)
    return my_sum