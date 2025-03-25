# Implement short-circuit evaluation in a condition.

# Short-circuit evaluation means that Python stops 
# evaluating a logical expression as soon as the final result is determined. This improves efficiency and avoids unnecessary computations.

x = 0
y = 10

# Without short-circuiting, y / x would cause an error.
if x != 0 and y / x > 2:
    print("Condition met")
else:
    print("Condition not met")  # Output: Condition not met
