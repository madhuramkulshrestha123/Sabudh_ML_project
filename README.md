# Sabudh_ML_project
Project Details:
In the English Premier League, May - July represents a lull period due
to the lack of club football. What makes up for it, is the intense
transfer speculation that surrounds all major player transfers today.
An important part of negotiations is predicting the fair market price
for a player. You are tasked with predicting this Market Value of a
player using the data provided below

# Tasks:
1. Use Seaborn to investigate the data and present your
findings

Output: ![image](https://github.com/user-attachments/assets/2bec73bc-74c8-4d9e-aa55-31cdd65a9bcf)


2. Build models using all the algorithms above to predict
market_value

Output: ![image](https://github.com/user-attachments/assets/92ef6add-faee-405c-af1c-7fc8e1f0d6f2)


3. Tune the hyperparameters and build the most accurate
model

Output: ![image](https://github.com/user-attachments/assets/a8d5ec80-3a5d-4fc1-afb0-c508ec0c44f5)
Best Model: Random Forest with RMSE: 4.313628750987281


4. Use model selection approaches discussed in class to
choose the best model

Output: ![image](https://github.com/user-attachments/assets/f7f090d7-30a6-4dbd-ac08-bf4744bfe201)
Best Model Selected: Random Forest with RMSE: 4.350784190834247 and CV RMSE: 6.214217794145062


5. Implement a Genetic Algorithm for learning attribute
weights for the Nearest Neighbour Algorithm. Implement at
least one mechanism for maintaining Diversity within the
Population

Output:
Generation 1: Best RMSE = 4.4977
Generation 2: Best RMSE = 4.2276
Generation 3: Best RMSE = 4.1257
Generation 4: Best RMSE = 4.1111
.
.
.
Generation 49: Best RMSE = 3.6040
Generation 50: Best RMSE = 3.5438
Best feature weights: [0.5420401  0.84212524 0.85462206 0.95665407 0.34773926 0.22358317
 0.18671626 0.38860162 0.54629233 0.69795647 0.28669392 0.28681674]
Final Optimized KNN RMSE: 3.5438

6. Deploy your model as a RESTful Web Service 
![image](https://github.com/user-attachments/assets/8e6c19a7-23df-4bea-a1f5-a3b5b2397bea)
