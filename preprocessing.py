from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd


# Create Feature
def create_new_features(df_test):

# Ubah kategori 4 weathersit ke kategori 3
    df_test.loc[df_test['weathersit']==4, 'weathersit'] = 3


#Feature Engineering
#1. `day`, `week_of_year`, `month`, `quarter`, `year`

    df_test['dteday'] = pd.to_datetime(df_test['dteday'])

    #ekstrak day
    df_test['day'] = df_test['dteday'].dt.strftime("%A")
    
    #ekstrak week of year
    df_test['week_of_year'] = df_test['dteday'].dt.week

    # ekstrak bulan pada kolom `dteday`
    df_test['month'] = df_test['dteday'].dt.strftime("%m")
    df_test['month'] = df_test['month'].astype(str)
    df_test['month']

    # ekstrak tahun pada kolom `dteday`
    df_test['year'] = df_test['dteday'].dt.strftime("%Y")
    df_test['year']

    #quarter
    def quarter (year) :
        for month in df_test['month'].unique() :
            if month in ['01','02','03'] :
                df_test.loc[(df_test['year']==year) & (df_test['month']==month), 'quarter'] = f"{year}_Q1"
            elif month in ['04','05','06'] :
                df_test.loc[(df_test['year']==year) & (df_test['month']==month), 'quarter'] = f"{year}_Q2"
            elif month in ['07','08','09'] :
                df_test.loc[(df_test['year']==year) & (df_test['month']==month), 'quarter'] = f"{year}_Q3"
            elif month in ['10','11','12'] :
                df_test.loc[(df_test['year']==year) & (df_test['month']==month), 'quarter'] = f"{year}_Q4"

    quarter("2011")
    quarter("2012")
#2. kolom `day_type`
    df_test.loc[(df_test['day'].isin(['Saturday', 'Sunday'])) & (df_test['holiday']==0), "day_type"] = 'weekend'
    df_test.loc[(~df_test['day'].isin(['Saturday', 'Sunday'])) & (df_test['holiday']==0), "day_type"] = 'weekday'
    df_test.loc[(df_test['holiday']==1), "day_type"] = 'holiday'

#3. kolom `HourBin_registered` dan `HourBin_casual`

    #`HourBin_registered`
    df_test.loc[df_test['hr']==0, 'HourBin_registered'] = 0
    df_test.loc[df_test['hr']==1, 'HourBin_registered'] = 1
    df_test.loc[(df_test['hr']>=2) & (df_test['hr']<=4) , 'HourBin_registered'] = 2
    df_test.loc[df_test['hr']==5, 'HourBin_registered'] = 3
    df_test.loc[(df_test['hr']==6),'HourBin_registered'] = 4
    df_test.loc[(df_test['hr']>=7) & (df_test['hr']<=23) , 'HourBin_registered'] = 5

    #`HourBin_casual`
    df_test.loc[df_test['hr']==0, 'HourBin_casual'] = 0
    df_test.loc[df_test['hr']==1, 'HourBin_casual'] = 1
    df_test.loc[(df_test['hr']==2) | (df_test['hr']==3), 'HourBin_casual'] = 2
    df_test.loc[(df_test['hr']==4) | (df_test['hr']==5) , 'HourBin_casual'] = 3
    df_test.loc[df_test['hr']==6, 'HourBin_casual'] = 4
    df_test.loc[df_test['hr']==7, 'HourBin_casual'] = 5
    df_test.loc[(df_test['hr']==8) | (df_test['hr']==9) , 'HourBin_casual'] = 6
    df_test.loc[(df_test['hr']>=10) & (df_test['hr']<=20) , 'HourBin_casual'] = 7
    df_test.loc[(df_test['hr']==21) | (df_test['hr']==22) , 'HourBin_casual'] = 8
    df_test.loc[df_test['hr']==23, 'HourBin_casual'] = 9

#4. kolom `TempBin_registered` dan `TempBin_casual`

    #`TempBin_registered`
    df_test.loc[(df_test['temp']==0.02) | (df_test['temp']==1.00), 'TempBin_registered'] = 0
    df_test.loc[(df_test['temp']>0) & (df_test['temp']<=0.32), 'TempBin_registered'] = 1
    df_test.loc[(df_test['temp']>0.32) & (df_test['temp']<=0.46), 'TempBin_registered'] = 2
    df_test.loc[(df_test['temp']>0.46) & (df_test['temp']<=0.70), 'TempBin_registered'] = 3
    df_test.loc[(df_test['temp']>0.70) & (df_test['temp']< 1.0 ), 'TempBin_registered'] = 4

    #`TempBin_casual`
    df_test.loc[(df_test['temp']>0) & (df_test['temp']<=0.24), 'TempBin_casual'] = 0
    df_test.loc[(df_test['temp']>0.24) & (df_test['temp']<=0.34), 'TempBin_casual'] = 1
    df_test.loc[(df_test['temp']>0.34) & (df_test['temp']<=0.68), 'TempBin_casual'] = 2
    df_test.loc[(df_test['temp']>0.68), 'TempBin_casual'] = 3

#5. kolom `HumBin_registered` dan `HumBin_casual`

    #`HumBin_registered`
    df_test.loc[(df_test['hum']>=0) & (df_test['hum']<=0.51), 'HumBin_registered'] = 0
    df_test.loc[(df_test['hum']>=0.52) & (df_test['hum']<=0.63), 'HumBin_registered'] = 1
    df_test.loc[(df_test['hum']>=0.64) & (df_test['hum']<=0.83), 'HumBin_registered'] = 2
    df_test.loc[(df_test['hum']>=0.84) & (df_test['hum']<=1.00), 'HumBin_registered'] = 3

    #`HumBin_casual`
    df_test.loc[(df_test['hum']>=0) & (df_test['hum']<=0.43), 'HumBin_casual'] = 0
    df_test.loc[(df_test['hum']>=0.44) & (df_test['hum']<=0.63), 'HumBin_casual'] = 1
    df_test.loc[(df_test['hum']>=0.64) & (df_test['hum']<=0.74), 'HumBin_casual'] = 2
    df_test.loc[(df_test['hum']>=0.75) & (df_test['hum']<=0.84), 'HumBin_casual'] = 3
    df_test.loc[(df_test['hum']==0.85) | (df_test['hum']==0.86), 'HumBin_casual'] = 4
    df_test.loc[(df_test['hum']>=0.87) & (df_test['hum']<=0.97), 'HumBin_casual'] = 5
    df_test.loc[(df_test['hum']>=0.98) & (df_test['hum']<=1.00), 'HumBin_casual'] = 6

#6. kolom vapour_pressure``

    df_temp = df_test.copy()
    df_temp = df_test[['temp', 'atemp', 'hum', 'registered', 'casual']]

    #ubah ke celcius
    df_temp['temp_celcius'] = df_temp['temp']*(39+8) - 8
    df_temp['atemp_celcius'] = df_temp['atemp']*(50+16) - 16

    #rumus vapur_pressure, lalu assign nilainya
    df_temp['vapour_pressure'] = df_temp['hum']*6.105*(np.exp((17.27*df_temp['temp_celcius'])/(237.7+df_temp['temp_celcius'])))
    df_test['vapour_pressure'] = df_temp['vapour_pressure']


#7. cluster
    def cluster(df_test):

        #kolom numeric
        num_cols = ['hr', 'hum', 'weathersit', 'temp']
        df_cluster = df_test[num_cols]

        #kolom kategori
        label_enc = LabelEncoder()
        cat_cols = ['day', 'month', 'year', 'quarter', 'day_type']

        for col in cat_cols: 
            df_cluster[col] = label_enc.fit_transform(df_test[col])

        #Fit transform model kmeans clustering
        km = KMeans(n_clusters=5, max_iter=200, n_init=10)
        km = km.fit(df_cluster)
        labels=km.labels_
        df_cluster.loc[:, 'cluster_kmeans'] = labels

        #assign nilai nya ke daframe utama
        df_test['cluster'] = df_cluster['cluster_kmeans']

        return df_test
    
    final_df_test = cluster(df_test)

    #drop kolom yang tidak diperlukan
    final_df_test = final_df_test.drop(['dteday', 'holiday'], axis=1)

    return final_df_test


