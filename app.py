#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install flask flask-ngrok


# In[2]:


from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok


# In[3]:


app = Flask(__name__) 
run_with_ngrok(app)


# In[4]:


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


# In[5]:


@app.route("/getRisk",methods=["GET"])
def get_risk():
    customer_id = request.args.get("customerId")
    risk = risk_data.get(customer_id, {"riskCategory": "Unknown"})
    return jsonify({"customerId": customer_id, "riskCategory": risk["riskCategory"], "percent": percent})


# In[ ]:


app.run()


# In[ ]:




