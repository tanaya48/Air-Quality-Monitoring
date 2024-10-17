# Air-Quality-Monitoring
This Air Quality Monitoring project analyzes and visualizes air quality data using Python. It includes data cleaning to handle missing values and employs various visualizations such as pie charts, box plots, scatter plots, and heat maps to uncover insights about ozone levels, solar radiation, wind speed, and temperature.

# Air Quality Monitoring Project

This project focuses on monitoring and analyzing air quality data using Python. The dataset used in this project contains key features such as ozone levels, solar radiation, wind speed, and temperature. The goal is to visualize and understand the patterns and correlations between these variables.

## Table of Contents
- [Dataset](#dataset)
- [Data Cleaning](#data-cleaning)
- [Visualizations](#visualizations)
  - [Pie Chart](#pie-chart)
  - [Box Plot](#box-plot)
  - [Scatter Plot](#scatter-plot)
  - [Heat Map](#heat-map)
- [Requirements](#requirements)
- [Usage](#usage)

## Dataset
The dataset used for this project includes air quality data, with columns like:
- `Ozone`: Ozone concentration
- `Solar.R`: Solar radiation
- `Wind`: Wind speed
- `Temp`: Temperature

## Data Cleaning
The dataset contains missing values, which were handled by filling the missing entries with the mean value of the respective columns.

## Visualizations

### Pie Chart
A pie chart displays the distribution of ozone levels categorized into different ranges (Very Low, Low, Moderate, High, Very High).

### Box Plot
Box plots provide insights into the distribution of wind speed and temperature.

### Scatter Plot
The scatter plot shows the relationship between ozone concentration and wind speed.

### Heat Map
A heat map is generated to display the correlation between the main variables: ozone, solar radiation, wind speed, and temperature.

## Requirements
To run this project, you'll need the following Python libraries:
- pandas
- matplotlib
- seaborn

Install the required libraries using the following command:
```bash
pip install pandas matplotlib seaborn
