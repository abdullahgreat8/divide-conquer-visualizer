import tkinter as tk
from tkinter import messagebox, ttk
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
    messagebox.showinfo("Success", "10 Closest Pair of Points files generated!")


def generate_integer_inputs():
    os.makedirs("integer_multiplication_inputs", exist_ok=True)
    for i in range(1, 11):
        num1 = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(200, 300))])
        num2 = ''.join([str(random.randint(0, 9)) for _ in range(random.randint(200, 300))])
        with open(f"integer_multiplication_inputs/multiplication_input{i}.txt", "w") as f:
            f.write(f"{num1}\n{num2}\n")
    messagebox.showinfo("Success", "10 Integer Multiplication files generated!")


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


def run_closest_pair(selection, output_label):
    if not selection:
        messagebox.showerror("Error", "No file selected!")
        return

    filepath = f"closest_pair_point_inputs/{selection}"
    points = []
    with open(filepath, "r") as f:
        for line in f:
            x, y = map(int, line.strip().split())
            points.append((x, y))

    _, closest_pair = closest_pair_of_points(points)

    result_window = tk.Toplevel()
    result_window.title("Closest Pair Result")
    result_window.geometry("400x300")

    result_label = tk.Label(result_window, text=f"Closest Pair: {closest_pair}", font=("Arial", 14))
    result_label.pack(pady=20)

    x, y = zip(*points)
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(x, y, label="Points", color="blue", s=10)

    for point in closest_pair:
        ax.scatter(*point, color="blue", s=10)
        ax.add_artist(plt.Circle(point, 15, color="green", fill=False, lw=2))

    ax.set_title("Closest Pair of Points", fontsize=16)
    ax.legend(["Points", "Closest Pair"], fontsize=12)
    ax.grid(True)

    plt.show()


def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10**half)
    high2, low2 = divmod(y, 10**half)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return z2 * 10**(2*half) + (z1 - z2 - z0) * 10**half + z0


def run_integer_multiplication(selection, output_label):
    if not selection:
        messagebox.showerror("Error", "No file selected!")
        return

    filepath = f"integer_multiplication_inputs/{selection}"
    with open(filepath, "r") as f:
        num1 = int(f.readline().strip())
        num2 = int(f.readline().strip())

    result = karatsuba(num1, num2)

    result_window = tk.Toplevel()
    result_window.title("Integer Multiplication Result")
    result_window.geometry("600x400")
    result_text = tk.Text(result_window, font=("Arial", 12), wrap="word", width=70, height=10)
    result_text.pack(pady=20)
    result_text.insert(tk.END, f"Multiplication Result (Karatsuba): {result}\n")
    result_text.config(state=tk.DISABLED)
    scrollbar = tk.Scrollbar(result_window, command=result_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    result_text.config(yscrollcommand=scrollbar.set)


def create_gui():
    root = tk.Tk()
    root.title("Divide and Conquer Algorithms")
    root.geometry("900x700")
    root.config(bg="#f0f0f0")

    tk.Label(root, text="Divide and Conquer Algorithms", font=("Arial", 20, "bold"), bg="#4A90E2", fg="white",
             padx=10, pady=10).pack(pady=20, fill=tk.X)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14), padding=10, background="#4A90E2", foreground="RoyalBlue")
    style.configure("TCombobox", font=("Arial", 12))
    
    frame_inputs = tk.Frame(root, bg="#f7f7f7", bd=2, relief="ridge", padx=10, pady=10)
    frame_inputs.pack(pady=20, fill="x", padx=30)

    tk.Label(frame_inputs, text="Generate Input Files", font=("Arial", 16, "bold"), bg="#f7f7f7").pack(pady=5)
    ttk.Button(frame_inputs, text="Generate Closest Pair Inputs", command=generate_cpp_inputs).pack(pady=10)
    ttk.Button(frame_inputs, text="Generate Integer Multiplication Inputs", command=generate_integer_inputs).pack(pady=10)

    frame_closest_pair = tk.Frame(root, bg="#f7f7f7", bd=2, relief="ridge", padx=10, pady=10)
    frame_closest_pair.pack(pady=20, fill="x", padx=30)

    tk.Label(frame_closest_pair, text="Closest Pair of Points", font=("Arial", 16, "bold"), bg="#f7f7f7").pack(pady=5)

    cpp_files = ttk.Combobox(frame_closest_pair, font=("Arial", 14))
    cpp_files['values'] = [f"points_input{i}.txt" for i in range(1, 11)]
    cpp_files.pack(pady=10)

    ttk.Button(frame_closest_pair, text="Run Closest Pair of Points", command=lambda: run_closest_pair(cpp_files.get(), None)).pack(pady=10)

    frame_integer_mul = tk.Frame(root, bg="#f7f7f7", bd=2, relief="ridge", padx=10, pady=10)
    frame_integer_mul.pack(pady=20, fill="x", padx=30)

    tk.Label(frame_integer_mul, text="Integer Multiplication", font=("Arial", 16, "bold"), bg="#f7f7f7").pack(pady=5)

    im_files = ttk.Combobox(frame_integer_mul, font=("Arial", 14))
    im_files['values'] = [f"multiplication_input{i}.txt" for i in range(1, 11)]
    im_files.pack(pady=10)

    ttk.Button(frame_integer_mul, text="Run Integer Multiplication", command=lambda: run_integer_multiplication(im_files.get(), None)).pack(pady=10)

    ttk.Button(root, text="Exit", command=root.destroy).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
