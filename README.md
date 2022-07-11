# Predicting Customer Churn - Classification Project
        Project Goal
            The goal of this project is to use statistical analysis and models on the Telco database in order to figure out the drivers of churn. The goal of the analysis and model is to accurately predict if a customer will stop being customers of Telco. 

         Project Description
            The telecommunication business is extremely competitive. One way to secure revenue is to try to maximize the amount of customers staying with a company and to renew contracts with Telco. To acheive this, we will look at our customer database to try an pinpoint the cause of churn and identify ways to lower the company's overall churn ratio.  Previous work shown that higher monthly charges and shorter tenure tends to churn more than longer term contracts. In order to analyze monthly costs, I will be looking into our bundled services with phone and internet as well as other services such as streaming and security


Questions:
       
    Question 1: Does bundling of internet and telephone services mean customers are less likely to churn than just internet or just phone customers?

            Null Hypothesis - Customer who bundled internet and phone are less likely to churn.
            Alt Hypothesis - Customers who bundled are equal or more likely to churn.

    Question 2: How much more do bundled customers pay and to what effect does high monthly charges play into customer churn? Does monthly charges coincide with contract type?
            Null Hypothesis: Bundled customers pay less than or equal amount to non-bundled 
            Alt Hypothesis: Bundled customers pay more than non-bundled 

    Do customers who bundle streaming services tend to churn less than those without streaming services?
            Null Hypothesis: Streaming services churn less or equal amount as those without
            Alt Hypothesis: Streaming services churn more than customers without streaming

    Do customers with security suite bundles churn less than customers without security features?
            Null Hypothesis: Customers with security services churn less or equal amount as security features
            Alt Hypothesis: Customers with security services churn more than customers with security features

    





 Null Hypothesis - There is no difference between bundled monthly payments and churn  


## Incluce a data dictionary.
    customer_id: An alpha-number number used to identify customer

    gender: Labels customer male or female

    is_senior_citizen: Labels customer senior or not senior

    partner: Labels customer with or without partner

    dependents: Labels customer with or wihtout dependents

    contract_type: Month-to-month, 1-year, or 2-year contract

    payment_type: Electronic, Mailled Check, or Bank transfer payment

    monthly_charges: Amount of monthly charges

    total_charges: Amount of total charges

    churn: Yes/No rate at which customers leave company

    tenure: Number of months customer has been with company

    is_female: T/F whether female or not female

    has_churned: T/F whether churned or not churned

    has_phone: T/F whether has phone or does not have phone

    has_internet: T/F whether has internet or does not have internet

    has_phone_and_internet: T/F whether has phone and internet service or not

    start_date: Date when individual become customer with company

    phone_type: No phone service, one-line, two or more lines

    internet_type: No internet service, DSL, or fiber optic

## The plan
    1. Acquire the data from SQL by using an env file and an acquire.py file to pull all columns and rows from the SQL server into my notebook. 
    2. After acquire, I prepped and cleaned the data before feature engineering conditional columns to better help answer my questions.
    3. Within my telco_prep.py folder I have the function used to prep my data as well as a desrciption of the features I engineered to anser my question
    4. After feature engineering, I split the data into train, validate, and test, using the function inside my telco_prep.py file
    5. Explore the features engineered against churn rates 
    6. Preform statistical analysis when needed 
    7. Model and tune models to gain most accurate insights

 ## Key Takeaways   
    1. Telco has a churn of 27%. The baseline to test against my models will be 73% which would be the accuracy if I did we guessed that a customer would not churn for all customers.  


## Exploratory Analysis 


Question 1: Null Hypothesis - Customer who bundled internet and phone are less likely to churn.
            Alt Hypothesis - Customers who bundled are equal or more likely to churn.


 Question 2: Null Hypothesis - There is no difference between bundled monthly payments and churn  


 ## Summary          

