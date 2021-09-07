
"""
This python file includes the ETL pipeline for Extracting, 
Transforming, and Loading disaster response messages
in order to prepare them for being used in ML algorithm.

"""
import sys
import pandas as pd
from sqlalchemy import create_engine
def extract(messages_filepath,categories_filepath):

    """
    This function reads the messages and categories dataframes.
    Then, it merges them together.
    INPUTS:
    * Two files 
    OUTPUT:
    A combined data frame
    """
    messages=pd.read_csv(messages_filepath)
    categories=pd.read_csv(categories_filepath)
    df=messages.merge(categories,how='left',on='id')
    return df


def CleanAndTransform(df):
    '''
    This function:
    Splits the values in the categories column on the ;
    character so that each value becomes a separate column.
    Uses the first row of categories dataframe to create column names
    for the categories data.
    Rename columns of categories with new column names.

    '''
    # create a dataframe of the 36 individual category columns
    categories_df=df['categories'].str.split(';',expand=True)
    col=df['categories'].copy()
    col=col.str.split(';')

    # select the first row of the categories dataframe
    rows=col[0]
    # use this row to extract a list of new column names for categories.
    # one way is to apply a lambda function that takes everything 
    # up to the second to last character of each string with slicing
    column_names=[x[0:-2] for x in rows]
    cat_columns=pd.DataFrame(categories_df.values,columns=column_names)

    #Convert category values to just numbers 0 or 1.
    for column in cat_columns.columns:
        cat_columns[column]=cat_columns[column].str.replace(column+'-','').astype('int')

    # drop the original categories column from `df`
    df.drop('categories',axis=1,inplace=True)
    # concatenate the original dataframe with the new `categories` dataframe
    result = pd.concat([df, cat_columns], axis=1)
    #Remove duplicates.
    result.drop_duplicates(inplace=True)
    return result 
def save_data_to_db(df, database_filepath):
    """
    Save Data to SQLite Database Function
    
    Arguments:
        df -> Combined data containing messages and categories with categories cleaned up
        database_filename -> Path to SQLite destination database
    """
    
    engine = create_engine('sqlite:///'+ database_filepath)
    table_name = database_filepath.replace(".db","") + "_table"
    df.to_sql(table_name, engine, index=False, if_exists='replace')


def main():
    """
    Main function which will kick off the data processing functions. There are three primary actions taken by this function:
        1) Load Messages Data with Categories
        2) Clean Categories Data
        3) Save Data to SQLite Database
    """
    
    # Print the system arguments
    # print(sys.argv)
    
    # Execute the ETL pipeline if the count of arguments is matching to 4
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:] # Extract the parameters in relevant variable

        print('Loading messages data from {} ...\nLoading categories data from {} ...'
              .format(messages_filepath, categories_filepath))
        
        df = extract(messages_filepath, categories_filepath)

        print('Cleaning categories data ...')
        df = CleanAndTransform(df)
        
        print('Saving data to SQLite DB : {}'.format(database_filepath))
        save_data_to_db(df, database_filepath)
        
        print('Cleaned data has been saved to database!')
    
    else: # Print the help message so that user can execute the script with correct parameters
        print("Please provide the arguments correctly: \nSample Script Execution:\n\
> python process_data.py disaster_messages.csv disaster_categories.csv disaster_response_db.db \n\
Arguments Description: \n\
1) Path to the CSV file containing messages (e.g. disaster_messages.csv)\n\
2) Path to the CSV file containing categories (e.g. disaster_categories.csv)\n\
3) Path to SQLite destination database (e.g. disaster_response_db.db)")

if __name__ == '__main__':
    main()