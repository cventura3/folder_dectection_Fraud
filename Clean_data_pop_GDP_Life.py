import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
# test github change
# xlrd is installed


df1_GDP = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx")
df2_Life_Exp = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\life_expectancy_years.xlsx")
df3_pop = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\population_total.xlsx")
df4_country_continent = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\Income_Life_pop\Country_continent_by_Gapminder.xlsx", sheet_name= "country_continent")

# If you want to count the missing values in each column, try: df.isnull().sum() or df.isnull().sum(axis=0)
# On the other hand, you can count in each row (which is your question) by: df.isnull().sum(axis=1)
# get the number of missing data in each columns
df4_country_continent.isnull().sum(axis = 0)

#get the number of missing data in each index (rows)
print (df4_country_continent.isnull().sum(axis = 1))

#get total sum of all of the NaN in the data
df4_country_continent.isnull().sum().sum()


#get number of rows and columns for each df
def print_shape(a, b, c, d):
    print('GDP_income_per_person_GDPcapital       shape:   ', a.shape)
    print('Life_expectancy_years                  shape:   ', b.shape)
    print('Population_total                       shape:   ', c.shape)
    print('Country_continent                      shape:   ', d.shape)
    print()

def print_if_nan(a, b, c, d):
    print( 'GDP_income_per_person_GDPcapital     NaN:      ', a.isnull().values.any())
    print( 'Life_expectancy_years                NaN:      ', b.isnull().values.any())
    print( 'Population_total                     NaN:      ', c.isnull().values.any())
    print( 'Country_continent                    NaN:      ', d.isnull().values.any())
    print()

def print_count_Nan (a, b, c,d):
    print( 'GDP_income_per_person_GDPcapital     NaN:      ', a.isnull().sum(axis = 0))
    print( 'Life_expectancy_years                NaN:      ', b.isnull().sum(axis = 0))
    print( 'Population_total                     NaN:      ', c.isnull().sum(axis = 0))
    print( 'Country_continent                    NaN:      ', d.isnull().sum(axis = 0))
    print()

def print_head_info (a, b, c, d):
    print( 'GDP_income_per_person_GDPcapital     head:      ', a.head())
    print( 'Life_expectancy_years                head:      ', b.head())
    print( 'Population_total                     head:      ', c.head())
    print( 'Country_continent                    head:      ', d.head())
    print()
 
 #drop NaN only fix index if NaN is dropped
def print_drop_idx_info (a, b, c, d):
    print( 'GDP_income_per_person_GDPcapital     index and NaN:   ', df_dropnan_fix_index(a))
    print( 'Life_expectancy_years                index and NaN:   ', df_dropnan_fix_index(b))
    print( 'Population_total                     index and NaN:   ', df_dropnan_fix_index(c))
    print( 'Country_continent                    index and NaN:   ', df_dropnan_fix_index(c))
    print()

#the dataframe have empty cells (NaN). Lets delete empty cells. Lets get rid of the Missing Data!


def df_dropnan_fix_index (data1):
    if data1.isnull().values.any() == True:
        df1 = data1.dropna()
        df1 = df1.reset_index (drop = True)
        print ('NaN dropped and Index reset: Data Fixed')
        return df1

    else:
        print ("No NaN, No drop data, No reset index ")
        data1 = data1
        return data1

print_shape(df1_GDP, df2_Life_Exp, df3_pop, df4_country_continent)
print_if_nan(df1_GDP, df2_Life_Exp, df3_pop,df4_country_continent)
print_count_Nan (df1_GDP, df2_Life_Exp, df3_pop, df4_country_continent)
print_head_info (df1_GDP, df2_Life_Exp, df3_pop, df4_country_continent)
print_drop_idx_info(df1_GDP,df2_Life_Exp, df3_pop, df4_country_continent)

df1_GDP = df_dropnan_fix_index (df1_GDP)
df2_Life_Exp = df_dropnan_fix_index(df2_Life_Exp)
df3_pop = df_dropnan_fix_index (df3_pop)
df4_country_continent = df_dropnan_fix_index (df4_country_continent)

print_shape(df1_GDP, df2_Life_Exp, df3_pop, df4_country_continent)

# need the same rows for all the data. Create a function. tells you

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


#get the data that is equal in the dataframe (not modification have been done). Just tell the info that is the same
#Use list() to convert the series into list

print('Rows that are the same in GDP and Life Expectancy In the Column Country [0]')

keys_test = match_list(list(df1_GDP.iloc[:, 0]), list(df4_country_continent.iloc[:, 0]))      #use the new funtion match_list(data1, data2) to get the data present, test if the function is working
print(*keys_test, sep = ' ')                                                                          #in both of the dataframe

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

                                                   #print('len df1: ', len(df1.columns)) to print column info
    if len(df1.index) > len(df2.index):            # compare the length of the rows for each dataframe see which one is >
        key = df1.keys()[0]                        #   data.keys() is a function that give you the name of the column in this case I want keys (name) of column '0'                                                   
        df1 = df1[df1[key].isin(match_values)]     # create a new dataframe which only has the column (key) that is present in both data. use .isin (match_value)
        return df1, df2                            # .isin () is a function that checks if the values from df1[df1[key] (its a list)
    else:
        key = df2.keys()[0]
        df2 = df2[df2[key].isin(match_values)]     # df2[df2[key]] give you all the rows related to column 'key'
        return df1, df2                            # return both df igual

df1, df2 = match_df_pair(df1_GDP, df2_Life_Exp)    #use the function to create two dataframe variables
df2, df3 = match_df_pair(df2_Life_Exp, df3_pop)
df2, df4 = match_df_pair(df2_Life_Exp, df4_country_continent)

print(df1.shape)
print(df2.shape)
print(df3.shape)
print(df4.shape)

df2, df4

# df4 has less column in common with df1, df2, df3 and thus function match_df_pair does not work very well

def drop_mismatch (data1, data2):
    for item in list (data1.iloc[:, 0]):                  #test if there is mismatch information in the column 0 "country"
        if item not in list(data2.iloc[:, 0]):
            print('Mismatch: ', item)                     #data = data.drop([0,1,2], axis=0)
            print(data1[data1[data1.keys()[0]] == item].index[0]) #get the index loc of the mismatch information
            index = data1[data1[data1.keys()[0]] == item].index[0] #this funtion get the index values of mismatch
            data1 = data1.drop([index])

        else:
            print('Item Match')
    return data1


df1 = drop_mismatch(df1, df4)
df2 = drop_mismatch(df2, df4)
df3 = drop_mismatch(df3, df4)


print (df1)
print (df2)
print (df3)
print (df4)


#check is the rows are the same

if len(list(df1.iloc[:, 0])) == len(list(df2.iloc[:, 0])) and len(list(df2.iloc[:, 0])) == len(list(df3.iloc[:,0])) and len(list(df3.iloc[:,0])) == len(list(df4.iloc[:,0])):                                               #another test, test (==) if df1 (new df) column 0 and all rows : are equal to df2 (new data)
    print('They have the same countries')
else:
    print('They don\'t have the same countries')

# check the index values of each dataframe. The function match_df_pair does not fix for index
print(df1.index.values)
print(df2.index.values)
print(df3.index.values)
print(df4.index.values)

#after using fuctions match_df_par and drop_mismatch the index are all over the place
#check the index values of each dataframe. The function match_df_pair does not fix for index
for idx, item in enumerate(df1.index.values):
    if item != df2.index.values[idx] and item != df3.index.values[idx] and item != df4.index.values[idx]:
        print('different', item)
    else:
        print ('Same index values')



#I need to fix the index

df1 = df1.reset_index ( drop = True)  # drop equal true make it to drop the old index 
df2 = df2.reset_index ( drop = True)
df3 = df3.reset_index ( drop = True)
df4 = df4.reset_index (drop = True)

print_head_info (df1, df2, df3, df4)


#test again for the index

for idx, item in enumerate(df1.index.values):      #
    if item != df2.index.values[idx] and item != df3.index.values[idx] and item != df4.index.values [idx]:
        print('different', item)
    else:
        print ('Same Index', item)  #this show that the index are fixed
 

#create a new dataframe for 2020 data and country (column is string) and 2020 (is numerical)
# I want to create a new df from columns of the 4 old dataframe


df1_GDP_2020 = df1[['country']].copy()
df1_GDP_2020_year = df1[[2020]].copy ()
df2_Life_Exp_2020 = df2[[2020]].copy()
df3_pop_2020 = df3[[2020]].copy()
df4_country_continent_new = df4[['four_regions']].copy()

print('GDP Income    ',     df1_GDP_2020)
print ('Life Expentacy',    df2_Life_Exp_2020)
print ('Population    ',    df3_pop_2020)
print ('Continents',        df4_country_continent_new)



# #df.columns[df.columns.str.contains('Spannung')]
#df1_list_year = list (df1_GDP_2020_year.iloc[:,0])

#how to get the key loc of a column in your dataframe use index to get index location df1.index.get loc (1800)
#df1.columns.get_loc (1800), print (df1.columns.get_loc(1800))


df1_list = list(df1_GDP_2020_year.iloc[:, 0])
df2_list = list(df2_Life_Exp_2020.iloc[:, 0])
df3_list = list(df3_pop_2020.iloc[:, 0])
df4_list = list(df4_country_continent_new.iloc[:, 0])



#df1_GDP_2020['GDP_income_per_person_GDP_capital'] = df1_list
df1_GDP_2020['Continents'] = df4_list
df1_GDP_2020['GDP Capital 2020'] = df1_list
df1_GDP_2020['Life 2020'] = df2_list
df1_GDP_2020['Pop 2020'] = df3_list

final_df_GDP_life_PoP_cont = df1_GDP_2020

print(final_df_GDP_life_PoP_cont) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# the range the pop is really big compared to life expectancy and GDP. We have to normalize the data
# store pop as a numpy array
np_pop = np.array(final_df_GDP_life_PoP_cont['Pop 2020'].astype(float))
np_gdp = np.array(list(final_df_GDP_life_PoP_cont['GDP Capital 2020']))
np_life = np.array(final_df_GDP_life_PoP_cont['Life 2020'])


#Lets normalize the data
print(np_pop)
def normalize_data(x):
    min_x = min(x)
    max_x = max(x)
    z = np.array([(xi - min_x)/(max_x - min_x) for xi in x])  # the data in  will return a list data
    return z                                                  # list data does not multiply each element in the list


print(normalize_data(np_pop))



def color_list (df_series):
    color = []
    for item in df_series:
        if item == 'asia':
            color.append('red') 
        elif item == 'africa':
            color.append('yellow')
        elif item == 'europe':
            color.append('green')
        elif item == 'americas':
            color.append ('blue')
    return color

color = color_list (final_df_GDP_life_PoP_cont['Continents'])

print(color)







# create the scatter plot
plt.scatter(np_gdp, np_life, s=(normalize_data(np_pop) * 1500), alpha = 0.9, c = 'red') # in order to use S
plt.scatter(np_gdp, np_life, s=(normalize_data(np_pop) * 1500), alpha = 0.9, c = 'yellow')
plt.scatter(np_gdp, np_life, s=(normalize_data(np_pop) * 1500), alpha = 0.9, c = 'green')
plt.scatter(np_gdp, np_life, s=(normalize_data(np_pop) * 1500), alpha = 0.9, c = 'blue')
plt.scatter(np_gdp, np_life, s=(normalize_data(np_pop) * 1500), alpha = 0.9, c = color,
 edgecolor= 'k')                                                             # and multiply each element you need an np.array

#fit the x scale
plt.xscale('log')

#string

#add axis labels
plt.xlabel('GDP per Capital [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2020',fontsize = 25)

# add the legend
legend = plt.legend(('Asia','Africa','Europe', 'Americas'), 
    loc='lower right', title = 'Continents', fontsize= 'small', 
    fancybox = True, borderpad = 2)
frame = legend.get_frame()
frame.set_facecolor('#b4aeae')    #color of legend
frame.set_edgecolor('black')      #edge color of legend
frame.set_alpha(1)                #deals with transparency
legend.scatteroffsets = 4

# add text
#plt.text (6000, 70, 'India')
#plt.text (14000, 79, 'China')

print (df1_GDP_2020)


#label each point

for x, y, label,fsize in zip(np_gdp,np_life, df1_GDP_2020['country'],(normalize_data(np_pop)*20)) :

    

                                                 # this method is called for each point
    plt.annotate(label,                          # this is the text
                 (x,y),                          # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,20), # distance from text to points (x,y)
                 ha='center').set_fontsize(fsize) # horizontal alignment can be left, right or center












#Edit the ticks on the x axis
plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])
plt.grid (True)

#
plt.show()


#df1.GDP_2020.rename(columns = {'2020': 'GDP'}, inplace = True)
#df2.columns.get_loc("pear")
# print(list(df1_GDP_2020.iloc[:, 0]))
# print('\n', list(df2_Life_Exp_2020.iloc[:, 0]))



