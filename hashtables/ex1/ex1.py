def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    # How to approach the problem:
    # create a weight_dict = {}
    weight_dict = {}
    # Check if already exists in weight_dict
    for i in range(length): 
        # create a variable value were limited_weight is equal with the limit weight - weight indexes
        # limited_weight = (limit-weights[i])
        value = weight_dict.get(limit-weights[i])
        #if we find the value in weight_dict list:
        if value is not None:
            #can return a tuple with the index
            return (i, value)
         #If there is not a value in weight_dict list           
        else:
        #Set key to current value, value at index
            weight_dict[weights[i]] = i
    print(weight_dict)
   

    return None
