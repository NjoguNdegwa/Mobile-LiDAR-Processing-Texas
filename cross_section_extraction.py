import laspy
import numpy as np
import matplotlib.pyplot as plt

def extract_cross_section(las_path, y_center, y_width):
    las = laspy.read(las_path)
    x = las.x
    y = las.y
    z = las.z

    idx = (y > y_center - y_width) & (y < y_center + y_width)
    x_slice = x[idx]
    z_slice = z[idx]

    plt.figure(figsize=(10, 4))
    plt.scatter(x_slice, z_slice, s=1, c='red')
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.title("LiDAR Cross Section")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    extract_cross_section("data/processed/ground_filtered.las", y_center=3100000, y_width=1)
