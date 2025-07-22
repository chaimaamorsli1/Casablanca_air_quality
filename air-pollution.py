import pandas as pd
import folium

# Sample data: Casablanca neighborhoods and PM2.5 pollution levels
data = {
    'Location': ['Maarif', 'Ain Diab', 'Derb Sultan', 'Hay Mohammadi', 'Sidi Moumen'],
    'Latitude': [33.5865, 33.5926, 33.6011, 33.5967, 33.6117],
    'Longitude': [-7.6323, -7.6613, -7.6370, -7.5914, -7.5624],
    'PM2.5': [35, 50, 28, 65, 40]
}

df = pd.DataFrame(data)

# Create base map centered on Casablanca
m = folium.Map(location=[33.59, -7.63], zoom_start=12)

# Function to pick color based on pollution level
def color_picker(pm25):
    if pm25 <= 30:
        return 'green'
    elif pm25 <= 50:
        return 'orange'
    else:
        return 'red'

# Add circle markers
for idx, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=10,
        popup=f"{row['Location']} - PM2.5: {row['PM2.5']}",
        color=color_picker(row['PM2.5']),
        fill=True,
        fill_color=color_picker(row['PM2.5'])
    ).add_to(m)

# Save map as HTML file
m.save('casablanca_air_pollution_map.html')

print("Map created! Open 'casablanca_air_pollution_map.html' in your browser.")
