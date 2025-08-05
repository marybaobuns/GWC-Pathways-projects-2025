# This code is written in python
# The pandas library is used for data processing and to read data files
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

import mpl_toolkits.mplot3d as mplot3d

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

# If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

ax = plt.axes(projection = "3d")
# Add Step 1 code here:
country1BooleanList =  lwd["country_name"] == "Senegal"
country2BooleanList = lwd["country_name"] == "Indonesia"

country1Data = lwd.loc[country1BooleanList]
country2Data = lwd.loc[country2BooleanList]
print("In my project, I will be comparing Indonesia and Senegal based on two parameters- average household size, and average years of education for women. I am interested in seeing how these two factors correlate with each other- and whether the amount of education women recieve impact whether they choose to have children")

input("(press return to continue.)\n")

print("Senegal is a country located in West Africa, it is classified as a highly indebted poor country")
      
input("(press return to continue.)\n")
      
print("On the other hand, Indonesia is a newly industrialized country, with the 17th largest global economy by nominal GDP")

print("The graph echos the fact that Senegal and Indonesia are opposites in terms of economic development- In Senegal, the average household size is above 12 chilren, while in indonesia, most people have less than 6 children")

input ("(press return to continue)\n")

print ("It may be true that educated women are less likely to have children, as indonesia has a higher average years of education than Senegal. However, this difference may also be due to other factors, such as the cost of raising children in each country.")

ax.scatter(x="ED_educ_years_mean", y="HD_women_size_mean", z="year", data = country1Data, label="Senegal")
ax.scatter(x="ED_educ_years_mean", y="HD_women_size_mean", z="year", data = country2Data, label="Indonesia")
ax.set_xlabel("average years of education")
ax.set_ylabel("average household size")
ax.legend()
ax.show()


# 