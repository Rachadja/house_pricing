import pandas as pd

def format_data(data):
    """
    Description:
    This function changes column names to lowercase and replaces spaces with underscores. It makes unique values that are written differently.

    Parameters:
    data: A DataFrame

    Returns:
    A cleaned DataFrame
    """
    # Writing the columns names in lowercase, and replacing any space in the names with _
    data = data.rename(columns=lambda x: x.lower().replace(' ', '_'))
    
    # Making unique values that have been written diffrentely 
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col] = data[col].str.lower()
    
            
    return data               