import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo # necessary for markdown to work 
    return (mo,)


@app.cell
def _():
    print("Hello, World")
    return


@app.cell
def _():
    lst = [1, 2, 3, 4, 5]
    return (lst,)


@app.cell
def _(lst):
    for i in lst:
        print(i)
    else:
        print("else block of for loop hit")
    return


@app.cell
def _(mo):
    mo.md(r"""else block gets executed if and only no break statements were executed in the loop""")
    return


@app.cell
def _(lst):
    for j in lst:
        if j == 3: break 
        print(j)
    else:
        print("else block of for loop hit")
    return


@app.cell
def _(mo):
    mo.md(r"""the above else syntax is available for while loops too""")
    return


@app.cell
def _():
    k = 0
    while k < 10:
        print(k)
        k += 1
    else:
        print("else block of while loop hit")
    return


@app.cell
def _():
    l = 0
    while l < 10:
        if l == 7: break 
        print(l)
        l += 1
    else:
        print("else block of while loop hit")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
