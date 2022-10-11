from gfse.api import timeit

@timeit
def say_hello():
    return {"message": "Hello API!"}
