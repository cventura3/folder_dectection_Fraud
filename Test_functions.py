import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
# xlrd is installed

df1_GDP = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
df2_Life_Exp = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\life_expectancy_years.xlsx")
df3_pop = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\population_total.xlsx")
df4_country_continent = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\Country_continent_by_Gapminder.xlsx", sheet_name= "country_continent")

for x, y in zip(xs,ys):

    label = "{:.2f}".format(y)

                                                 # this method is called for each point
    plt.annotate(label,                          # this is the text
                 (x,y),                          # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center







# if df4_country_continent.index.isnull().sum(axis = 0) > 5:
# 	print ('Columns')
	
# data1 = df4_country_continent.dropna( axis = 0)

# if df4_country_continent.isnull().sum(axis = 0).values.any() > 5:
# 	data1 = df4_country_continent.dropna(axis = 0)
# 	print ('Columns with more than 5 Nan were dropped')

# for idx, item in data:
# 	if item in 




# print (df4_country_continent.index.isnull().sum(axis = 0) > 5)





# def drop_nan_data (data):
#     if data.isnull().sum(axis = 0) > 5:
#         data1 = data.drop(axis = 0)
#         print ('Columns with more than 5 Nan were dropped')
#     else:
#         print ('Columns have less than 5 NaN or No NaN')
#         data = data

#     if data.isnull().sum(axis = 1) > 5:
#         data1 = data.drop(axis = 1)
#     else: 
#         print ('Rows have less than 5 NaN or No NaN')
#         data = data





#     return data