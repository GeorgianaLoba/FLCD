from src.Transition import Transition


class FiniteAutomata:
    # Q = states
    # Sigma = alphabet
    # Delta = transition functions
    # q0 = initial state
    # F = set of final states
    def __init__(self):
        self.Q = []
        self.Sigma = []
        self.q0 = ""
        self.F = []
        self.Delta = []

    def split_line(self, line):
        return line.strip().split(' ')

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            # first 4 lines are fixed sized
            self.Q = self.split_line(f.readline())
            self.Sigma = self.split_line(f.readline())
            self.q0 = self.split_line(f.readline())[0]
            self.F = self.split_line(f.readline())
            for line in f:
                self.Delta.append(Transition.get_transition_from_line(line))

    def __str__(self) -> str:
        stringg = ""
        stringg += "States: " + str(self.Q) + "\n"
        stringg += "Alphabet: " + str(self.Sigma) + "\n"
        stringg += "Initial state: " + str(self.q0) + "\n"
        stringg += "Final states: " + str(self.F) + "\n"
        for transition in self.Delta:
            stringg += str(transition)
        return stringg
