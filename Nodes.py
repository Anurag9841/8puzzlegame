import pydot
class Node:
    goal_state = [0,0,1]
    i = 0

    def __init__(self,state,parent,action,depth):
        self.parent = parent
        self.state = state
        self.action = action
        self.depth = depth
        if self.goal_test():
            color = 'gold'
        elif self.is_killed():
            color = "red"
        elif self.is_valid():
            color = "green"
        else:
            color = "white"
        self.graph_node = pydot.Node(str(self), style="filled", fillcolor=color)
        Node.i+=1

    def __str__(self):
        return str(self.state)

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    def is_valid(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        boat = self.state[2]
        if missionaries < 0 or missionaries > 3:
            return False
        if cannibals < 0 or cannibals > 3:
            return False
        if boat > 1 or boat < 0:
            return False
        return True

    def is_killed(self):
        missionaries = self.state[0]
        cannibals = self.state[1]
        if missionaries < cannibals and missionaries > 0:
            return True
        if missionaries > cannibals and missionaries < 3:
            return True

    def generate_child(self):
        children = []
        depth = self.depth + 1
        if self.state[2] == 0:
            op = 1
        else:
            op = -1
        for missionary in range(3):
            for cannibals in range(3):
                new_state = self.state.copy()
                new_state[0] = new_state[0]+op * missionary
                new_state[1] = new_state[1]+op * cannibals
                new_state[2] = new_state[2]+ op * 1
                action = [missionary,cannibals]
                new_node = Node(new_state,self,action,depth)
                if (missionary + cannibals >= 1 and missionary + cannibals <= 2):
                    children.append(new_node)
        return children

    def solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution

node = Node([3,3,0],None,None,0)
a = node.generate_child()
print(a)


