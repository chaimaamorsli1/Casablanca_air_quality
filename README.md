
# 🌍 Casablanca Air Pollution Map (Sample Data)

## Project Overview

This project creates an interactive geographical map visualizing PM2.5 (fine particulate matter) pollution levels in various neighborhoods of Casablanca, Morocco. The map is generated using Python with the `pandas` library for data handling and `folium` for interactive mapping.

This project serves as a practical demonstration of creating web-based geographical visualizations from structured data.

## ⚠️ Important Note on Data

**The PM2.5 pollution levels used in this map are SAMPLE/DUMMY DATA and do not represent actual real-time or historical air quality measurements for Casablanca's neighborhoods.** The purpose of this project is to illustrate the mapping capabilities of `folium` and data handling with `pandas`, not to provide accurate environmental data.

## Features

* **Interactive Map:** Pan, zoom, and explore different areas of Casablanca.
* **Neighborhood Markers:** Each circle marker represents a specific neighborhood.
* **Pollution Level Popups:** Click on a marker to see the neighborhood name and its sample PM2.5 level.
* **Color-Coded Pollution:** Markers are colored based on sample PM2.5 levels for quick visual assessment:
    * **Green:** PM2.5 $\le$ 30 (simulated good air quality)
    * **Orange:** 30 < PM2.5 $\le$ 50 (simulated moderate air quality)
    * **Red:** PM2.5 > 50 (simulated poor air quality)
* **HTML Output:** The map is saved as a standalone HTML file, easily viewable in any web browser.

## Technologies Used

* **Python 3**
* **[Pandas](https://pandas.pydata.org/)**: For data manipulation and DataFrame creation.
* **[Folium](https://python-visualization.github.io/folium/latest/index.html)**: For creating interactive Leaflet maps.

## How to Run the Code

1.  **Clone the repository** (or download the code):
    ```bash
    git clone [https://github.com/](https://github.com/)<YOUR_GITHUB_USERNAME>/casablanca-air-quality-map.git
    cd casablanca-air-quality-map
    ```

2.  **Install the required libraries** (if you don't have them):
    ```bash
    pip install pandas folium
    ```

3.  **Run the Python script:**
    ```bash
    python casablanca_air_pollution_map.py
    ```
    (Make sure your Python script is named `casablanca_air_pollution_map.py`. If it's named something else, adjust this command.)

4.  **Open the generated map:**
    A file named `casablanca_air_pollution_map.html` will be created in the project directory. Open this file in your preferred web browser to view the interactive map.

## Future Enhancements (Ideas)

* Integrate with real-time air quality APIs (e.g., OpenAQ, local environmental agencies) to use actual data.
* Add historical data visualization with a time slider.
* Implement more advanced analysis or statistical insights.
* Include a legend on the map for the color-coding.
* Deploy as a web application (e.g., using Flask or Django).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
