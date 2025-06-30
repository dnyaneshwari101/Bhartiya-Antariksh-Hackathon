# Bhartiya-Antariksh-Hackathon
# 🌍 geo-cot-rag-web

Geospatial Processing Module for **ISRO BAH 2025** - Problem Statement 4: *"Chain-of-Thought-Based LLM System for Complex Spatial Tasks"*

This module is responsible for **geoprocessing, clipping, and visualization** of raster (e.g. flood, DEM) and vector data (e.g. boundary, buffers) based on user queries or test datasets.

---

## 📊 Features

* Clip raster datasets using vector AOI (buffered boundary)
* Generate statistics from clipped raster (e.g. flood pixel count)
* Create static `.png` maps and interactive `.html` maps using Folium
* Output formatted for LLM/CoT integration (`.json`, `.tif`, `.html`)

---

## 📂 Folder Structure

```
geo-cot-rag-web/
├── geo_processor.py           # Clipping + stats pipeline
├── map_renderer.py            # PNG + Folium map rendering
├── data/
│   ├── raw/                   # Input sample data
│   │   ├── chennai_boundary_sample.geojson
│   │   ├── flood_chennai_sample.tif
│   │   └── dem_chennai_sample.tif
│   └── processed/             # Output data
│       ├── flood_clipped.tif
│       ├── flood_clipped_stats.json
│       ├── flood_map.png
│       └── flood_map.html
```

---

## 🔧 How to Run

### 1. Install Requirements

```bash
pip install geopandas rasterio folium matplotlib
```

### 2. Run GIS Processor (Clips flood raster)

```bash
python geo_processor.py
```

Generates:

* `flood_clipped.tif`
* `flood_clipped_stats.json`

### 3. Render Maps

```bash
python map_renderer.py
```

Generates:

* `flood_map.png`
* `flood_map.html`

Open `flood_map.html` in a browser to view interactive results.

---

## 🧑‍💼 Author: Anjali Yadav

**Role:** GIS Processing & Map Rendering
**Responsibilities:**

* Data clipping and buffer logic
* DEM/raster stats
* Map visualization (PNG, Folium)

---

## 🏆 Contribution to Hackathon

This GIS module serves as the foundation for spatial reasoning in our LLM pipeline. It enables:

* Automatic preprocessing of satellite & geospatial layers
* Input-output flow to Chain-of-Thought agent
* Visualization for judges, users, or benchmark validation

---

## 🔗 Integration Notes

* Input/output paths standardized to `data/`
* Future support for elevation (DEM) stats, NDVI, suitability
* Easily integrable with `rag_retriever.py` or `llm_handler.py`

---

Let’s map intelligence 🌎 with AI 🧐!
