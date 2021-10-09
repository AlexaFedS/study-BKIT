from lab_python_oop.rectangle import rectangle
from lab_python_oop.circle import circle
from lab_python_oop.square import square

def main():
    r = rectangle(2, 3, "синего")
    c = circle(3, "красного")
    s = square("желтого", 2)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()