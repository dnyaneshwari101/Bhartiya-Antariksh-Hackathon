# geo_processor.py

import geopandas as gpd
import rasterio
from rasterio.mask import mask
import json
from shapely.geometry import mapping


def load_vector(file_path):
    """Load a vector file (e.g., .geojson, .shp)."""
    return gpd.read_file(file_path)


def buffer_vector(gdf, distance):
    """Create a buffer around features (in meters)."""
    gdf = gdf.to_crs(epsg=32643)  # Project to UTM Zone 43N for India
    gdf['geometry'] = gdf.buffer(distance)
    return gdf.to_crs(epsg=4326)


def clip_raster_with_vector(raster_path, vector_gdf, output_path):
    """Clip a raster using a vector boundary."""
    with rasterio.open(raster_path) as src:
        out_image, out_transform = mask(src, vector_gdf.geometry, crop=True)
        out_meta = src.meta.copy()

    out_meta.update({
        "driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        "transform": out_transform
    })

    with rasterio.open(output_path, "w", **out_meta) as dest:
        dest.write(out_image)
    return output_path


def calculate_flood_stats(clipped_raster_path):
    """Calculate total flooded pixels and area."""
    with rasterio.open(clipped_raster_path) as src:
        band = src.read(1)
        pixel_size = src.res[0] * src.res[1]
        flooded_pixels = (band > 0).sum()
        flooded_area_km2 = (flooded_pixels * pixel_size) / 1e6

    stats = {
        "flooded_pixels": int(flooded_pixels),
        "flooded_area_km2": round(flooded_area_km2, 2)
    }
    with open(clipped_raster_path.replace('.tif', '_stats.json'), 'w') as f:
        json.dump(stats, f, indent=2)
    return stats


# Example usage (to be replaced with actual paths during integration)
if __name__ == "__main__":
    boundary = load_vector("data/raw/chennai_boundary_sample.geojson")
    buffered = buffer_vector(boundary, 5000)
    clipped_flood_path = clip_raster_with_vector(
        "data/raw/flood_chennai_sample.tif",
        buffered,
        "data/processed/flood_clipped.tif"
    )
    stats = calculate_flood_stats(clipped_flood_path)
    print("Flood stats:", stats)
# This code is designed to process geographical data, specifically for clipping raster data with vector boundaries and calculating flood statistics.
# It uses libraries like geopandas and rasterio for handling geospatial data.
# The code includes functions to load vector data, create buffers, clip rasters, and calculate flood statistics.
# The example usage at the end demonstrates how to use these functions with sample data paths.