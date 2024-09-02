# app.py
def hello_world(name="World"):
    return f"Hello, {name}!"
if __name__ == "__main__":
    print(hello_world())
    print(hello_world("Alice"))
