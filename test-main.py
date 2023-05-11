from main import add

def testAdd():
    assert add(2, 3) == 5
    assert add(5, 5) == 10
    print("Add function works fine!")

if __name__ == '__main__':
    testAdd()