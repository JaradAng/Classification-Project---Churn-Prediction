import pandas as pd
import numpy as np
import os
import env

def get_db_url(dbname, username=env.user, hostname=env.host, passw=env.password):
    url = f'mysql+pymysql://{username}:{passw}@{hostname}/{dbname}'
    return url

url = get_db_url('titanic_db', env.user, env.host, env.password)

def new_titanic_data():
    return pd.read_sql('select * from passengers', url)

def get_titanic_data():
    filename = "titanic.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        titanic_df = new_titanic_data()

        # Write that dataframe to disk for later. Called "caching" the data for later.
        titanic_df.to_csv(filename)

        # Return the dataframe to the calling code
        return titanic_df  


def get_iris_data():
    filename = "iris.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        iris_df = pd.read_sql('SELECT * FROM measurements join species using (species_id)', get_db_url('iris_db'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        iris_df.to_csv(filename)

        # Return the dataframe to the calling code
        return iris_df  

def get_telco_data():
    filename = "telco_churn.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        telco_churn_df = pd.read_sql('''select * from customers
                                        join contract_types using (contract_type_id)
                                        join payment_types using (payment_type_id)
                                        join internet_service_types using (internet_service_type_id)''', get_db_url('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        telco_churn_df.to_csv(filename)

        # Return the dataframe to the calling code
        return telco_churn_df  