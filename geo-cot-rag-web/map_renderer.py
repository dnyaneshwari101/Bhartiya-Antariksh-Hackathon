# map_renderer.py

import rasterio
import matplotlib.pyplot as plt
import geopandas as gpd
import folium
from rasterio.plot import show
import os


def render_static_map(raster_path, output_png):
    """Render a .tif raster as a PNG image using matplotlib."""
    with rasterio.open(raster_path) as src:
        fig, ax = plt.subplots(figsize=(8, 6))
        show(src, ax=ax, cmap='Blues')
        ax.set_title("Flood Zone Map")
        plt.savefig(output_png)
        plt.close()


def render_interactive_map(raster_path, vector_path=None, output_html="flood_map.html"):
    """Create an interactive map using folium."""
    with rasterio.open(raster_path) as src:
        bounds = src.bounds
        center_lat = (bounds.top + bounds.bottom) / 2
        center_lon = (bounds.left + bounds.right) / 2

        flood_image = src.read(1)

        m = folium.Map(location=[center_lat, center_lon], zoom_start=11)

        folium.raster_layers.ImageOverlay(
            image=flood_image,
            bounds=[[bounds.bottom, bounds.left], [bounds.top, bounds.right]],
            colormap=lambda x: (0, 0, 1, x),  # Blue color scale
            opacity=0.5,
            name='Flood Layer'
        ).add_to(m)

        # Add buffered vector layer if available
        if vector_path and os.path.exists(vector_path):
            gdf = gpd.read_file(vector_path)
            folium.GeoJson(gdf, name='Buffer Zone').add_to(m)

        folium.LayerControl().add_to(m)
        m.save(f"data/processed/{output_html}")


# Example usage (update paths as needed)
if __name__ == "__main__":
    render_static_map(
        raster_path="data/processed/flood_clipped.tif",
        output_png="data/processed/flood_map.png"
    )

    render_interactive_map(
        raster_path="data/processed/flood_clipped.tif",
        vector_path="data/processed/rivers_buffer.geojson",
        output_html="flood_map.html"
    )

    print("✅ Maps rendered successfully. Check the 'data/processed/' folder.")
# This code provides functions to render both static and interactive maps from raster data.
# It uses rasterio for reading raster files and matplotlib for static rendering,
# while folium is used for creating interactive maps with optional vector overlays.
# The example usage at the end demonstrates how to call these functions with specified file paths.