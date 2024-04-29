def multi_period_table(*in_objs):
    """
    Concatenates multiple instances of a company (different periods) into a single DataFrame.

    Parameters:
    *in_objs (tuple): Variable number of company instances.

    Returns:
    DataFrame: A DataFrame containing the concatenated financial data from all provided company instances.
    """
    # initialze data frame
    df_multi_period = pd.DataFrame()
    
    # for every provided object append it 
    for in_obj in in_objs:
        # Concatenate the DataFrame generated from each instance using create_df method
        df_multi_period = pd.concat([df_multi_period, in_obj.create_df()], ignore_index=False)
        
    return df_multi_period
