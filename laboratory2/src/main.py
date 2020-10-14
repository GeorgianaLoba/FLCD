from src.SymbolTable import SymbolTable


def test():
    size = 15
    st = SymbolTable(size)
    firstVals = ['a', 'b', 'geo', 'd']
    secondVals = ['15', '2', '7']
    assert (st.size()) == (0)
    for identifier in firstVals:
        st.add(identifier)
    assert (st.size()) == (4)
    for identifier in secondVals:
        st.add(identifier)
    assert (st.size()) == (7)
    listPosition, dequePosition = st.getPosition('z')
    assert (listPosition) == (-1)
    posBefore, dequeBefore = st.getPosition('a')
    assert (posBefore) != (-1)
    st.remove('a')
    posAfter, dequeAfter = st.getPosition('a')
    assert (posAfter) == (-1)
    assert (st.size()) == (6)
    print(st)

if __name__ == "__main__":
    test()
