class CustomError(Exception):
    pass

def check_value(value):
    if not isinstance(value, int):
        raise CustomError("Type Error: This is not an integer!")
    
    if value < 0:
        raise CustomError("Value Error: Negative values are not allowed!")

    print(f"Value is valid: {value}")

def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        raise CustomError("FileNotFound Error: File not found!")

def main():
    try:
        check_value("hello")
    except CustomError as e:
        print("Error:", e)

    try:
        check_value(-5)
    except CustomError as e:
        print("Error:", e)

    try:
        open_file("non_existent_file.txt")
    except CustomError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
