import typer
from .engine import Engine
app=typer.Typer()
@app.command()
def solve(): typer.echo(Engine().run())
