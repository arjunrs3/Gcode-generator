import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def create_spiral(positions, diameter, total_height, coils, dt=0.1): 
    t = np.linspace(0, 2 * coils * np.pi, int(coils * 2 * np.pi / dt))
    x = diameter * np.sin(t)
    y = diameter * np.cos(t)
    z = (t / np.max(t)) * total_height
    for i in range (x.size): 
        positions.append([x[i], y[i], z[i]])

def create_circle(positions, diameter, z, no_of_circles, dt=0.01):
    t = np.linspace(0, 2 * no_of_circles * np.pi, int(no_of_circles * 2 * np.pi / dt))
    x = diameter * np.sin(t)
    y = diameter * np.cos(t)
    for i in range (x.size): 
        positions.append([x[i], y[i], z])

def create_zigzag(positions, width, height, cycles, z, dt=0.1):
    t = np.linspace(0, 1, int(cycles / dt))
    for i in range (cycles): 
        positions.append([width * i, 0, z])
        positions.append([width * i, height, z])
        positions.append([width * i + width/2, height, z])
        positions.append([width * i + width/2, 0, z])

def write_position(positions):
    with open("gcode.gcode", "w") as f:
        f.write("G91\n")
        f.write("G16 X Y Z\n")
        f.write("F 3\n")
        for x, y, z in positions:
            f.write(f"G1 X{x} Y{y} Z{z}\n")

def clear_gcode():
    open("gcode.gcode", "w").close()

def plot_curve(positions): 
    positions = np.array(positions)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])
    ax.set_aspect("equal")
    plt.show()

positions = []
create_zigzag(positions, 10, 10, 4, 0)
clear_gcode()
write_position(positions)
plot_curve(positions)


