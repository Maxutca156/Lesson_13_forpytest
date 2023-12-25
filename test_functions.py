from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'
def test_hello_who_other():
    assert hello_who('Other') == 'Hello, Other'
    assert hello_who('Leo') == 'Hello, Leo'
    assert hello_who('Petr') == 'Hello, Petr'
    assert hello_who('Nikita') == 'Hello, Nikita'
    assert hello_who('Anton') == 'Hello, Anton'

def test_salary():
    assert(2, 2) != 8
    assert(3, 1) != 6