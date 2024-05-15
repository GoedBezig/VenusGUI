import tkinter as tk
import math

class CoordinateSystem(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin

    def plot_point(self, x, y, color="red", shape="circle", size=2):
        scaled_x = self.origin[0] + x
        scaled_y = self.origin[1] - y
        if shape == "circle":
            self.create_oval(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)
        elif shape == "hexagon":
            self.create_polygon(
                scaled_x - size, scaled_y - size / 2,
                scaled_x - size / 2, scaled_y - size,
                scaled_x + size / 2, scaled_y - size,
                scaled_x + size, scaled_y - size / 2,
                scaled_x + size / 2, scaled_y + size / 2,
                scaled_x - size / 2, scaled_y + size / 2,
                fill=color
            )
        elif shape == "square":
            self.create_rectangle(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)

class CoordinateSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coordinate System")

        self.coordinate_system = CoordinateSystem(master, width=400, height=400)
        self.coordinate_system.pack(side=tk.LEFT)

    def plot_point(self, x, y, color="red", shape="circle", size=2):
        self.coordinate_system.plot_point(x, y, color=color, shape=shape, size=size)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateSystemApp(root)
    
    # Example usage: plot a hexagon at coordinates (50, 50) with a blue color and larger size

    app.plot_point(50, 50, color="blue", shape="circle", size=10)

    root.mainloop()
