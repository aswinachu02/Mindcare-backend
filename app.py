from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "Running"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        model = pickle.load(open("model.pkl", "rb"))
        if len(data["tweets"]) == 0:
            return jsonify({"success": False, "data": "Please send some tweets"})
        prediction = model.predict(data["tweets"])
        data = {"prediction": prediction}
        return jsonify({"success": True, "data": data})
    except Exception as err:
        return jsonify({"success": False, "data": str(err)})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
