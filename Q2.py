import random
import os

def generate_cpp_inputs():
    os.makedirs("closest_pair_point_inputs", exist_ok=True)
    for i in range(1, 11):
        points = [(random.randint(0, 1000), random.randint(0, 1000)) for _ in range(random.randint(200, 300))]
        with open(f"closest_pair_point_inputs/points_input{i}.txt", "w") as f:
            for x, y in points:
                f.write(f"{x} {y}\n")
    print("10 Closest Pair of Points files generated!")

def generate_integer_inputs():
    os.makedirs("integer_multiplication_inputs", exist_ok=True)
    for i in range(1, 11):
        num1 = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(200, 300))])
        num2 = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(200, 300))])
        with open(f"integer_multiplication_inputs/multiplication_input{i}.txt", "w") as f:
            f.write(f"{num1}\n{num2}\n")
    print("10 Integer Multiplication files generated!")

generate_cpp_inputs()
generate_integer_inputs()
