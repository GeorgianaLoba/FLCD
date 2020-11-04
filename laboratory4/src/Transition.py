class Transition:
    def __init__(self, from_state, alphabet, to_state):
        self.from_state = from_state
        self.alphabet = alphabet
        self.to_state = to_state

    @staticmethod
    def get_transition_from_line(line):
        items = line.strip().split(' ')
        return Transition(items[0], items[1], items[2])

    def __str__(self) -> str:
        return "(" + str(self.from_state) + ", " + str(self.alphabet) + ") -> " + str(self.to_state) + "\n"
