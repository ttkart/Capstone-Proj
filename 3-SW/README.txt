Capstone Project - Group 3 

Authors - Karthika Thiruvallur, Qiaoying Zhang, Shivani Bhasin

Code Location:
Our final notebook to run is within the folder '3-SW', called 'DSC_288R_Group_3_Final_models.ipynb'


Instructions for running & compilation of code:
Step 1 - Download the following necessary libraries:

    import pandas as pd
    
    import numpy as np
    
    import seaborn as sns
    
    import matplotlib.pyplot as plt
    
    from sklearn.model_selection import train_test_split
    
    from sklearn.model_selection import RandomizedSearchCV,cross_val_score
    
    from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
     
Step 2 - Download our finalized and cleaned dataset called 'merge.csv' within the '3-SW' folder.

Step 3 - Our code is using google collab (in cell 2 & cell 3). Here is the code to read it locally:

     df = pd.read_csv('merge.csv')

     df.info()

Step 4 - After completing the above steps, begin to run the code from this cell 4 onwards. For reference, cell 4 states:
   
     X = df.loc[:, df.columns != 'Total_Mkt_Fare']
     y = df.Total_Mkt_Fare

     # make 30% test set and 70% training
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=21)

     # devide test into half to form validation set: 25% test, 25% valid, 50% train
     X_hold, X_valid, y_hold, y_valid = train_test_split(X_test, y_test, test_size=0.5,random_state=21)
     

Overall Research Project:
Predicting customer ticket prices for domestic flights based on departure cities vs arrival cities 

> We're studying how much it costs for people to fly from city to city within U.S.
    
> Our goal is to figure out why ticket prices vary based on the cities people are flying to and from.
    
> This research helps us predict how much domestic flight tickets cost, which is important for the airline industries.


Abstract:
The research aims to predict domestic flight ticket prices based on departure and arrival cities within the United States. This study addresses the variability in domestic ticket prices and its influencing factors. It employs hyperparameter tuning to optimize our chosen machine-learning regression models. These methods enhance the model performance and computational efficiency by exploring hyperparameter spaces effectively. Ultimately, our project contributions reflect valuable insights for predicting airline ticket costs, benefiting both the consumer and airline industries through the addition of crucial variables including and not limited to domestic air fuel costs, weather conditions, etc.


