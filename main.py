import tkinter as tk
import random

class CoordinateSystem(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin

    def plot_point(self, x, y, color="red", shape="oval", size=2):
        scaled_x = self.origin[0] + x
        scaled_y = self.origin[1] - y
        if shape == "oval":
            self.create_oval(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)
        elif shape == "rectangle":
            self.create_rectangle(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)

class CoordinateSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coordinate System")

        self.coordinate_system = CoordinateSystem(master, width=400, height=400)
        self.coordinate_system.pack(side=tk.LEFT)

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.x_label = tk.Label(self.input_frame, text="X:")
        self.x_label.grid(row=0, column=0, sticky=tk.E)
        self.x_entry = tk.Entry(self.input_frame)
        self.x_entry.grid(row=0, column=1)

        self.y_label = tk.Label(self.input_frame, text="Y:")
        self.y_label.grid(row=1, column=0, sticky=tk.E)
        self.y_entry = tk.Entry(self.input_frame)
        self.y_entry.grid(row=1, column=1)

        self.color_label = tk.Label(self.input_frame, text="Color:")
        self.color_label.grid(row=2, column=0, sticky=tk.E)
        self.color_entry = tk.Entry(self.input_frame)
        self.color_entry.grid(row=2, column=1)

        self.shape_label = tk.Label(self.input_frame, text="Shape:")
        self.shape_label.grid(row=3, column=0, sticky=tk.E)
        self.shape_entry = tk.Entry(self.input_frame)
        self.shape_entry.grid(row=3, column=1)

        self.size_label = tk.Label(self.input_frame, text="Size:")
        self.size_label.grid(row=4, column=0, sticky=tk.E)
        self.size_entry = tk.Entry(self.input_frame)
        self.size_entry.grid(row=4, column=1)

        self.random_button = tk.Button(self.input_frame, text="Random", command=self.random_plot)
        self.random_button.grid(row=5, columnspan=2)

        self.plot_button = tk.Button(self.input_frame, text="Plot", command=self.plot_point)
        self.plot_button.grid(row=6, columnspan=2)

    def plot_point(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            color = self.color_entry.get()
            shape = self.shape_entry.get()
            size = float(self.size_entry.get()) if self.size_entry.get() else 2
            self.coordinate_system.plot_point(x, y, color=color, shape=shape, size=size)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter numeric values for X, Y, and Size.")

    def random_plot(self):
        x = random.uniform(-110, 100)
        y = random.uniform(-100, 100)
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Random color
        shape = random.choice(["oval", "rectangle"])  # Random shape
        size = random.uniform(1, 10)  # Random size
        self.x_entry.delete(0, tk.END)
        self.x_entry.insert(0, str(x))
        self.y_entry.delete(0, tk.END)
        self.y_entry.insert(0, str(y))
        self.color_entry.delete(0, tk.END)
        self.color_entry.insert(0, color)
        self.shape_entry.delete(0, tk.END)
        self.shape_entry.insert(0, shape)
        self.size_entry.delete(0, tk.END)
        self.size_entry.insert(0, str(size))
        self.coordinate_system.plot_point(x, y, color=color, shape=shape, size=size)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateSystemApp(root)
    root.mainloop()
