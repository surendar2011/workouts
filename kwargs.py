def print_kwargus(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargus(name="don", age=30, city="new york")