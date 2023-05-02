
import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action 

class StackFrontier():
    #last in first out data

    #creates frontier using list
    def __init__(seft): 
        self.frontier = []
    
    #adds to the frontier appending it to the end of the list
    def add(self, node):
        self.frontier.append(node)
    
    #checks if frontier contains a state
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    #checks if frontier is empty e.g length = 0
    def empty(self):
        return len(self.frontier) == 0

    #remove from the frontier
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[-1] #last item in list
            return node 


class QueueFrontier(StackFrontier):

    #remove from the begining of a list
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node