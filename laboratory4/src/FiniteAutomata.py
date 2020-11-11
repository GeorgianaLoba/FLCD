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

    def get_transitions_from_initial_state(self, state):
        transitions = []
        for transition in self.Delta:
            if transition.from_state == state:
                transitions.append(transition)
        return transitions

    def is_deterministic(self):
        for state in self.Q:
            transitions = self.get_transitions_from_initial_state(state)
            for transition in transitions:
                unique = list(filter(lambda x: x.alphabet != transition.alphabet, transitions))
                if len(unique) != len(transitions) - 1:
                    return False
        return True

    def is_accepted(self, sequence):
        if not self.is_deterministic():
            return False
        current = self.q0
        for c in sequence:
            transitions = self.get_transitions_from_initial_state(current)
            current_val = c
            current = None
            for t in transitions:
                if t.alphabet == current_val:
                    current = t.to_state
            if current is None:
                return False
        if current not in self.F:
            return False
        else:
            return True

    def __str__(self) -> str:
        stringg = ""
        stringg += "States: " + str(self.Q) + "\n"
        stringg += "Alphabet: " + str(self.Sigma) + "\n"
        stringg += "Initial state: " + str(self.q0) + "\n"
        stringg += "Final states: " + str(self.F) + "\n"
        for transition in self.Delta:
            stringg += str(transition)
        return stringg
