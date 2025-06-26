from flask import Flask, request, jsonify
# Don't import flask_ngrok when deploying on Render or production
# from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# Only use run_with_ngrok in local development
# run_with_ngrok(app)

# Risk data mapping
risk_data = {
    "CUST001": {"percent": "15%", "riskCategory": "Low"},
    "CUST002": {"percent": "45%", "riskCategory": "Medium"},
    "CUST003": {"percent": "88%", "riskCategory": "High"},
    "CUST004": {"percent": "29%", "riskCategory": "Low"},
    "CUST005": {"percent": "67%", "riskCategory": "Medium"},
    "CUST006": {"percent": "73%", "riskCategory": "High"},
    "CUST007": {"percent": "38%", "riskCategory": "Medium"},
    "CUST008": {"percent": "91%", "riskCategory": "High"},
    "CUST009": {"percent": "22%", "riskCategory": "Low"},
    "CUST010": {"percent": "56%", "riskCategory": "Medium"},
}

# API endpoint
@app.route("/getRisk", methods=["GET"])
def get_risk():
    customer_id = request.args.get("customerId")
    risk = risk_data.get(customer_id, {"riskCategory": "Unknown", "percent": "N/A"})
    return jsonify({
        "customerId": customer_id,
        "riskCategory": risk["riskCategory"],
        "percent": risk["percent"]
    })

# This makes sure Render or local dev runs on proper port
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
