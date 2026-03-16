import pandas as pd 
import matplotlib.pyplot as plt


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


""" find then frequency/tendency of each wind direction
    You can count the number of each value from a DataFrame using a .value_counts()
    df.value_counts(parameter)
"""
direction_count = (wind_data['direction_degrees'].value_counts())

print(direction_count)






