def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x
    else:
        raise ValueError(f"Unknown shape: {shape}")
print("Rectangle (10 x 5):", calculate_area("rectangle", 10, 5))  
print("Square (4):", calculate_area("square", 4))  
print("Circle (radius 3):", calculate_area("circle", 3))
