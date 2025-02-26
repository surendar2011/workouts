# Create a function with default arguments.

def greet(name, title="Mr.", message="Welcome"):
    print(f"{title} {name}, {message}!")

# Example usage:
greet("John") 
greet("Jane", "Ms.")  
greet("Alex", "Dr.", "Hello")  