#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination




def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # The Strategy:
    # Is to match the destinations of each ticket 
    # with its starting point
    # and then create the whole route
    # so that each destination is the aftermath for the next route

    # How to approach the problem:
    # Since I have sources and destinations it means that 
    # I have starting_point = source and ending_point = destination
    # Both of them start from NONE
    # I also create a ticket dict to hold tickets
    # and a route which will be an empty array(populated later with the path of the cities)
    # Then I need to connect(link) each individual ticket with its destination.
    # I also going to create a variable called current_city which
    # is destination for a previous city and at the same time source for another city
    # this variable will be equal with my storing tickets start as NONE
    # next step will be to add this current_city as none to my storage(dict) tickets
    
    
    ticket_dict = {}
    route = []
   
    
    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    
    curr_city = ticket_dict['NONE']
    route.append(curr_city)

    while curr_city != 'NONE':
        # the current_city takes the value from my storage
        curr_city = ticket_dict[curr_city]
        # and adding the current_city to my route path
        route.append(curr_city)

    return route
   
