import enum
from typing import Union


class RABBITS(enum.Enum):
    EMPTY = 0
    EAST = 1
    WEST = 2

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.value}"


class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def __str__(self):
        return f"Node({self.state})"

    def __repr__(self):
        return f"Node({self.state})"

    def get_children(self):
        children = []
        empty_index = self.state.index(RABBITS.EMPTY)
        for i in range(empty_index - 1, empty_index - 3, -1):
            if i < 0:
                break
            if self.state[i] == RABBITS.EAST:
                new_state = self.state[:]
                new_state[i], new_state[empty_index] = RABBITS.EMPTY, RABBITS.EAST
                children.append(Node(new_state, self))
                break

        for i in range(empty_index + 1, empty_index + 3):
            if i > len(self.state) - 1:
                break
            if self.state[i] == RABBITS.WEST:
                new_state = self.state[:]
                new_state[i], new_state[empty_index] = RABBITS.EMPTY, RABBITS.WEST
                children.append(Node(new_state, self))
                break
        return children

    def get_parent(self):
        return self.parent

    def get_state(self):
        return self.state

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

    def _is_goal(self):
        return self.curr_node.state == self.final_state

    def bfs(self):
        i = 0
        valid_nodes = {}
        self.frontier = [Node(self.initial_state)]
        while self.frontier:
            self.curr_node = self.frontier.pop(0)
            if self._is_goal():
                valid_nodes[self.curr_node] = i
            self.frontier.extend(self.curr_node.get_children())
            i += 1
        return valid_nodes

    def dfs(self):
        i = 0
        valid_nodes = {}
        self.frontier = [Node(self.initial_state)]
        while self.frontier:
            self.curr_node = self.frontier.pop()
            if self._is_goal():
                valid_nodes[self.curr_node] = i
            self.frontier.extend(self.curr_node.get_children())
            i += 1
        return valid_nodes


if __name__ == '__main__':
    initial_state = [RABBITS.EAST, RABBITS.EAST, RABBITS.EAST, RABBITS.EMPTY, RABBITS.WEST, RABBITS.WEST, RABBITS.WEST]
    final_state = [RABBITS.WEST, RABBITS.WEST, RABBITS.WEST, RABBITS.EMPTY, RABBITS.EAST, RABBITS.EAST, RABBITS.EAST]
    space = Space(initial_state, final_state)

    nodes_dfs = space.dfs()
    print(len(nodes_dfs))
    print(*[[i, len(node.get_path()) - 1, node.get_path()] for node, i in nodes_dfs.items()], sep='\n')

    print()

    node_bfs = space.bfs()
    print(len(node_bfs))
    print(*[[i, len(node.get_path()) - 1, node.get_path()] for node, i in node_bfs.items()], sep='\n')
