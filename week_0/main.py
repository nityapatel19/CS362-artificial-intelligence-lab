import enum


class RABBITS(enum.Enum):
    EMPTY = 0
    EAST = 1
    WEST = 2

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.value}"


class Space:
    def __init__(self, initial_state, final_state):
        self.frontier = None
        self.curr_state = None
        self.path = []
        self.initial_state = initial_state
        self.final_state = final_state

    def _is_goal(self):
        return self.curr_state == self.final_state

    def _has_path_dfs(self, state, path=None):
        if path is None:
            path = []

        self.path.append(state)

        self.curr_state = state
        if self._is_goal():
            return True

        for child in self._get_children():
            if self._has_path_dfs(child, path):
                return True

        self.path.pop()
        return False

    def _has_path_bfs(self, state):
        self.path.append(state)
        self.curr_state = state
        if self._is_goal():
            return True

        for child in self._get_children():
            if self._has_path_bfs(child):
                return True

        self.path.pop()
        return False

    def dfs(self):
        self.path = []
        self.curr_state = self.initial_state
        if not self._has_path_dfs(self.initial_state):
            self.path = None
        return self.path

    def _get_children(self):
        children = []
        empty_index = self.curr_state.index(RABBITS.EMPTY)
        for i in range(empty_index - 1, empty_index - 3, -1):
            if i < 0:
                break
            if self.curr_state[i] == RABBITS.EAST:
                new_state = self.curr_state[:]
                new_state[i], new_state[empty_index] = RABBITS.EMPTY, RABBITS.EAST
                children.append(new_state)
                break

        for i in range(empty_index + 1, empty_index + 3):
            if i > len(self.curr_state) - 1:
                break
            if self.curr_state[i] == RABBITS.WEST:
                new_state = self.curr_state[:]
                new_state[i], new_state[empty_index] = RABBITS.EMPTY, RABBITS.WEST
                children.append(new_state)
                break
        return children


if __name__ == '__main__':
    initial_state = [RABBITS.EAST, RABBITS.EAST, RABBITS.EAST, RABBITS.EMPTY, RABBITS.WEST, RABBITS.WEST, RABBITS.WEST]
    final_state = [RABBITS.WEST, RABBITS.WEST, RABBITS.WEST, RABBITS.EMPTY, RABBITS.EAST, RABBITS.EAST, RABBITS.EAST]
    space = Space(initial_state, final_state)
    path = space.dfs()
    print(f"Number of steps = {len(path)-1}\n")
    print(*path, sep='\n')

