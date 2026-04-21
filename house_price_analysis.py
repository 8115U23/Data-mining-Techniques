# House Price Analysis and Prediction - Updated for Your Dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load Dataset
df = pd.read_csv('house_prices.csv')

# Display first few rows
print("Dataset Preview:\n", df.head())

# Basic Info
print("\nDataset Info:")
print(df.info())

# Check Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# Fill Missing Values (simple method)
df = df.fillna(df.mean(numeric_only=True))

# Features and Target
features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']
target = 'price'

X = df[features]
y = df[target]

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("\nModel Evaluation:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# ----------- Visualization Section -----------

# Bar Plot - Average Price by Bedrooms
plt.figure(figsize=(8,5))
sns.barplot(x='bedrooms', y='price', data=df)
plt.title("Average House Price by Number of Bedrooms")
plt.show()

# Pie Chart - Stories Distribution
plt.figure(figsize=(5,5))
df['stories'].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("House Distribution by Stories")
plt.show()

# Scatter Plot - Area vs Price
plt.figure(figsize=(8,5))
sns.scatterplot(x='area', y='price', data=df)
plt.title("Area vs House Price")
plt.show()

# Heat Map - Correlation between features
plt.figure(figsize=(10,6))
sns.heatmap(df[features + [target]].corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Box Plot - Price by Bathrooms
plt.figure(figsize=(10,6))
sns.boxplot(data=df[features])
plt.title("Box Plot of Selected Features")
plt.xlabel("Features")
plt.ylabel("Value Range")
plt.show()



print("\n✅ Visualization Completed Successfully!")
