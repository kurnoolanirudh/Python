import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""Iterable = that which can be iterated over like lists, tuple, set""")
    return


@app.cell
def _():
    nums = [1, 2, 3]
    for num in nums:
        print(num)
    return (nums,)


@app.cell
def _(mo):
    mo.md(r"""for a object to be iterable __iter__ method should have been defined for it. Iterator is a object with a state so it remember where it is during iteration. Iterator get their next value with __next__. Iterators can only go forward""")
    return


@app.cell
def _(nums):
    i_nums = nums.__iter__()
    return (i_nums,)


@app.cell
def _(i_nums, nums):
    for _ in range(len(nums)):
        print(i_nums.__next__())
    return


@app.cell
def _(mo):
    mo.md(r"""another way to do the above thing""")
    return


@app.cell
def _(nums):
    i_nums_1 = iter(nums)
    for _ in range(len(nums)):
        print(next(i_nums_1))
    return


@app.cell
def _(mo):
    mo.md(r"""Custom Object With A Custom Iterator""")
    return


@app.class_definition
class MyRange:
    def __init__(self, start, end):
        self.start = start 
        self.end = end 

    def __iter__(self):
        return self 

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        curr = self.start
        self.start += 1
        return curr


@app.cell
def _():
    r = MyRange(1, 5)
    for i in r:
        print(i)
    return


@app.cell
def _(mo):
    mo.md(r"""Generators are also iterators where __iter__ and __next__ methods are created automatically""")
    return


@app.function
def my_range(max_num):
    for i in range(max_num):
        yield i


@app.cell
def _():
    nums1 = my_range(10)
    return (nums1,)


@app.cell
def _(nums1):
    nums1
    return


@app.cell
def _(nums1):
    for _ in range(10):
        print(next(nums1))
    return


@app.cell
def _(mo):
    mo.md(r"""Iterators can be infinite""")
    return


@app.cell
def _(mo):
    mo.md(r"""For a object to be iteratble it has to return a iterable from its __iter__ method""")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
