
import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
# xlrd is installed

df1_GDP = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
df2_Life_Exp = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\life_expectancy_years.xlsx")
df3_pop = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\population_total.xlsx")

print (df2_Life_Exp.index.values)
print (df2_Life_Exp.shape)





if df2_Life_Exp.isnull().values.any() == True:
		df2 = df2_Life_Exp.dropna()                      #Nan data is drop however, index are not fixed
		df2 = df2.reset_index(drop = True)               # fix index using the data that you dropped NaN
else:
	print ("Data does not have NaN")


print (df2.index.values)
print (df2.shape)

def df_dropnan_fix_index (data1):
	if data1.isnull().values.any() == True:
		print ('Values with Missing Data are: ', data1.isnull().sum(axis = 1)) # .sum (axis = 1)= give you the rows
		df1 = data1.dropna()
		df1 = df1.reset_index (drop = True)
		return df1 
	else:
		print ("Data does not have NaN")
		return data1 

df_dropnan_fix_index (df2_Life_Exp)	

data2 = df_dropnan_fix_index (df2_Life_Exp)	
print (data2.shape)
	

# if data2.isnull().values.any() == True:
# 		df2 = data2.dropna()
# 		df2 = df2.reset_index (drop = True)
# 	else:
# 		Print ('Data does not have NaN')
# 		data2 = data2




	

                               
	
	
# df1_GDP = df1_GDP.dropna()     
# 	data1= [item for item in data1 if item in data2]
# 		return data1
# 	print('Data have NaN')
# else:
# 	df1_GDP.isnull().values.any() == False
# 	print ('Data does not have NaN')



# def match_df_pair(df1, df2):    # create a functions to get dataframe matching data now
#     """
#     :param df1:                   
#     :param df2:
#     :return:
#     """
#     match_values = match_list(list(df1.iloc[:, 0]), list(df2.iloc[:, 0]))   # get the data that is present in both list (: all rows,  from column "0")

#     print('len df1: ', len(df1.columns))
#     if len(df1.index) > len(df2.index):            # compare the length of the rows for each dataframe see which one is >
#         key = df1.keys()[0]                        #   data.keys() is a function that give you the name of the column in this case I want keys (name) of column '0'                                                   
#         df1 = df1[df1[key].isin(match_values)]     # create a new dataframe which only has the column (key) that is present in both data. use .isin (match_value)
#         return df1, df2                            # .isin () is a function that checks if the values from df1[df1[key] (its a list)
#     else:
#         key = df2.keys()[0]
#         df2 = df2[df2[key].isin(match_values)]     # df2[df2[key]] give you all the rows related to column 'key'
#         return df1, df2                            # return both df igual

# df1, df2 = match_df_pair(df1_GDP, df2_Life_Exp)     #use the function to create two dataframe variables
# # print(df1.shape)
# # print(df2.shape)



# #def data_NaN (data1, data):
# 	#if data.isnull()= True:











# #dictionary  'key':['list']
# data1= {'Column1': ['abc','def'], 'Column2':['ghi','jkl']}
# data2= {'Column1':['abc', 'de', 'hjg'], 'Column2':['ghi','jkl','you']}

# #convert dictionary to dataframe
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)



def match_list(data1, data2):                                           #Create a funtion to get the information located in both                                       
	if len(data1) > len(data2):
		data1= [item for item in data1 if item in data2]
		return data1
	else:
		data2 = [item for item in data2 if item in data1]
		return data2


# # test the function, the data is in the df and need to be converted into a list, using the : (all rows) and 0 (for the firt column)
# print()
# print('Rows that are the Same in the two list Column [0]')
# print(match_list(list(df1.iloc[:,0]), list(df2.iloc[:,0])))

# def match_df_pair (df1, df2):                                            #creating a function 
# 	"""
# 	Arguments: two datafarames
# 	Descrption: This fuction drops value keys that are not present in both data frames
# 	Return: Dataframe
# 	"""
# 	match_values= match_list(list(df1.iloc[:,0]), list(df2.iloc[:,0]))   #
# 	if len(df1.columns) > len (df2.columns)







