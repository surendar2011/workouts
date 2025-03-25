# Write a function that takes keyword arguments using **kwargs.


# **kwargs collects all keyword arguments into a dictionary.
def print_kwargus(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargus(name="don", age=30, city="new york")

# Output
# name: don
# age: 30
# city: new york
