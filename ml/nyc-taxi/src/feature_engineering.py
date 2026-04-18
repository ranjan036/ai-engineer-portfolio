import pandas as pd
import numpy as np

def clean_data(df):

    #drop all the rows with passenger count = 0
    df = df[df['passenger_count'] > 0]
    #drop all the rows with invalid lattitude and longitude

    valid_longitude_latitude = ( (df['dropoff_longitude'].between(-75,-73)) & (df['dropoff_latitude'].between(40,41)) &
                                (df['pickup_longitude'].between(-75,-73))& (df['pickup_latitude'].between(40,41)))


    df = df[valid_longitude_latitude]

    # Drop rows with duration>4 hrs, duration> 14400 sec , or keep rows with duration < 14400

    df = df[df['trip_duration'] < 14400]

    return df

def haversine_distance(lat1,long1,lat2,long2):
    lat1 = (np.pi/180)*lat1 
    long1 = (np.pi/180)*long1 
    lat2 = (np.pi/180)*lat2
    long2 = (np.pi/180)*long2
    delta_Lat = lat2 - lat1
    delta_long = long2 - long1
    
    a1 = np.sin(delta_Lat/2)
    a1 = a1**2
    a2 = np.cos(lat1) * np.cos(lat2)
    a3 = np.sin(delta_long/2)
    a3 = a3**2
    
    a = a1 + a2 * a3
    p1 = np.sqrt(a)
    p2 = np.sqrt(1-a)
    c = 2 * np.arctan2(p1,p2)

    d = 6371 *c
    return d


def create_feature(df):


    #convert object type to actual timestamp 
    df['dropoff_datetime'] = pd.to_datetime(df['dropoff_datetime']) 
    df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
    #pickup hour
    df['pickup_hour'] = df['pickup_datetime'].dt.hour
    #weekend information
    df['pickup_day_of_week'] = df['pickup_datetime'].dt.day_of_week
    df['is_weekend'] = df['pickup_day_of_week']>=5
    #trip distance 
    df['trip_distance'] = haversine_distance(df['pickup_latitude'],df['pickup_longitude'],df['dropoff_latitude'],df['dropoff_longitude'])

    # Droping unnecessary/duplicate feature
    df = df.drop(['dropoff_datetime','pickup_datetime','id', 'vendor_id'],axis = 1)

    return df


    