# lab06_ATOC4815

Assignment: Turn in a cool plot and code via a github link, you will be graded on how cool it is. Turn in the code also (that uses pandas.)

Goal: Use the wind data from the ATOC Weather Station to create a windrose plot. 

Pandas Usage: 
    a. Created a DataFrame to return only the wind speed and direction
    
    b. Used the mapping fucntion on Pandas to convert the wind direction from cardinal direction into degrees. Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map

    c. In order to sort the wind speeds into categories I used the .cut function to segment data into bins. Source: https://pandas.pydata.org/docs/reference/api/pandas.cut.html

    d. Used a .sort_values funtion to organize my DataFrame by direction. Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html

    e. Used the crosstab funtion to create a table of wind direction as the rows and the speed frequency as columns. Source: https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html

Windrose Plotting: 
Downloaded the matplotlib windrose module to plot the wind data on a polar diagram. Wind direction is shown by the angular position of each "petal" arond the circle, speed is shown by the color-coded band, and frequency is represented by the length of each petal. 

Final Output:
The code here should output a frequency table with the rows being wind direction and columns being speed categories with the output being the frequency of the wind mesurments from each direction and speed. As well as a wind rose diagram itself. 
