# type annotations in python are completely optional but tadding them can make tools give better support
# for example you get better auto complete support because of type annotations
# editors can detect more errors if type annotations are given
# to annotate generic type you have to use the typing module


from typing import Annotated, override


def get_full_name(first_name: str, last_name: str):
    return first_name.title() + " " + last_name.title()


print(get_full_name("john", "doe"))

names: list[str] = ["hello", "world", "galaxy"]
print(names)
print(type(names))

person: tuple[str, str, int] = ("John", "Male", 28)
print(person)
print(type(person))

byte_set: set[bytes] = {b"Hello", b"World", b"Galaxy"}
print(byte_set)
print(type(byte_set))

dct: dict[str, int] = {"A": 1, "B": 2, "C": 3}
print(dct)
print(type(dct))

# to annotate the fact that this variable can be either a int or a string
int_or_string: int | str = 1
print(int_or_string)
print(type(int_or_string))
int_or_string = "Hello"
print(int_or_string)
print(type(int_or_string))

# to annotate the fact that something could be None
# Optional is syntactic sugar for Something | None
optional_str: str | None = None
print(optional_str)
print(type(optional_str))
optional_str = "Hello"
print(optional_str)
print(type(optional_str))

# These types that take type parameters in square brackets are called Generic types or Generics,


# user defined types can also be annotated
class DumType:
    def __init__(self, dum: str):
        self.dum: str = dum

    @override
    def __repr__(self):
        return f"dum = {self.dum}"


dum: DumType = DumType("dum1")
print(dum)

# additional metadata can be put with type annotations
meta_data: Annotated[str, "just some metadata"] = "Hello"

print(meta_data)
