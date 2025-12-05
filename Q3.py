import random
import os
import matplotlib.pyplot as plt
from math import sqrt

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


def closest_pair_of_points(points):
    def dist(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def closest_pair_recursive(pts):
        if len(pts) <= 3:
            min_d = float('inf')
            min_pair = None
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    d = dist(pts[i], pts[j])
                    if d < min_d:
                        min_d = d
                        min_pair = (pts[i], pts[j])
            return min_d, min_pair

        mid = len(pts) // 2
        mid_x = pts[mid][0]

        left_min_d, left_pair = closest_pair_recursive(pts[:mid])
        right_min_d, right_pair = closest_pair_recursive(pts[mid:])
        min_d = min(left_min_d, right_min_d)
        min_pair = left_pair if left_min_d < right_min_d else right_pair

        strip = [p for p in pts if abs(p[0] - mid_x) < min_d]
        strip.sort(key=lambda p: p[1])

        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                d = dist(strip[i], strip[j])
                if d < min_d:
                    min_d = d
                    min_pair = (strip[i], strip[j])

        return min_d, min_pair

    points.sort()
    return closest_pair_recursive(points)


def run_closest_pair(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            x, y = map(int, line.strip().split())
            points.append((x, y))

    _, closest_pair = closest_pair_of_points(points)
    print(f"Closest Pair in {file_path}: {closest_pair}")

    x, y = zip(*points)
    fig, ax = plt.subplots(figsize=(10, 8)) 
    ax.scatter(x, y, label="Points", color="blue", s=10) 

    for point in closest_pair:
        ax.scatter(*point, color="blue", s=10)
        ax.add_artist(plt.Circle(point, 15, color="green", fill=False, lw=2))  # Green circle around closest points

    ax.set_title("Closest Pair of Points", fontsize=16)
    ax.legend(["Points", "Closest Pair"], fontsize=12)
    ax.grid(True)
    plt.show()


def run_integer_multiplication(file_path):
    with open(file_path, "r") as f:
        num1 = int(f.readline().strip())
        num2 = int(f.readline().strip())

    result = num1 * num2
    print(f"Multiplication result in {file_path}: {result}")

def main():
    generate_cpp_inputs()
    generate_integer_inputs()

    for i in range(1, 11):
        closest_pair_file = f"closest_pair_point_inputs/points_input{i}.txt"
        run_closest_pair(closest_pair_file)

        integer_multiplication_file = f"integer_multiplication_inputs/multiplication_input{i}.txt"
        run_integer_multiplication(integer_multiplication_file)


if __name__ == "__main__":
    main()
