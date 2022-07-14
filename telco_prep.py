import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# import splitting and imputing functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# turn off pink boxes for demo
import warnings
warnings.filterwarnings("ignore")





def prep_telco_data(df):

    # Drop duplicate columns
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'Unnamed: 0', 'gender'])
       
    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Create new column for manual paying customers
    df['manual_pay'] = (df.payment_type.str.contains('check')) 
   
    # Turning total_charges into float 
    df['total_charges'] = df.total_charges.astype(float)
    
    # Encoding yes and no categories with 1 and 0 respectively
    df['manual_encoded'] = df.manual_pay.map({ True: 1, False: 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Creating dummies so its easier for alogorithm to work 
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=False)
    
    # Adding in dummies from above into the existing dataframe
    df = pd.concat([df, dummy_df], axis=1)

    # Dropping the coloumn for no internet service type and services require internet dropped if no internet
    f = df.drop(columns=['internet_service_type_None', 'streaming_movies_No internet service', 'streaming_tv_No internet service', 'online_backup_No internet service'])

    #Create a coloumn for those who bundle internet and phone service
    df['Bundled'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL'), 1 , 0)

     # Create a column for those with streaming services 
    df['streaming_bundle'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['internet_service_type'] == 'DSL') | (df['internet_service_type_Fiber optic'] == 1), 1 , 0)

    #Create Column for whose with full security and insurance suite 
    df['security_bundle'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['internet_service_type'] == 'DSL') | (df['internet_service_type_Fiber optic'] == 1), 1 , 0)


    # New column to break down monthly charges into 5 groups
    df['monthly_charge_groups'] = pd.qcut(df['monthly_charges'], [0, 0.20, 0.40, 0.60, 0.80, 1], labels=[21, 44, 70, 86, 103])

    # New column to break down total charges into 5 groups
    df['total_charge_groups'] = pd.qcut(df['total_charges'], [0, 0.1, 0.2, 0.30, 0.40, 0.5, 0.6, 0.7, 0.8, 0.9, 1], labels=['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'])

    #Create a coloumn for those who bundle internet and phone service who are month to month customers
    df['bundled_monthly'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL') & (df['contract_type_Two year'] == 0) & (df['contract_type_One year'] == 0 ), 1 , 0)


    
    return df
    

def split_telco(df):

    # split the data
    train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=123, 
                                            stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.2, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    return train, validate, test




## Function to look into the best recommendation strategy for the company moving forward by breaking down what goes into monthly charges.


def telco_rec(df):

    #Create Column for whose with full security and insurance suite with DSL
    df['security_suite_dsl'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['internet_service_type'] == 'DSL'), 1 , 0)

      #Create Column for whose with full security and insurance suite with Fiber Optic
    df['security_suite_fiber'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['internet_service_type_Fiber optic'] == 1), 1 , 0)

        #Create Column for whose with  security and insurance suite with month-to-month contract
    df['security_monthly'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['contract_type_Two year'] == 0) & (df['contract_type_One year'] == 0 ), 1 , 0)
    
    # Create column for those with streaming services with two year contract
    df['streaming_monthly'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['contract_type_Two year'] == 0) & (df['contract_type_One year'] == 0 ), 1 , 0)

    # Create a column for those with streaming services with one year contract
    df['streaming_one'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['contract_type_One year'] == 1), 1 , 0)

    # Create column for those with streaming services with two year contract
    df['streaming_two'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['contract_type_Two year'] == 1 ), 1 , 0)
    
    #Create Column for whose with  security and insurance suite with one year contract
    df['security_one'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['contract_type_One year'] == 1), 1 , 0)

    #Create Column for whose with  security and insurance suite with two year contract
    df['security_two'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['contract_type_Two year'] == 1 ), 1 , 0)


    #Create a coloumn for those who bundle internet and phone service with one year contracts
    df['bundled_one'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL') & (df['contract_type_Two year'] == 0) & (df['contract_type_One year'] == 1 ), 1 , 0)
     
     
    #Create a coloumn for those who bundle internet and phone service with two year contracts
    df['bundled_two'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL') & (df['contract_type_Two year'] == 1) & (df['contract_type_One year'] == 0 ), 1 , 0)
     
       #Create a coloumn for those who bundle internet and phone service
    df['only_dsl'] = np.where((df['phone_service_encoded'] == 0) & (df['internet_service_type_Fiber optic'] != 1) & (df['internet_service_type'] == 'DSL'), 1 , 0)

          #Create a coloumn for those who bundle internet and phone service
    df['only_fiber'] = np.where((df['phone_service_encoded'] == 0) & (df['internet_service_type_Fiber optic'] == 1), 1 , 0)

    # Create a column for those with streaming services with DSL
    df['streaming_dsl'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['internet_service_type'] == 'DSL'), 1 , 0)

    # Create column for those with streaming services and fiber
    df['streaming_fiber'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['internet_service_type'] == 'Fiber Optic'), 1 , 0)

    return df

## To make the csv file, I am recreating the original database except keeping customer ID as per instructions

def predict_telco_data(df):

    # Drop duplicate co
    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'Unnamed: 0', 'gender', 'senior_citizen'])
       
    # Drop null values stored as whitespace    
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    # Create new column for manual paying customers
    df['manual_pay'] = (df.payment_type.str.contains('check')) 
   
    # Turning total_charges into float 
    df['total_charges'] = df.total_charges.astype(float)
    
    # Encoding yes and no categories with 1 and 0 respectively
    df['manual_encoded'] = df.manual_pay.map({ True: 1, False: 0})
    df['partner_encoded'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents_encoded'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service_encoded'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn_encoded'] = df.churn.map({'Yes': 1, 'No': 0})
    
    # Creating dummies so its easier for alogorithm to work 
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=False)
    
    # Adding in dummies from above into the existing dataframe
    df = pd.concat([df, dummy_df], axis=1)

    # Dropping the coloumn for no internet service type and services require internet dropped if no internet
    f = df.drop(columns=['internet_service_type_None', 'streaming_movies_No internet service', 'streaming_tv_No internet service', 'online_backup_No internet service'])

    #Create a coloumn for those who bundle internet and phone service
    df['Bundled'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL'), 1 , 0)

     # Create a column for those with streaming services 
    df['streaming_bundle'] = np.where((df['streaming_tv_Yes'] == 1) | (df['streaming_movies_Yes'] == 1) & (df['internet_service_type'] == 'DSL') | (df['internet_service_type_Fiber optic'] == 1), 1 , 0)

    #Create Column for whose with full security and insurance suite 
    df['security_bundle'] = np.where((df['online_security_Yes'] == 1) | (df['online_backup_Yes'] == 1) | (df['tech_support_Yes'] == 1) & (df['internet_service_type'] == 'DSL') | (df['internet_service_type_Fiber optic'] == 1), 1 , 0)


    # New column to break down monthly charges into 5 groups
    df['monthly_charge_groups'] = pd.qcut(df['monthly_charges'], [0, 0.20, 0.40, 0.60, 0.80, 1], labels=[21, 44, 70, 86, 103])

    # New column to break down total charges into 5 groups
    df['total_charge_groups'] = pd.qcut(df['total_charges'], [0, 0.1, 0.2, 0.30, 0.40, 0.5, 0.6, 0.7, 0.8, 0.9, 1], labels=['0-10%', '10-20%', '20-30%', '30-40%', '40-50%', '50-60%', '60-70%', '70-80%', '80-90%', '90-100%'])

    #Create a coloumn for those who bundle internet and phone service who are month to month customers
    df['bundled_monthly'] = np.where((df['phone_service_encoded'] == 1) & (df['internet_service_type_Fiber optic'] == 1) | (df['internet_service_type'] == 'DSL') & (df['contract_type_Two year'] == 0) & (df['contract_type_One year'] == 0 ), 1 , 0)


 # New column to break down total charges into 5 groups
    df['tenure_bins'] = pd.qcut(df['tenure'], [0, 0.20, 0.40, 0.60, 0.80, 1], labels=[20, 40, 60, 80, 100])

    
    return df