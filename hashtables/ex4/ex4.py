def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # The Strategy:
    # The purpose is to find the absolute value of each negative numbers 
    # exists in the list of numbers
    # All integers that are less than zero mean negative, have the absolute 
    # value of the number its self
    # There is no -0 in maths

    # How to approach the problem:
    # I am creating a nums_dict to store my numbers
    # I also create an empty result array were I will populated with the list of negative numbers
    # I m start looping each number and checking if the absolute value of our number 
    # belongs to our nums_dict
    # here I m going to use a built-in function called abs() it will return me the absolute value
    # for the input given number
    nums_dict = {}
    result = []
    for num in a:
        # it takes the absolute value of each negative number 
        # it makes it a positive number and checks if it exists in
        # the list of dict list of numbers numbers
        if nums_dict.get(abs(num)):
            # if it exists we add it to our result list 
            result.append(abs(num))
        else:
            # otherwise it is added to our nums_dict list
            nums_dict[abs(num)] = num
    return result
    # so in table result there will be all the positive numbers
    # that have corresponding negative numbers


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
