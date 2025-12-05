import mod1  # this executes print(f"{__name__}") line in mod1.py and __name__ will be set to mod1

mod1.main()

print(f"{__name__}")  # this will be __main__ if this file is run
