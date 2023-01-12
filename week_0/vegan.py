from typing import Union


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def __str__(self):
        return f"Node({self.state})"

    def __repr__(self):
        return f"Node({self.state})"

    def is_valid(self, state):
        if state[0] < 0 or state[1] < 0 or state[0] > 3 or state[1] > 3:
            return False
        if state[0] == state[1] or state[0] == 3 or state[0] == 0:
            return True
        return False

    def get_children(self):
        children = []
        steps = {(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)}

        if self.state[2] == 'L':
            for step in steps:
                state = [None, None, None]
                state[0] = self.state[0] - step[0]
                state[1] = self.state[1] - step[1]
                state[2] = 'R'
                if self.is_valid(state):
                    children.append(Node(state, self))
        else:
            for step in steps:
                state = [None, None, None]
                state[0] = self.state[0] + step[0]
                state[1] = self.state[1] + step[1]
                state[2] = 'L'
                if self.is_valid(state):
                    children.append(Node(state, self))

        return children

    def get_parent(self):
        return self.parent

    def get_path(self):
        path = [self.state]
        parent = self.parent
        while parent is not None:
            path.append(parent.state)
            parent = parent.get_parent()

        return path[::-1]


class Space:
    def __init__(self, initial_state, final_state):
        self.frontier = None
        self.curr_node: Union[Node, None] = None
        self.initial_state = initial_state
        self.final_state = final_state
        self.visited = None

    def _is_goal(self):
        return self.curr_node.state == self.final_state

    def bfs(self):
        i = 0
        valid_nodes = {}
        self.visited = []
        self.frontier = [Node(self.initial_state)]
        while self.frontier:
            self.curr_node = self.frontier.pop(0)
            if self.curr_node.state not in self.visited:
                if self._is_goal():
                    valid_nodes[self.curr_node] = i
                self.frontier.extend(self.curr_node.get_children())
                self.visited.append(self.curr_node.state)
                i += 1
        return valid_nodes

    def dfs(self):
        i = 0
        valid_nodes = {}
        self.visited = []
        self.frontier = [Node(self.initial_state)]
        while self.frontier:
            self.curr_node = self.frontier.pop()
            if self.curr_node.state not in self.visited:
                if self._is_goal():
                    valid_nodes[self.curr_node] = i
                self.frontier.extend(self.curr_node.get_children())
                self.visited.append(self.curr_node.state)
                i += 1
        return valid_nodes

    def count_nodes(self):
        i = 0
        valid_nodes = {}
        self.visited = []
        self.frontier = [Node(self.initial_state)]
        while self.frontier:
            self.curr_node = self.frontier.pop(0)
            if self.curr_node.state not in self.visited:
                if self._is_goal():
                    valid_nodes[self.curr_node] = i
                self.frontier.extend(self.curr_node.get_children())
                self.visited.append(self.curr_node.state)
                i += 1
        print(self.visited)
        return i


if __name__ == '__main__':
    initial_state = [3, 3, 'L']
    final_state = [0, 0, 'R']
    space = Space(initial_state, final_state)

    nodes_dfs = space.dfs()
    print('DFS:')
    print(len(nodes_dfs))
    print(*[[i, len(node.get_path()) - 1, node.get_path()] for node, i in nodes_dfs.items()], sep='\n')

    print()

    nodes_bfs = space.bfs()
    print('BFS:')
    print(len(nodes_bfs))
    print(*[[i, len(node.get_path()) - 1, node.get_path()] for node, i in nodes_bfs.items()], sep='\n')


    print()
    total_search_space = space.count_nodes()
    print('Total number of nodes:')
    print(total_search_space)
