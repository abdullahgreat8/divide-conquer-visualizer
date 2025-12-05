import tkinter as tk
from tkinter import Canvas
from random import randint
import math
import time


def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force_closest(pair_list, canvas, all_pairs):
    min_dist = float("inf")
    closest_pair = None
    for i in range(len(pair_list)):
        for j in range(i + 1, len(pair_list)):
            refresh_canvas(canvas, all_pairs, None, f"Checking: {pair_list[i]}, {pair_list[j]}",
                           highlights=[pair_list[i], pair_list[j]])
            dist = calc_distance(pair_list[i], pair_list[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (pair_list[i], pair_list[j])
    return min_dist, closest_pair


def closest_in_band(band, min_dist, canvas, all_pairs, best_pair):
    closest_dist = min_dist
    closest_pair = best_pair
    band.sort(key=lambda p: p[1])
    for i in range(len(band)):
        for j in range(i + 1, len(band)):
            if (band[j][1] - band[i][1]) >= closest_dist:
                break
            refresh_canvas(canvas, all_pairs, closest_pair, "Evaluating band points",
                           highlights=[band[i], band[j]])
            dist = calc_distance(band[i], band[j])
            if dist < closest_dist:
                closest_dist = dist
                closest_pair = (band[i], band[j])
    return closest_dist, closest_pair


def compute_closest(points, canvas):
    def recursive_split(sorted_x, sorted_y):
        num_points = len(sorted_x)
        if num_points <= 3:
            return brute_force_closest(sorted_x, canvas, points)

        mid_idx = num_points // 2
        mid_point = sorted_x[mid_idx]

        canvas.create_line(mid_point[0], 0, mid_point[0], canvas.winfo_height(),
                           fill="purple", dash=(5, 5))
        canvas.update()
        time.sleep(0.5)

        left_half_x = sorted_x[:mid_idx]
        right_half_x = sorted_x[mid_idx:]
        left_half_y = [p for p in sorted_y if p[0] <= mid_point[0]]
        right_half_y = [p for p in sorted_y if p[0] > mid_point[0]]

        left_dist, left_pair = recursive_split(left_half_x, left_half_y)
        right_dist, right_pair = recursive_split(right_half_x, right_half_y)

        smallest_dist = min(left_dist, right_dist)
        closest_pair = left_pair if left_dist < right_dist else right_pair

        band = [p for p in sorted_y if abs(p[0] - mid_point[0]) < smallest_dist]
        canvas.create_rectangle(mid_point[0] - smallest_dist, 0,
                                mid_point[0] + smallest_dist, canvas.winfo_height(),
                                outline="green", dash=(2, 2))
        canvas.update()
        time.sleep(0.5)
        band_dist, band_pair = closest_in_band(band, smallest_dist, canvas, points, closest_pair)
        return (band_dist, band_pair) if band_dist < smallest_dist else (smallest_dist, closest_pair)

    points_x = sorted(points)
    points_y = sorted(points, key=lambda p: p[1])
    return recursive_split(points_x, points_y)


def refresh_canvas(canvas, points, best_pair, message, highlights=None):
    canvas.delete("all")
    radius = 5

    for x, y in points:
        color = "orange"
        if highlights and (x, y) in highlights:
            color = "blue"
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)

    if best_pair:
        x1, y1 = best_pair[0]
        x2, y2 = best_pair[1]
        canvas.create_line(x1, y1, x2, y2, fill="cyan", width=2)
        message += f"\nClosest Points: {best_pair[0]} and {best_pair[1]}"

    canvas.create_text(400, 580, text=message, fill="black", font=("Arial", 12))
    canvas.update()
    time.sleep(0.5)


def generate_random_points(count, canvas):
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    return [(randint(50, width - 50), randint(50, height - 50)) for _ in range(count)]


def initiate_simulation(canvas):
    canvas.delete("all")
    num_points = 20
    random_points = generate_random_points(num_points, canvas)

    refresh_canvas(canvas, random_points, None, "Generated Random Points")

    _, closest_points = compute_closest(random_points, canvas)
    refresh_canvas(canvas, random_points, closest_points, "Closest Pair Found")


def main():
    window = tk.Tk()
    window.title("Closest Pair Visualizer")

    canvas = Canvas(window, width=800, height=600, bg="white")
    canvas.pack()

    controls = tk.Frame(window)
    controls.pack()
    start_btn = tk.Button(controls, text="Run Simulation",
                          command=lambda: initiate_simulation(canvas))
    start_btn.pack(side=tk.LEFT, padx=10)

    window.mainloop()


if __name__ == "__main__":
    main()
