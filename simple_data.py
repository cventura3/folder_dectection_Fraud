import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
# xlrd is installed

df1_GDP = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
df2_Life_Exp = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\life_expectancy_years.xlsx")
df3_pop = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\population_total.xlsx")

#getinformation about the df
print('Information about Dataframe')
print()
print('GDP')
print(df1_GDP.info())
print()
print('Life Expectancy')
print(df2_Life_Exp.info())
print()
print('Population')
print(df3_pop.info())
print()

#get number of rows and columns for each df
print('Get the rows and Columns of each DataFrame')
print()
print('Population')
print(df3_pop.shape)
print()
print('Life Expectancy')
print(df2_Life_Exp.shape)
print()
print('GDP')
print(df1_GDP.shape)
print ()

#inspect the data using .head()

print('Inspect the Data')
print()
print('Population')
print(df3_pop.head())
print()
print('Life Expectancy')
print(df2_Life_Exp.head())
print()
print('GDP')
print(df1_GDP.head())
#the dataframe have empty cells. Lets delete empty cells. Lets get rid of the Missing Data!


#Now the dataframe have empty cells. Lets delete empty cells. Lets get rid of the Missing Data!

df1_GDP = df1_GDP.dropna()                  # new data with the drop NAN
df2_Life_Exp = df2_Life_Exp.dropna()

df1_GDP = df1_GDP.reset_index(drop = True)    #reset index  function. dropna() does not reset index
df2_Life_Exp = df2_Life_Exp.reset_index (drop = True)

print(df1_GDP.head())
print(df2_Life_Exp.head())





# df2 = df2.dropna()
# #df1 = df1.reset_index(drop = True)
#print(df2.head())

# def empty_data_delete(data1, data2): 
#     data1 = (item for data1

# need the same rows for all the data. Create a function.
def match_list(list1, list2):                                 #create a functions that get the same row information from two dataframe
    """
    :param list1: argument list 1
    :param list2: argument list 2
    :Description: This function takes two list and return one list with the values that are present in both list
    :return: list of data that are present in both input list
    """
    if len(list1) > len(list2):                                 #create a if loop that inspect the data and return the data that is present in both files
        list1 = [item for item in list1 if item in list2]       # create a 'new' list with item that are present in both data (list)
        return list1
    else:
        list2 = [item for item in list2 if item in list1]
        return list2

# the function of match_list only works with list
print('Get the type')
print(type(df2_Life_Exp.iloc[:, 0]))              # this data type is a series, it needs to be a list
print()

#get the data that is equal in the dataframe (not modification have been done). Just tell the info that is the same
#Use list() to convert the series into list

print('Rows that are the same in GDP and Life Expectancy In the Column Country [0]')

keys_test = match_list(list(df1_GDP.iloc[:, 0]), list(df2_Life_Exp.iloc[:, 0]))      #use the new funtion match_list(data1, data2) to get the data present, test if the function is working
print(keys_test)                                                                          #in both of the dataframe

#Modify dataframe using .drop to drop the data that is not present in both
#use docstring to use help()
print()

def match_df_pair(df1, df2):    # create a functions to get dataframe matching data now
    """
    :param df1:                   
    :param df2:
    :return:
    """
    match_values = match_list(list(df1.iloc[:, 0]), list(df2.iloc[:, 0]))   # get the data that is present in both list (: all rows,  from column "0")

    print('len df1: ', len(df1.columns))
    if len(df1.index) > len(df2.index):            # compare the length of the rows for each dataframe see which one is >
        key = df1.keys()[0]                        #   data.keys() is a function that give you the name of the column in this case I want keys (name) of column '0'                                                   
        df1 = df1[df1[key].isin(match_values)]     # create a new dataframe which only has the column (key) that is present in both data. use .isin (match_value)
        return df1, df2                            # .isin () is a function that checks if the values from df1[df1[key] (its a list)
    else:
        key = df2.keys()[0]
        df2 = df2[df2[key].isin(match_values)]     # df2[df2[key]] give you all the rows related to column 'key'
        return df1, df2                            # return both df igual

df1, df2 = match_df_pair(df1_GDP, df2_Life_Exp)     #use the function to create two dataframe variables
print(df1.shape)
print(df2.shape)

for item in list (df1.iloc[:, 0]):                  #test if there is mismatch information 
    if item not in list(df2.iloc[:, 0]):
        print('Mismatch: ', item)

# check is the rows are the same

if len(list(df1.iloc[:, 0])) == len(list(df2.iloc[:, 0])):  #another test, test (==) if df1 (new df) column 0 and all rows : are equal to df2 (new data)
    print('They have the same countries')
else:
    print('They don\'t have the same countries')

print()
# l1 = list(df1.iloc[:, 0])
# l2 = list(df2.iloc[:, 0])
# l1.sort()                                                 #sort the data in alphabetical order
# l2.sort()
# print(l1)
# print(l2)

print(df1.head())
print(df2.head())

#create a new dataframe for 2020 data and country (column is string) and 2020 (is numerical)
df1_GDP = df1.reset_index ()
df2_Life_Exp = df2.reset_index ()

df1_GDP_2020 = df1_GDP[['country', 2020]].copy()
df2_Life_Exp_2020 = df2_Life_Exp[['country', 2020]].copy()

#df1_GDP_2020.reset_index()

print(df1_GDP_2020.tail())
print(df2_Life_Exp_2020.tail())

print(list(df1_GDP_2020.iloc[:, 0]))
print('\n', list(df2_Life_Exp_2020.iloc[:, 0]))



print(df1_GDP_2020.index.values)
print(df2_Life_Exp_2020.index.values)


print(df1_GDP.index.values)
print(df2_Life_Exp.index.values)

#
# for idx, item in enumerate(df1_GDP_2020.index.values):
#     if item != df2_Life_Exp_2020.index.values[idx]:
#         print('different', item)






