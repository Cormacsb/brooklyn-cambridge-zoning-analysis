import geopandas as gpd
import pandas as pd
import folium
from folium import plugins
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
import numpy as np

def load_manhattan_data():
    """Load Manhattan zoning data from NYC PLUTO database"""
    # Load NYC boroughs shapefile
    nyc_boroughs = gpd.read_file('zoning_analysis/nyc_boroughs/nyc_boroughs.shp')
    
    # Filter for Manhattan (Borough code 1)
    manhattan = nyc_boroughs[nyc_boroughs['boro_code'] == 1]
    
    # Load zoning data for Manhattan
    manhattan_zoning = gpd.read_file('zoning.gdb', layer='zoning')
    manhattan_zoning = manhattan_zoning[manhattan_zoning.intersects(manhattan.unary_union)]
    
    return manhattan_zoning

def create_manhattan_height_map(manhattan_zoning):
    """Create an interactive map of Manhattan zoning colored by height limits"""
    # Calculate centroid for initial map view
    center_lat = manhattan_zoning.geometry.centroid.y.mean()
    center_lon = manhattan_zoning.geometry.centroid.x.mean()
    
    # Create base map
    m = folium.Map(location=[center_lat, center_lon],
                  zoom_start=12,
                  tiles='cartodbpositron')
    
    # Add zoning districts colored by height
    folium.Choropleth(
        geo_data=manhattan_zoning.__geo_interface__,
        name='Manhattan Zoning',
        data=manhattan_zoning,
        columns=['zone_dist', 'max_height'],
        key_on='feature.properties.zone_dist',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Maximum Height (ft)'
    ).add_to(m)
    
    # Add hover functionality
    style_function = lambda x: {'fillColor': '#ffffff', 
                              'color':'#000000', 
                              'fillOpacity': 0.1, 
                              'weight': 0.1}
    highlight_function = lambda x: {'fillColor': '#000000', 
                                  'color':'#000000', 
                                  'fillOpacity': 0.50, 
                                  'weight': 0.1}
    
    NIL = folium.features.GeoJson(
        manhattan_zoning,
        style_function=style_function,
        control=False,
        highlight_function=highlight_function,
        tooltip=folium.features.GeoJsonTooltip(
            fields=['zone_dist', 'max_height', 'max_far'],
            aliases=['Zone:', 'Max Height (ft):', 'Max FAR:'],
            style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
        )
    )
    m.add_child(NIL)
    m.keep_in_front(NIL)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Save map
    m.save('zoning_analysis/manhattan_zones_by_height.html')
    print("Manhattan zoning map saved as 'zoning_analysis/manhattan_zones_by_height.html'")

def calculate_manhattan_stats(manhattan_zoning):
    """Calculate zoning statistics for Manhattan"""
    stats = {
        'mean_far': manhattan_zoning['max_far'].mean(),
        'median_far': manhattan_zoning['max_far'].median(),
        'max_far': manhattan_zoning['max_far'].max(),
        'min_far': manhattan_zoning['max_far'].min(),
        'mean_height': manhattan_zoning['max_height'].mean(),
        'median_height': manhattan_zoning['max_height'].median(),
        'max_height': manhattan_zoning['max_height'].max(),
        'min_height': manhattan_zoning['max_height'].min(),
    }
    
    return stats

def create_manhattan_far_plots(manhattan_zoning):
    """Create FAR distribution plots for Manhattan"""
    # Create figure
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=('FAR Distribution', 'Cumulative FAR Distribution'))
    
    # FAR Distribution
    fig.add_trace(
        go.Histogram(x=manhattan_zoning['max_far'],
                    name='Manhattan',
                    nbinsx=30),
        row=1, col=1
    )
    
    # Cumulative FAR Distribution
    sorted_far = np.sort(manhattan_zoning['max_far'])
    cumulative = np.arange(1, len(sorted_far) + 1) / len(sorted_far)
    
    fig.add_trace(
        go.Scatter(x=sorted_far,
                  y=cumulative,
                  name='Manhattan',
                  mode='lines'),
        row=1, col=2
    )
    
    # Update layout
    fig.update_layout(
        title_text="Manhattan FAR Analysis",
        showlegend=True,
        height=600,
        width=1200
    )
    
    # Save plot
    fig.write_html('zoning_analysis/manhattan_far_analysis.html')
    print("Manhattan FAR analysis plots saved as 'zoning_analysis/manhattan_far_analysis.html'")

def main():
    # Load data
    manhattan_zoning = load_manhattan_data()
    
    # Create visualizations
    create_manhattan_height_map(manhattan_zoning)
    create_manhattan_far_plots(manhattan_zoning)
    
    # Calculate and print statistics
    stats = calculate_manhattan_stats(manhattan_zoning)
    print("\nManhattan Zoning Statistics:")
    print(f"Mean FAR: {stats['mean_far']:.2f}")
    print(f"Median FAR: {stats['median_far']:.2f}")
    print(f"FAR Range: {stats['min_far']:.2f} - {stats['max_far']:.2f}")
    print(f"Mean Height: {stats['mean_height']:.2f} ft")
    print(f"Median Height: {stats['median_height']:.2f} ft")
    print(f"Height Range: {stats['min_height']:.2f} - {stats['max_height']:.2f} ft")

if __name__ == "__main__":
    main() 