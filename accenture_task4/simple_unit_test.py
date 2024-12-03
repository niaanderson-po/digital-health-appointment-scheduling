def hello_function():
    return "hello"

def test_hello_funtion():
    string = "hello"
    assert (string == hello_function()) is True
