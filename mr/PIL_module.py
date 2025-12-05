import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""PIL module is used to deal with images""")
    return


@app.cell
def _():
    from PIL import Image
    return (Image,)


@app.cell
def _(Image):
    img1 = Image.open('')
    return


if __name__ == "__main__":
    app.run()
