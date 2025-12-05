import tkinter as tk
import time

def im_karatsuba_approach(x, y, canvas, x_offset=50, y_offset=50, level=0):
    if x < 10 or y < 10:
        canvas.delete("all")
        draw_base_case(canvas, x, y, x_offset, y_offset, level)
        root.update()
        time.sleep(2)
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    high1, low1 = divmod(x, 10 ** half)
    high2, low2 = divmod(y, 10 ** half)

    canvas.delete("all")
    draw_split(canvas, x, high1, low1, x_offset, y_offset, level, label="X")
    draw_split(canvas, y, high2, low2, x_offset, y_offset + 50, level, label="Y")
    root.update()
    time.sleep(2)

    n0 = im_karatsuba_approach(low1, low2, canvas, x_offset, y_offset, level + 1)
    n1 = im_karatsuba_approach(high1, high2, canvas, x_offset, y_offset, level + 1)
    n2 = im_karatsuba_approach(high1 + low1, high2 + low2, canvas, x_offset, y_offset, level + 1) - n1 - n0

    canvas.delete("all")
    result = (n1 * 10 ** (2 * half)) + (n2 * 10 ** half) + n0
    draw_combination(canvas, n1, n2, n0, result, x_offset, y_offset, level)
    root.update()
    time.sleep(2)

    return result

def draw_split(canvas, num, high, low, x_offset, y_offset, level, label):
    num_length = len(str(num))
    width = max(100, num_length * 8)
    height = 30
    label_offset = 40

    canvas.create_text(x_offset - label_offset, y_offset + height // 2, text=f"{label}", font=("Helvetica", 10))
    rect = canvas.create_rectangle(x_offset, y_offset, x_offset + width, y_offset + height, outline="black")
    canvas.create_text(x_offset + width // 4, y_offset + height // 2, text=f"{high}", font=("Helvetica", 10))
    canvas.create_text(x_offset + 3 * width // 4, y_offset + height // 2, text=f"{low}", font=("Helvetica", 10))
    canvas.create_line(x_offset + width // 2, y_offset, x_offset + width // 2, y_offset + height, dash=(4, 2))

def draw_base_case(canvas, num1, num2, x_offset, y_offset, level):
    width = 200
    height = 50
    canvas.create_oval(x_offset, y_offset, x_offset + width, y_offset + height, outline="black")
    canvas.create_text(x_offset + width // 2, y_offset + height // 2, text=f"{num1 * num2}", font=("Helvetica", 10))

def draw_combination(canvas, n1, n2, n0, result, x_offset, y_offset, level):
    canvas.create_text(x_offset, y_offset, text=f"Combining: {n1}*10^{level*2} + {n2}*10^{level} + {n0} = {result}", font=("Helvetica", 10), anchor="nw")

def start_algo():
    try:
        n = int(entry.get())
        if n < 1 or n > 10:
            raise ValueError("Number out of range")
        file_name = f"IM_input_{n}.txt"
        with open(file_name, "r") as file:
            num1 = int(file.readline().strip())
            num2 = int(file.readline().strip())
        im_karatsuba_approach(num1, num2, canvas)
    except ValueError as e:
        canvas.delete("all")
        canvas.create_text(600, 400, text=f"Invalid input: {str(e)}", font=("Helvetica", 12), fill="red")
    except FileNotFoundError:
        canvas.delete("all")
        canvas.create_text(600, 400, text="File not found. Please check if file exist!", font=("Helvetica", 12), fill="red")

root = tk.Tk()
root.title("Integer Multiplication using Karatsuba's Approach")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=5)

label = tk.Label(frame, text="Enter file number (1-10):")
label.pack(side=tk.LEFT, padx=5)

entry = tk.Entry(frame, width=5)
entry.pack(side=tk.LEFT, padx=5)

button_start = tk.Button(frame, text="Start", command=start_algo)
button_start.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(root, width=1200, height=800, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
