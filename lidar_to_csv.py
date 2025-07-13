import laspy
import pandas as pd

def las_to_csv(las_path, csv_path):
    las = laspy.read(las_path)
    df = pd.DataFrame({
        'X': las.x,
        'Y': las.y,
        'Z': las.z,
        'Intensity': las.intensity,
        'Classification': las.classification
    })
    df.to_csv(csv_path, index=False)
    print(f"Saved to {csv_path}")

if __name__ == "__main__":
    las_to_csv("data/processed/ground_filtered.las", "data/processed/ground_points.csv")
