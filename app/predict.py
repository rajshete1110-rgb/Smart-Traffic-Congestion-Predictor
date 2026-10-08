import os
import joblib
import pandas as pd

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load model
model_path = os.path.join(BASE_DIR, "models", "traffic_rf_model.pkl")
model = joblib.load(model_path)

# Load feature names
feature_path = os.path.join(BASE_DIR, "models", "feature_names.pkl")
feature_names = joblib.load(feature_path)

print("✅ Model loaded successfully!")

# Create empty dataframe with ALL training features
sample = pd.DataFrame(0, index=[0], columns=feature_names)

# Fill example values
sample["temp"] = 280
sample["rain_1h"] = 0
sample["snow_1h"] = 0
sample["clouds_all"] = 90
sample["hour"] = 17
sample["month"] = 12
sample["is_weekend"] = 0
sample["rush_hour"] = 1

# Weather condition
sample["weather_Clear"] = 1

# Day of week
sample["day_Monday"] = 1

# Predict
prediction = model.predict(sample)

print("\n🚦 Predicted Congestion Level:", prediction[0])