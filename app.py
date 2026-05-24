from flask import Flask, jsonify, request
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
<<<<<<< HEAD
CORS(app, origins=["https://khalid-deev.netlify.app"])
=======
>>>>>>> e1f05bd (Updated backend API and fixed CORS)

CORS(
    app,
    resources={
        r"/api/*": {
            "origins": ["https://khalid-deev.netlify.app"]
        }
    }
)

@app.route("/")
def home():
    return "Portfolio Backend Running"



@app.route("/api/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No JSON data received"
            }), 400

        name = data.get("name", "")
        email = data.get("email", "")
        phone = data.get("phone", "")
        budget = data.get("budget", "")
        timeline = data.get("timeline", "")
        user_message = data.get("message", "")

        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Budget: {budget}
        Timeline: {timeline}

        Message:
        {user_message}
        """

        sender_email = "quadrikhalid33@gmail.com"
        receiver_email = "quadrikhalid33@gmail.com"
        app_password = "vcjy vixn phve dxqd"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = f"Portfolio Contact from {name}"

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)

        return jsonify({
            "success": True,
            "message": "Email sent successfully"
        })

    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)1, debug=True)
