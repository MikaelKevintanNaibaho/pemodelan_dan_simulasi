import tkinter as tk
import math

class Speedometer(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=200, height=200)
        self.create_oval(20, 20, 180, 180, outline='black', width=2)  # Outer circle
        self.needle = self.create_line(100, 100, 190, 100, fill='red', width=2)  # Needle
        self.create_speed_labels()

    def create_speed_labels(self):
        cx, cy = 100, 100  # Center of the speedometer
        radius = 80  # Distance from center to labels
        label_angles = [30, 60, 90, 120, 150]  # Angles for speed labels

        for angle in label_angles:
            angle_rad = math.radians(angle)
            x_label = cx + radius * math.cos(angle_rad)
            y_label = cy - radius * math.sin(angle_rad)
            speed_value = int((180 - angle) * (120 / 180))  # Calculate speed value
            self.create_text(x_label, y_label, text=str(speed_value), font=("Arial", 10, "bold"))

    def update_speed(self, speed):
        angle = 180 - (180 * (speed / 120))  # Convert speed to angle (0 to 180 degrees) in quadrant 1 and 4
        self.rotate_needle(angle)

    def rotate_needle(self, angle):
        cx, cy = 100, 100  # Center of the speedometer
        angle_rad = math.radians(angle)
        x2_new = cx + 90 * math.cos(angle_rad)  # Needle length = 90
        y2_new = cy - 90 * math.sin(angle_rad)  # Negative sin because y-axis is inverted
        self.coords(self.needle, cx, cy, x2_new, y2_new)

if __name__ == "__main__":
    root = tk.Tk()
    speedometer = Speedometer(root)
    speedometer.pack()

    # Simulate speed changes
    speed_values = [0, 30, 60, 90, 120]
    speed_index = 0

    def update_speedometer():
        global speed_index
        speedometer.update_speed(speed_values[speed_index])
        speed_index = (speed_index + 1) % len(speed_values)
        root.after(1000, update_speedometer)

    update_speedometer()

    root.mainloop()
