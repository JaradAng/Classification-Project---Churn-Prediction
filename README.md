# Predicting Customer Churn - Classification Project
        Project Goal
            The goal of this project is to use statistical analysis and models on the Telco database in order to figure out the drivers of churn. The goal of the analysis and model is to accurately predict if a customer will stop being customers of Telco. 

         Project Description
            The telecommunication business is extremely competitive. One way to secure revenue is to try to maximize the amount of customers staying with a company and to renew contracts with Telco. To acheive this, we will look at our customer database to try an pinpoint the cause of churn and identify ways to lower the company's overall churn ratio.  Previous work shown that higher monthly charges and shorter tenure tends to churn more than longer term contracts. In order to analyze monthly costs, I will be looking into our bundled services with phone and internet as well as other services such as streaming and security


Questions:
     Question 1: Do the customers who churn pay on average the same amount as those who do not churn?
            Null Hypothesis: Customers who churn pay on average less than or equal amount to non-churning customers 
            Alt Hypothesis: Customers who churn pay more than customer who do not churn   

      Question 2: Are customers with fiber optic more or less likely to churn?
            Null Hypothesis: Fiber Optic customers churn less than or equal amount to non-fiber optic customers 
            Alt Hypothesis: Fiber Optic customers pay more than non-fiber optic customers      

   Question 3: Are month to month customers more or less likely to churn?
            Null Hypothesis: Month to month customers churn an equal amount to contracted customers 
            Alt Hypothesis: Month to month customers churn differently than contracted customers      
   
    Question 4: Does bundling of internet and telephone services mean customers are less likely to churn than just internet or just phone customers?

            Null Hypothesis - Customer who bundled internet and phone are less likely to churn.
            Alt Hypothesis - Customers who bundled are equal or more likely to churn.

   
    Question 4: Do customers who bundle streaming services tend to churn less than those without streaming services?
            Null Hypothesis: Streaming services churn less or equal amount as those without
            Alt Hypothesis: Streaming services churn more than customers without streaming

    Question 5: Do customers with security suite bundles churn less than customers without security features?
            Null Hypothesis: Customers with security services churn less or equal amount as security features
            Alt Hypothesis: Customers with security services churn more than customers with security features

    


# Data Dictionary For Telco Churn

partner -- Yes or No -- Does the customer have a partner

dependents -- Yes or No -- Does the customer have dependents

tenure -- Length of time with company

phone_service -- Yes or No -- Does the customer have phone service

multiple_lines -- Yes or No -- Does the customer have multiple phone lines

online_security -- Yes or No -- Does the customer have online security

online_backup -- Yes or No -- Does the customer have online backup

device_protection -- Yes or No -- Does the customer have device protection

tech_support -- Yes or No -- Does the customer have tech support

streaming_tv -- Yes or No -- Does the customer have streaming tv

streaming_movies -- Yes or No -- Does the customer have streaming movies

paperless_billing -- Yes or No -- Does the customer have paperless billing

monthly_charges -- Amount of monthly charge for customer

total_charges -- chrages occured over time

churn -- if customer left company -- Yes or No

contract_type -- month to month, one year, two year 

payment_type -- mailed check, electronic check, credit card

internet_service_type -- Type of internet service customer has No Service, DSL, Fiber Optic

manual_pay -- If customer paid by electronic or mailed check 

Bundled -- 1 for cust has internet and phone

monthly_charge_groups -- monthly charges divided in 20% groups

total_charge_groups -- total charges divided into 10% groups

The encoded values replace yes with 1 and no with 0

bundled_monthly -- 1 for month to month contract and has internet and phone

## How to reproduce my results
 -   You will need an env.py file that contains the hostname, username and password of the mySQL database that contains the telco table. Store that env file locally in the repository.
 -   clone my repo (including the acquire.py and telco_prep.py) (confirm .gitignore is hiding your env.py file)
 -   libraries used are pandas, matplotlib, seaborn, numpy, sklearn.
 -   you should be able to run final_telco_churn

## The plan
    1. Acquire the data from SQL by using an env file and an acquire.py file to pull all columns and rows from the SQL server into my notebook. 

    2. After acquire, I prepped and cleaned the data before feature engineering conditional columns to better help answer my questions.
    
    3. Within the telco_prep.py folder I have the function used to prep my data as well as a desrciption of the features I engineered to answer my questions
    
    4. After feature engineering, I split the data into train, validate, and test, using the function inside the telco_prep.py file
    
    5. Explore the features engineered against churn rates through the use of charts and vizuals to look for key drivers of churn
    
    6. Preform statistical analysis when needed 
    
    7. Model and tune models to gain most accurate insights
    
    8. Deliver key findings and models 

## Exploratory Analysis 


Question 1: Null Hypothesis - Customer who bundled internet and phone are less likely to churn.
            Alt Hypothesis - Customers who bundled are equal or more likely to churn.


 ## Summary 
    1. Telco has a churn of 27%. The baseline to test against my models will be 73% which would be the accuracy if I did we guessed that a customer would not churn for all customers.  
    
    2. New Telco customers are more likely to churn than customers who have been with the company awhile. 
    
    3. Monthly charges have a positive correlation to churn rate. As the monthly charge increases so does the likelyhood of churn.
    
    4. The top factors for churn include month-to-month Contract, paying by electronic check, and having fiber optic internet







        

