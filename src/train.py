import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv('data/insurance.csv')

# Split features and target
X = df.drop('expenses', axis=1)
y = df['expenses']

# Columns
categorical = ['sex', 'smoker', 'region']
numerical = ['age', 'bmi', 'children']

# Preprocessing
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'bmi', 'children']),
    ('cat', OneHotEncoder(), ['sex', 'smoker', 'region'])
])

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestRegressor())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Save model
pickle.dump(pipeline, open('model/model.pkl', 'wb'))

print("Model trained and saved successfully!")