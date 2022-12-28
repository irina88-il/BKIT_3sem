from lab_python_oop.rectangle import rectangle
from lab_python_oop.circle import circle
from lab_python_oop.square import sq

'''
import numpy
a = np.array([1, 2, 3], int)
a.shape
'''
def main():
    r = rectangle(13, 13, "синего")
    c = circle(13, "зеленого")
    s = sq(13, "красного")
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
