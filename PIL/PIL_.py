import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.cell
def _():
    import PIL
    return (PIL,)


@app.cell
def _(PIL):
    PIL.Image()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
