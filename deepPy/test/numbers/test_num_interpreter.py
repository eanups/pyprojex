from src.numbers.num_interpreter import NumInterpreter


def test_num_type():
    i = 43
    ni = NumInterpreter(i)
    assert ni.get_type() == type(i)
