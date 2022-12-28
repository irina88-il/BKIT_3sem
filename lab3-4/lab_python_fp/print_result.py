def print_result(func):
    def wrapper(*args):
        ret = func(*args)
        name = func.__name__
        print(name)
        if type(ret) == list:
            for i in ret:
                print(i)
        elif type(ret) == dict:
            for i in ret.keys():
                    print (i, ' = ', ret[i])
        else:
            print (ret)
            
        return ret
    
    return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
                

        
    
