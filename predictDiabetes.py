import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import schemas

# Load the dataset
dataset = pd.read_csv('diabetes.csv')  # Replace 'diabetes_dataset.csv' with your dataset

# Split the dataset into features and target variable
X = dataset.drop('Outcome', axis=1)  # Assuming 'diabetes' is the target column
y = dataset['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

async def PredictDiabetesHandle(t) -> str:
# User Details
    user_data = t
# Predict the diabetes risk for the user
    risk_percentage = model.predict_proba(user_data)[0][1] * 100
    risk_percentage_round = round(risk_percentage)
    print("Diabetes risk percentage:", risk_percentage_round)
    return {"unapproximated":risk_percentage,"approximated":risk_percentage_round}
