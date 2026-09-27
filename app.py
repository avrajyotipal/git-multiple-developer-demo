def welcome_message():
    print("Welcome to the Multi-Developer Git Project!")


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    welcome_message()

    result = add_numbers(10, 20)
    print(f"10 + 20 = {result}")