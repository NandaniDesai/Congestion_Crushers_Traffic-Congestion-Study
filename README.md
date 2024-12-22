y# Congestion Crushers- Traffic Congestion Study

## Group Members

- Nandani Desai - KU2407U144
- Manthan Bhambhani - KU2407U130
- Hely Modi - KU2407U073
- Riya Singh - KU2407U183
- Rudra Desai - KU2407U186

## Objective Of The Project

The primary objective is to analyze and visualize traffic patterns based on various factors, including rush hours, weather conditions, holidays, temperature, and cloud coverage. The project aims to provide insights into congestion trends to aid in better traffic management and planning.

## Tools And Libraries Used

- Python: For data manipulation, analysis, and visualization.
- Matplotlib: To create detailed and interactive graphs embedded into the UI.
- Tkinter: For building a graphical user interface (GUI) for user interaction.
- Pandas: For data cleaning, transformation, and aggregation.
  
## Data Source

- Synthetic Dataset: A dataset resembling real-world traffic data, including columns like traffic_volume, weather_main, holiday, temp, and clouds_all.
- Assumed Source: Authentic dataset generated using GPS data for simulating public traffic records and weather conditions.

## Execution Steps

1. **Install Required Libraries**: Ensure Pandas, Matplotlib, and Tkinter are installed.
2. **Load the Dataset**: Ensure the dataset (traffic.csv) is placed in the same directory as the script.
3. **Run the Script**: Execute the Python script.
4. **Interact with the UI**:
   - Click on the buttons to display corresponding traffic analysis graphs.
   - Graphs for rush hour, holidays, weather, temperature, and cloud coverage can be viewed dynamically.
5. **Optional**: Customize or save cleaned data using embedded options.

## Summary of Results

 - Traffic is significantly higher during rush hours compared to non-rush hours.
 - Non-holiday traffic volumes exceed holiday traffic volumes, except for some special occasions.
 - Weather conditions like cloudy and rainy days lead to increased congestion, while clear days see smoother traffic flow.
 - Traffic volume increases in moderate temperatures and decreases in extreme cold or hot conditions.


## Challenges Faced

 - Handling missing data effectively without compromising insights.
 - Distinguishing between holiday and non-holiday traffic due to insufficient holiday data in the dataset.
 - Ensuring the UI dynamically scales graphs to fit various screen sizes.
 - Embedding responsive, interactive Matplotlib graphs into the Tkinter interface while maintaining performance.




