def create_far_comparison_plots(brooklyn_data, cambridge_data, cambridge_reduced_data):
    """Create interactive comparison plots for FAR statistics"""
    # Define responsive configuration
    responsive_config = {
        'responsive': True,
        'scrollZoom': True,
        'displayModeBar': True,
        'displaylogo': False
    }
    
    responsive_css = """
    <style>
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
        }
        .plotly-graph-div {
            width: 100%;
            height: 100%;
        }
    </style>
    """
    
    # Create figure with secondary y-axis
    fig = make_subplots(rows=2, cols=2, 
                        subplot_titles=('FAR Distribution by Area', 'FAR Distribution by Population Capacity',
                                      'Cumulative FAR Distribution by Area', 'Cumulative FAR Distribution by Population Capacity'))
    
    # [Rest of the plotting code remains the same until the save section]
    
    # Update layout for combined plot
    fig.update_layout(
        title_text="FAR Comparison: Brooklyn vs Cambridge",
        showlegend=True,
        autosize=True,
        margin=dict(t=100, b=50, l=50, r=50)
    )
    
    # Save plots with responsive settings
    fig.write_html("zoning_analysis/far_comparison_plots.html", 
                  include_plotlyjs=True, 
                  full_html=True, 
                  config=responsive_config,
                  include_mathjax='cdn',
                  full_html_with_css=responsive_css)
    
    print("FAR comparison plots saved as 'zoning_analysis/far_comparison_plots.html'")
    
    # Individual plots with responsive settings
    for fig_obj, filename in [
        (fig_area, "far_distribution_area.html"),
        (fig_pop, "far_distribution_population.html"),
        (fig_cum_area, "far_cumulative_area.html"),
        (fig_cum_pop, "far_cumulative_population.html")
    ]:
        fig_obj.update_layout(
            showlegend=True,
            autosize=True,
            margin=dict(t=100, b=50, l=50, r=50)
        )
        fig_obj.write_html(f"zoning_analysis/{filename}",
                          include_plotlyjs=True,
                          full_html=True,
                          config=responsive_config,
                          include_mathjax='cdn',
                          full_html_with_css=responsive_css) 