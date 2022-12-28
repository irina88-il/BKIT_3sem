from random import randint
def get_random(num_count, begin, end):
    for i in range(num_count):
        yield randint(begin, end)
    

def main():
    a = get_random(5, 1 , 3)
    for i in a:
        print(i, end = ' ')
if __name__ == "__main__":
    main()
