from src.Scanner import Scanner
from src.SymbolTable import SymbolTable


def test():
    # for lab2 below ---------------------------

    # size = 15
    # st = SymbolTable(size)
    # firstVals = ['a', 'b', 'geo', 'd']
    # secondVals = ['15', '2', '7']
    # assert (st.size()) == (0)
    # for identifier in firstVals:
    #     st.add(identifier)
    # assert (st.size()) == (4)
    # for identifier in secondVals:
    #     st.add(identifier)
    # assert (st.size()) == (7)
    # listPosition, dequePosition = st.getPosition('z')
    # assert (listPosition) == (-1)
    # posBefore, dequeBefore = st.getPosition('a')
    # assert (posBefore) != (-1)
    # st.remove('a')
    # posAfter, dequeAfter = st.getPosition('a')
    # assert (posAfter) == (-1)
    # assert (st.size()) == (6)
    # print(st)

    # for lab3 below ---------------------

    reservedWords = ["let", "func", "returns", "is", "or", "and", "print", "while", "return", "if", "else", "then",
                     "integer", "boolean", "array", "true", "false", "scan"]
    operators = ["<", "<=", ">", " >=", "==", "!=", "=", "+", "-", "*", "%", "/"]
    separators = ["(", ")", ",", ";", "\"", " ", "{", "}"]
    scanner = Scanner(reservedWords, operators, separators)
    scanner.read_file('p1error.in')
    scanner.write_files('st.out', 'pif.out')



if __name__ == "__main__":
    test()
