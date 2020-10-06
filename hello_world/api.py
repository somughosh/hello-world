import fastapi
import uvicorn
from . import hello_world

app = fastapi.FastAPI()


@app.get("/{name}")
def main(name: str):
    return hello_world.hello(name)


@app.get("/")
def main():
    return hello_world.hello()


if __name__ == "__main__":
    uvicorn.run("hello_world.api:app")
