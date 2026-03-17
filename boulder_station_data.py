import pandas as pd 
import matplotlib.pyplot as plt

from windrose import WindroseAxes


url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20260215.txt"

df = pd.read_fwf(url, header=[0, 1], skiprows=[2])

date_col = [c for c in df.columns if c[1] == "Date"][0]
time_col = [c for c in df.columns if c[1] == "Time"][0]

t = (
    df[time_col]
    .astype(str)
    .str.strip()
    .str.replace(r"a$", "AM", regex=True)
    .str.replace(r"p$", "PM", regex=True)
)

dt = pd.to_datetime(
    df[date_col].astype(str).str.strip() + " " + t,
    format="%m/%d/%y %I:%M%p",
    errors="coerce",
)

df = df.set_index(dt).drop(columns=[date_col, time_col])
df.index.name = "datetime"

df.columns = [
    "_".join([str(a).strip(), str(b).strip()]).replace(" ", "_").strip("_")
    for a, b in df.columns
]

df
print('done')

"""
Part 1
Create dataframe with wind speed and direction.
Part 2
Bin the data.
Direction bins (N, NE, E, etc.)
Speed bins (0 to 2, 2 to 4, etc.)
Part 3
Compute frequency table.
Part 4
Plot wind rose.
"""
# create a DataFrame with just Wind Speed and Direction
wind_data = pd.DataFrame({
    'speed': df["Hi_Speed"],
    'direction': df["Hi_Dir"]
})

# convert wind direction to degrees and add to the DataFrame
direction_mapping = {
    'N': 0,
    'NNE': 22.5,
    'NE': 45,
    'ENE': 67.5,
    'E': 90,
    'ESE': 112.5,
    'SE': 135,
    'SSE': 157.5,
    'S': 180, 
    'SSW': 202.5,
    'SW': 225,
    'WSW': 247.5,
    'W': 270, 
    'WNW': 292.5,
    'NW': 315,
    'NNW': 337.5
}

wind_data['direction_degrees'] = wind_data["direction"].map(direction_mapping)


"""
You have the number of times the wind blows in each direction.
Now you need to sort the wind from each direction into speed categories:
    0-5 mph
    6-10 mph
    11-15 mph
    16-20 mph
    20-25 mph
    25-30 mph

Uses the bins function in Pandas to sort the wind speed and frequency by direction
"""
speed_bins = [0,5,10,15,20,25,30]
speed_label = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30']

wind_data['speed_groups'] = pd.cut(wind_data['speed'], bins=speed_bins, labels=speed_label)

"""
For the wind rose plot:
    a) direction_mapping - 16 cardinal direction spokes
    b) speed_groups - wind speed categories
    c) create a frequency table that plots the frequency of the wind for each speed bin

create a table with the direction frequency and the speed bins
"""
# sort wind_data by wind direction
wind_data.sort_values(by='direction', ascending=True)

wind_freq = pd.crosstab(wind_data['direction_degrees'], wind_data['speed_groups'])

print (wind_freq)

"""
Use the Matplotlib windrose plot to graph the data. 
"""
direction = wind_data['direction_degrees']
speed = wind_data['speed']


ax = WindroseAxes.from_ax()
ax.bar(direction, speed, 
       bins = [0,5,10,15,20,25,30],
       normed = True, opening = 1, 
       edgecolor="black")
ax.set_legend(title="Wind Speed (mph)", loc = 'best')
ax.set_title("Feb. 15th, 2026 Windrose Diagram", fontsize = 16)

plt.savefig('windrose.png', dpi = 150, bbox_inches = 'tight')
plt.show()

print ("Figured saved to lab06_ATOC4815")







