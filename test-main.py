from main import add

def testAdd():
    assert add(2, 3) == 5
    print("Add function works fine!")
    assert add(5, 5) == 10
    

if __name__ == '__main__':
    testAdd()