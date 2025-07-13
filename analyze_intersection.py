import pdal
import json

def run_pipeline(las_file, output_file):
    print("Running PDAL pipeline to filter LiDAR ground points...")

    pipeline_json = {
        "pipeline": [
            las_file,
            {
                "type": "filters.smrf",
                "scalar": 1.25,
                "slope": 0.15,
                "window": 16.0
            },
            {
                "type": "writers.las",
                "filename": output_file
            }
        ]
    }

    pipeline = pdal.Pipeline(json.dumps(pipeline_json))
    pipeline.execute()
    print("Filtered LAS saved to:", output_file)

if __name__ == "__main__":
    run_pipeline("data/raw_lidar/intersection.las", "data/processed_lidar/ground_filtered.las")
