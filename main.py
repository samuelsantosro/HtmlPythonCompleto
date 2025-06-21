from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    grid = Html(
    Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/flexboxgrid/6.3.1/flexboxgrid.min.css", type="text/css"),
    Div(
        Div(Div("This takes up the full width", cls="box", style="background-color: #800000;"), cls="col-xs-12"),
        Div(Div("This takes up half", cls="box", style="background-color: #008000;"), cls="col-xs-6"),
        Div(Div("This takes up half", cls="box", style="background-color: #0000B0;"), cls="col-xs-6"),
        cls="row", style="color: #fff;"
    )
    )
    show(grid)
    return grid

serve()