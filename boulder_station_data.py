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
Part 1: Create a DataFrame with wind speed and direction.
Part 2: Sort the wind speeds into categories and directions. 
Part 3: Create frequency table.
Part 4: Plot windrose diagram.
"""
# create a DataFrame with just Wind Speed and Direction
Wind_Data = pd.DataFrame({
    'speed': df["Hi_Speed"],
    'direction': df["Hi_Dir"]
})

# convert wind direction to degrees and add to the DataFrame
Direction_Mapping = {
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

Wind_Data['Direction_Degrees'] = Wind_Data["direction"].map(Direction_Mapping)


"""
Sort the wind from each direction into speed categories using pd.cut:
    0-5 mph
    6-10 mph
    11-15 mph
    16-20 mph
    20-25 mph
    25-30 mph

Uses the bins function in Pandas to sort the wind speed and frequency by direction
"""
Speed_Bins = [0,5,10,15,20,25,30]
Speed_Label = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30']

# append do the original DataFrame for easy access
Wind_Data['Speed_Groups'] = pd.cut(Wind_Data['speed'], bins=Speed_Bins, labels=Speed_Label)

"""
Frequency Table: 
 a. Sort values starting at 0 degrees (North). 
 b. Use pd.crosstab to create a table of the wind speed and direction frequency. 
"""
# sort wind_data by wind direction
Wind_Data.sort_values(by='direction', ascending=True)

# create a table with directions as rows and speeds bins as columns
Wind_Frequency = pd.crosstab(Wind_Data['Direction_Degrees'], Wind_Data['Speed_Groups'])

print (Wind_Frequency)

"""
Use the Matplotlib windrose plot to graph the data. 
"""
direction = Wind_Data['Direction_Degrees']
speed = Wind_Data['speed']


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







