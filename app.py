from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "Running"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    # prediction = model.predict([[np.array(data["exp"])]])
    prediction = {"something": "somewhere"}
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
