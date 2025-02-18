# Brooklyn & Cambridge Zoning Analysis

This repository contains an analysis comparing zoning regulations between Brooklyn, NY and Cambridge, MA, with a focus on building heights and Floor Area Ratios (FAR).

## Interactive Visualizations

View the interactive visualizations at: [https://cormacsb.github.io/brooklyn-cambridge-zoning-analysis/](https://cormacsb.github.io/brooklyn-cambridge-zoning-analysis/)

### Interactive Maps
- [Brooklyn Zones by Height](./zoning_analysis/brooklyn_zones_by_height.html) - Interactive map showing Brooklyn's zoning districts colored by maximum allowed building height
- [Cambridge Zones by Height](./zoning_analysis/cambridge_zones_by_height.html) - Current Cambridge zoning districts with height limits
- [Cambridge Zones by Height (Reduced)](./zoning_analysis/cambridge_zones_by_height_reduced.html) - Alternative scenario with reduced height limits

### FAR Distribution Analysis
- [FAR Distribution by Area](./zoning_analysis/far_distribution_area.html) - Distribution of Floor Area Ratios weighted by land area
- [FAR Distribution by Population Capacity](./zoning_analysis/far_distribution_population.html) - Distribution of FARs weighted by potential population
- [Cumulative FAR Distribution by Area](./zoning_analysis/far_cumulative_area.html) - Cumulative distribution of FARs by land area
- [Cumulative FAR Distribution by Population Capacity](./zoning_analysis/far_cumulative_population.html) - Cumulative distribution of FARs by potential population
- [Combined FAR Comparison Plots](./zoning_analysis/far_comparison_plots.html) - All FAR analyses in a single dashboard

## Key Findings

1. Brooklyn has a wider range of FARs (0.5 to 10.0) compared to Cambridge (0.5 to 4.0)
2. Cambridge's zoning is more uniformly distributed, while Brooklyn shows more variation
3. Population capacity analysis reveals different patterns than pure area-based analysis
4. Height limits in Cambridge are generally lower than in comparable Brooklyn zones

## Repository Structure
```
.
├── index.html                  # Main landing page
├── README.md                   # This file
└── zoning_analysis/           # Analysis code and visualizations
    ├── zoning_comparison.py   # Main analysis script
    ├── cambridge_zone_heights.json  # Cambridge zoning data
    └── requirements.txt       # Python dependencies
```

## Setup and Dependencies

To run the analysis locally:

1. Clone this repository
2. Install the required Python packages:
   ```bash
   pip install -r zoning_analysis/requirements.txt
   ```
3. Run the analysis:
   ```bash
   python zoning_analysis/zoning_comparison.py
   ```

## Dependencies
- Python 3.x
- geopandas >= 0.13.2
- pandas >= 2.0.0
- folium >= 0.14.0
- fiona >= 1.9.4
- plotly >= 5.13.0

## Data Sources
- NYC PLUTO Database for Brooklyn zoning information
- City of Cambridge GIS data for Cambridge zoning districts
- Municipal zoning codes for height and FAR regulations
