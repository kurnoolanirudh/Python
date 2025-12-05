# this will always run no matter how this is executed
print(f"module name = {__name__}")


def main():
    print("Hello, World")


# when the python file is directly run python interpreter sets the name to be __main__
# if some file imports stuff from this file then __name__ is set this file's name
# so the __name__ is used to check whether this file is being run or some module importing it is running this file
# the below code only executes when this file is run directly
# everything above this is executed no matter how this file is run
if __name__ == "__main__":
    main()
