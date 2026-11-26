import click
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "service-b ok"


@click.command()
@click.option("--port", default=8000, help="Port to listen on.")
def run(port: int) -> None:
    app.run(port=port)


if __name__ == "__main__":
    run()
