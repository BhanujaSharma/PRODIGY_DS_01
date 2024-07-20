import pandas as pd
import plotly.express as px

# Load the dataset (adjust the path as necessary)
url = r'C:\Users\Bhanuja\Desktop\BHANUJA\PROJECTS\API_SP.POP.TOTL_DS2_en_csv_v2_1098332\API_SP.POP.TOTL_DS2_en_csv_v2_1098332.csv'
df = pd.read_csv(url, skiprows=4)

# Extract all years available in the dataset
years = [str(year) for year in range(1960, 2021)]

# Select data for all years and drop NaN values
df_years = df[['Country Name'] + years].dropna()

# Melt the DataFrame to have 'Year' and 'Population' as variables
df_melted = df_years.melt(id_vars=['Country Name'], value_vars=years,
                          var_name='Year', value_name='Population')

# Create an empty list to store all figures
figures = []

# Define a custom color palette with darker shades
color_palette = [
    '#1f77b4',  # dark blue
    '#ff7f0e',  # dark orange
    '#2ca02c',  # dark green
r    '#d62728',  # dark red
    '#9467bd',  # dark purple
    '#8c564b',  # dark brown
    '#e377c2',  # dark pink
    '#7f7f7f',  # dark gray
    '#bcbd22',  # dark yellow
    '#17becf'   # dark cyan
]

# Plot bar charts for each country separately and append the figure to the list
for i, country in enumerate(df_melted['Country Name'].unique()):
    df_country = df_melted[df_melted['Country Name'] == country]
    
    fig = px.bar(df_country, x='Year', y='Population',
                 labels={'Population': 'Population', 'Year': 'Year'},
                 title=f'Population of {country} (1960-2020)',
                 color='Year', color_discrete_sequence=color_palette)
    
    # Update traces to increase bar width
    fig.update_traces(marker_line_width=0, width=0.6)  # Adjust width as needed
    
    # Update layout
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Population',
        barmode='group',  # To display bars for each year grouped by country
        height=600,
    )
    
    # Convert the plot to HTML div content and append to the list
    figures.append(fig.to_html(full_html=False, include_plotlyjs='cdn'))
    figures.append('<br><br>')  # Add space between plots

# Combine all figures into a single HTML file
html_content = '''
<html>
<head>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
'''

# Add all figures to the HTML content
for fig in figures:
    html_content += fig

html_content += '''
</body>
</html>
'''

# Write the HTML content to a file
html_filename = 'population_bars_by_country.html'
with open(html_filename, 'w') as f:
    f.write(html_content)

print(f'HTML file "{html_filename}" generated successfully.')
