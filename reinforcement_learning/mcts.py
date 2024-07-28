import math
import random

class MCTSNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0
    
    def is_fully_expanded(self):
        return len(self.children) == len(self.state.get_legal_actions())
    
    def best_child(self, c_param=1.4):
        choices_weights = [
            (child.wins / child.visits) + c_param * math.sqrt((2 * math.log(self.visits) / child.visits))
            for child in self.children
        ]
        return self.children[choices_weights.index(max(choices_weights))]

class MCTS:
    def __init__(self, state, num_iterations=1000):
        self.root = MCTSNode(state)
        self.num_iterations = num_iterations
    
    def search(self):
        for _ in range(self.num_iterations):
            node = self.select(self.root)
            reward = self.simulate(node.state)
            self.backpropagate(node, reward)
        return self.root.best_child(c_param=0)  # Exploit only

    def select(self, node):
        while not node.state.is_terminal():
            if not node.is_fully_expanded():
                return self.expand(node)
            else:
                node = node.best_child()
        return node

    def expand(self, node):
        actions = node.state.get_legal_actions()
        for action in actions:
            if not any(child.state == node.state.take_action(action) for child in node.children):
                new_state = node.state.take_action(action)
                new_node = MCTSNode(new_state, parent=node)
                node.children.append(new_node)
                return new_node
        raise Exception("Should never reach here")

    def simulate(self, state):
        current_state = state
        while not current_state.is_terminal():
            actions = current_state.get_legal_actions()
            action = random.choice(actions)
            current_state = current_state.take_action(action)
        return current_state.get_reward()

    def backpropagate(self, node, reward):
        while node is not None:
            node.visits += 1
            node.wins += reward
            node = node.parent

class TicTacToeState:
    def __init__(self, board=None, player=1):
        self.board = board if board is not None else [0] * 9
        self.player = player

    def get_legal_actions(self):
        return [i for i in range(9) if self.board[i] == 0]

    def take_action(self, action):
        new_board = self.board[:]
        new_board[action] = self.player
        return TicTacToeState(new_board, -self.player)

    def is_terminal(self):
        return self.get_winner() is not None or all(x != 0 for x in self.board)

    def get_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != 0:
                return self.board[combo[0]]
        return None

    def get_reward(self):
        winner = self.get_winner()
        if winner is None:
            return 0
        return 1 if winner == 1 else -1

    def __repr__(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        board_str = '\n'.join([' '.join([symbols[self.board[3 * row + col]] for col in range(3)]) for row in range(3)])
        return f"Player {self.player}'s turn\n{board_str}\n"


initial_state = TicTacToeState()
mcts = MCTS(initial_state, num_iterations=1000)
best_next_state = mcts.search()
print("Best next state:\n", best_next_state.state)
