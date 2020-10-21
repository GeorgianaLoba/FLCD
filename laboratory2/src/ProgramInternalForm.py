class ProgramInternalForm:
    def __init__(self):
        self.__repletion = []

    # position_st will be a tuple like (int, int)
    def add(self, token, position_st):
        self.__repletion.append((token, position_st))

    def __str__(self) -> str:
        out = ""
        for tuple in self.__repletion:
            out += str(tuple[0]) + " on symbol table: (" + str(tuple[1][0]) + ";" + str(tuple[1][1]) + ")\n"
        return out
