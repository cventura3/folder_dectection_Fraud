
# need the same rows for all the data. Create a function.
def match_list(list1, list2):                                 #create a functions that get the same list information (the goal is to get row information from two dataframe)
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







##discard all data not present in the three df (the data is already break into three different dataframe).
# Cross reference files that overlap search parameters delete the rest
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


#one data

def df_dropnan_fix_index (data1):
    if data1.isnull().values.any() == True:
        df1 = data1.dropna()
        df1 = df1.reset_index (drop = True)

    else:
        print ("No NaN, No drop data, No reset index ")
        data1 = data1


df1 = df_dropnan_fix_index ()

#two dataframe

def df_dropnan_reset_idx (data1, data2):
    if data1.isnull().values.any() == True:
        df1 = data1.dropna()
        df1 = df1.reset_index (drop = True)
    
    if data2.isnull().values.any() == True:
        df2.dropna()
        df2.reset_index(drop=True)

    new_df1, new_df2 = match_df_pair(df1, df2)
    return new_df1, new_df2

  # use.sum()

  def drop_nan_data (data):
    if data.isnull().sum(axis = 0) > 5:
        data1 = data.drop(axis = 0)
    else:
        print ('Columns have less than 5 NaN or No NaN')
        data = data

    if data.isnull().sum(axis = 1) > 5:
        data1 = data.drop(axis = 1)
    else: 
        print ('Rows have less than 5 NaN or No NaN')
        data = data

    return data