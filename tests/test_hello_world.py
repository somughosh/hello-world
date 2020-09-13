from hello_world import __version__, hello_world


def test_hello(capsys):
    hello_world.hello()
    assert capsys.readouterr().out == "Hello World\n"


def test_version():
    assert __version__ == "0.1.0"
