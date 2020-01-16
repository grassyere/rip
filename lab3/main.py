def main():
    from lab_python_oop.rectangle import rectangle
    from lab_python_oop.circle import circle
    from lab_python_oop.square import square

    rect = rectangle(2, 3, "blue")
    rect.repr()

    circle = circle(5, "green")
    circle.repr()

    square = square(5, "red")
    square.repr()


if __name__ == "__main__":
    main()