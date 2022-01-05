
import io
from contextlib import redirect_stdout


def get_output(func):
    ios = io.StringIO()
    with redirect_stdout(ios):
        func()
    return ios.getvalue()


def persist(value, path):
    f = open(path, "w")
    f.write(value)
    f.close()


def readfile(path):
    f = open(path, "r")
    output = f.read()
    f.close()
    return output
