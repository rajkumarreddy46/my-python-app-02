# app.py
def hello_world(name="World"):
    return f"Hello, {name}!"
def goodbye_world(name="World"):
    return f"Goodbye, {name}!"
if __name__ == "__main__":
    print(hello_world())
    print(hello_world("Alice"))
    print(goodbye_world())
    print(goodbye_world("Alice"))
