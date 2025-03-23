import pickle
import numpy as np
from flask import Flask, request, jsonify

with open("optimized_knn.pkl", "rb") as file:
    model_data = pickle.load(file)

loaded_model = model_data["model"]
loaded_weights = model_data["weights"]
scaler = model_data["scaler"]

app = Flask(__name__)

def predict_market_value(features):
    features = np.array(features).reshape(1, -1)  
    features_scaled = scaler.transform(features)
    features_weighted = features_scaled * loaded_weights
    prediction = loaded_model.predict(features_weighted)[0]
    return prediction

@app.route("/")
def home():
    return jsonify({"message": "Football Market Value Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data.get("features")

        if not features:
            return jsonify({"error": "Missing 'features' in request"}), 400
        
        num_features = scaler.n_features_in_
        if len(features) != num_features:
            return jsonify({"error": f"Expected {num_features} features, but got {len(features)}"}), 400

        predicted_value = predict_market_value(features)
        return jsonify({"predicted_market_value": predicted_value})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
