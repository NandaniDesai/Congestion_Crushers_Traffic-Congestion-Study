import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Button, Frame, Label, BOTH

# Load the data
data = pd.read_csv("./data/traffic.csv", na_values=[])

# Data Cleaning
data.drop_duplicates(inplace=True)
data['holiday'] = data['holiday'].fillna('Non-Holiday')  # Fill any NaN in the holiday column
data['holiday'] = data['holiday'].replace('None', 'Non-Holiday') # Replace 'None' with 'Non-Holiday' for clarity
data['temp'] = data['temp'] - 273.15  # Convert temperature to Celsius
if data.isnull().sum().any():
    data = data.ffill()  # Forward fill for missing values

# Save the cleaned dataset
data.to_csv("./data/cleaned_traffic.csv", index=False)
data.to_csv("./output/cleaned_traffic.csv", index=False)

# Function to create a graph and embed it in the Tkinter window
def plot_graph(graph_function):
    # Clear the frame for the new graph
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Create the figure
    fig = graph_function()

    # Embed the Matplotlib figure in the Tkinter frame
    canvas = FigureCanvasTkAgg(fig, graph_frame)
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)
    canvas.draw()

# Graph Functions
def rush_hour_graph():
    rush_hour_traffic = data.groupby('Rush Hour')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    palette = plt.colormaps['tab10']
    rush_hour_traffic.plot(kind='bar', ax=ax, color=palette([2, 3]))
    ax.set_title('Traffic Volume During Rush Hour')
    ax.set_xlabel('Rush Hour (0: No, 1: Yes)')
    ax.set_ylabel('Average Traffic Volume')
    ax.set_xticks([0, 1], labels=['No', 'Yes'])
    plt.tight_layout()
    return fig

def temperature_graph():
    sorted_data = data.sort_values(by='temp')
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(data['temp'], data['traffic_volume'], alpha=0.1, color='orange', label='Data Points')
    ax.plot(sorted_data['temp'], sorted_data['traffic_volume'].rolling(window=100).mean(), color='red', linewidth=1, label='Trend Line')
    ax.set_title('Temperature vs. Traffic Volume with Trend Line')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Traffic Volume')
    ax.legend()
    plt.tight_layout()
    return fig

def weather_graph():
    weather_traffic = data.groupby('weather_main')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    palette = plt.colormaps['tab10']
    weather_traffic.plot(kind='bar', ax=ax, color=palette(range(len(weather_traffic))))
    ax.set_title('Traffic Volume Across Different Weather Conditions')
    ax.set_xlabel('Weather Condition')
    ax.set_ylabel('Traffic Volume')
    ax.set_xticks(range(len(weather_traffic)), labels=weather_traffic.index, rotation=45, ha='right')
    plt.tight_layout()
    return fig

def cloud_coverage_graph():
    cloud_traffic = data.groupby('clouds_all')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    cloud_traffic.plot(kind='line', ax=ax, marker='o', color='green')
    ax.set_title('Cloud Coverage vs. Average Traffic Volume')
    ax.set_xlabel('Cloud Coverage (%)')
    ax.set_ylabel('Average Traffic Volume')
    ax.grid(True)
    plt.tight_layout()
    return fig

def holiday_graph():
    holiday_traffic = data.groupby('holiday')['traffic_volume'].mean()
    fig, ax = plt.subplots(figsize=(6, 4))
    palette = plt.colormaps['tab10']
    holiday_traffic.plot(kind='bar', ax=ax, color=palette([0, 1]))
    ax.set_title('Traffic Volume on Holidays vs. Non-Holidays')
    ax.set_xlabel('Holiday')
    ax.set_ylabel('Average Traffic Volume')
    ax.set_xticks(range(len(holiday_traffic)), labels=holiday_traffic.index, rotation=45, ha='right')
    plt.tight_layout()
    return fig

# Tkinter Window
root = Tk()
root.title("Traffic Congestion Study")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry(f"{width}x{height}")  # Default window size

# Adding a background color
root.configure(bg="#f0f0f0")

# Button Frame
button_frame = Frame(root, bg="#f0f0f0", height=100)
button_frame.pack(fill=BOTH, side="top", padx=10, pady=10)

# Graph Frame
graph_frame = Frame(root, bg="#ffffff")
graph_frame.pack(fill=BOTH, expand=True, padx=0, pady=10)

# Buttons
Button(button_frame, border=2, bg='light grey', fg='black', cursor='hand2', text="Rush Hour Analysis", command=lambda: plot_graph(rush_hour_graph), width=20, font=("Helvetica", 12)).pack(side="left", padx=10)
Button(button_frame, border=2, bg='light grey', fg='black', cursor='hand2', text="Temperature vs Traffic", command=lambda: plot_graph(temperature_graph), width=20, font=("Helvetica", 12)).pack(side="left", padx=10)
Button(button_frame, border=2, bg='light grey', fg='black', cursor='hand2', text="Weather Conditions", command=lambda: plot_graph(weather_graph), width=20, font=("Helvetica", 12)).pack(side="left", padx=10)
Button(button_frame, border=2, bg='light grey', fg='black', cursor='hand2', text="Cloud Coverage", command=lambda: plot_graph(cloud_coverage_graph), width=20, font=("Helvetica", 12)).pack(side="left", padx=10)
Button(button_frame, border=2, bg='light grey', fg='black', cursor='hand2', text="Holiday Analysis", command=lambda: plot_graph(holiday_graph), width=20, font=("Helvetica", 12)).pack(side="left", padx=10)

root.mainloop()
