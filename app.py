from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_KEY = "test_bde227188757bcfa53707f0f1b89a350d8bd7c4cc36db7cd337d446a09a0de54"
HEADERS = {
    "X-BUSINESS-API-KEY": API_KEY,
    "Content-Type": "application/json"
}
BASE_URL = "https://api.sandbox.hit-pay.com/v1/payment-requests"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_payment():
    amount = request.form["amount"]
    name = request.form["name"]
    email = request.form["email"]

    payload = {
        "amount": amount,
        "currency": "MYR",
        "name": name,
        "email": email,
        "redirect_url": "https://pbtp.jages.org/thankyou"
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    result = response.json()
    return redirect(result["url"])

@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")

# No need for app.run() in cPanel
