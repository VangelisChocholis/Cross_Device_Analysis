import pandas as pd


def clean(df):
    # 'Transaction Id' will be set to upper case
    # 'User Id' will be set to lower case.
    df['Transaction Id'] = df['Transaction Id'].str.upper()
    df['User Id'] = df['User Id'].str.lower()
    
    # get the indices of rows with missing Transaction Id
    miss_ind = df[df['Transaction Id'].isna()].index
    # assign the random IDs to the missing values
    df.loc[miss_ind, 'Transaction Id'] = [f'RANDOM{miss_id}' for miss_id in miss_ind]
    
    # combine 'Year' and 'Month into a 'Date' column
    df['Date'] = pd.to_datetime(df['Year'].astype('str') + '-' + df['Month'].astype('str'), format='%Y-%m')
    df = df.drop(columns=['Year', 'Month'])
    
    return df


def transform(df):
    '''
    We will define six audience types: one for each available device
    that includes users who use only that device, and two multi-device audiences 
    containing users who use multiple devices. The two multi-device segments will be 'web only' and 'web & android.'
    We have chosen these specific types in order to compare the performance between the website and app. Unfortunately, 
    we are unable to include 'ios' user data, which leaves only 'Android' data from  app.
    ''' 
    # we add an extra column indicating the type of audience for each users.
    # for single device users
    df['Audience Type'] = 'N/A'
    # group by 'User Id' and make a list of devices used for each user
    device_lists = (df
                    .groupby('User Id')['Device Category']
                    .apply(lambda x: x.unique().tolist())
                   )
    # we make a dictionary to map 'User Id' to 'Audience type'
    single_dev_map = {}
    for user, dev_list in device_lists.items():
        if len(dev_list) == 1:
            single_dev_map[user] = dev_list[0]
    # map
    df.loc[df['User Id'].isin(single_dev_map), 'Audience Type'] = df['User Id'].map(single_dev_map)
    
    # for multiple devices, we categorize them as either 'web only' or 'web & android'.
    # we use the 'Platform' column, which indicates whether the user is a 'web' or an 'app' (Android) user
    # we group by 'User Id' and make a list of platforms used for each user
    platform_lists = df.groupby('User Id')['Platform'].apply(lambda x: x.unique().tolist())
    # make a dictionary to map 'User Id' to 'Audience Type'
    mul_dev_map = {}
    for user, plat_list in platform_lists.items():
        if len(plat_list)==1 and plat_list[0]=='web':
            mul_dev_map[user] = 'web only'
        elif len(plat_list)>1:
            mul_dev_map[user] = 'web & android'
    # map
    df.loc[(df['Audience Type'] == 'N/A') & \
           (df['User Id'].isin(mul_dev_map)), 'Audience Type'] = df['User Id'].map(mul_dev_map)
    
    return df
    

    
