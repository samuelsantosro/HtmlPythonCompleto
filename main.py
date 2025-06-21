from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def home():
    return "<h1>Hello, World teste 2</h1>"

serve()