import laspy
import matplotlib.pyplot as plt

def plot_lidar_profile(las_path, axis='x', limit=50):
    print("Reading LAS file...")
    las = laspy.read(las_path)

    x = las.x
    y = las.y
    z = las.z

    if axis == 'x':
        idx = (y > y.mean() - limit) & (y < y.mean() + limit)
        plt.scatter(x[idx], z[idx], s=1, c='blue')
        plt.xlabel("X")
    else:
        idx = (x > x.mean() - limit) & (x < x.mean() + limit)
        plt.scatter(y[idx], z[idx], s=1, c='green')
        plt.xlabel("Y")

    plt.ylabel("Elevation (Z)")
    plt.title("LiDAR Profile View")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_lidar_profile("data/processed/ground_filtered.las", axis='x', limit=5)
