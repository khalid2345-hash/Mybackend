from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# import os
from werkzeug.utils import secure_filename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
CORS(app, origins=["https://khalid-deev.netlify.app"])

# DATABASE
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# UPLOADS
# UPLOAD_FOLDER = "uploads"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# ADMIN PASSWORD
# ADMIN_PASSWORD = "rom2026"


# -----------------------------
# DATABASE MODEL
# -----------------------------
# class Project(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     tech = db.Column(db.String(200))
#     image = db.Column(db.String(200))
#     video = db.Column(db.String(200))
#     github = db.Column(db.String(200))
#     demo = db.Column(db.String(200))


# -----------------------------
# HOME
# -----------------------------
@app.route("/")
def home():
    return "Portfolio Backend Running"


# -----------------------------
# GET PROJECTS
# -----------------------------
# @app.route("/api/projects", methods=["GET"])
# def get_projects():

#     projects = Project.query.all()

#     result = []

#     for p in projects:
#         result.append({
#             "id": p.id,
#             "title": p.title,
#             "description": p.description,
#             "tech": p.tech,
#             "image": p.image,
#             "video": p.video,
#             "github": p.github,
#             "demo": p.demo
#         })

#     return jsonify(result)


# -----------------------------
# ADD PROJECT
# -----------------------------
# @app.route("/api/projects", methods=["POST"])
# def add_project():

#     auth = request.headers.get("Admin-Password")

#     if auth != ADMIN_PASSWORD:
#         return jsonify({"message": "Unauthorized"}), 401

#     title = request.form.get("title")
#     description = request.form.get("description")
#     tech = request.form.get("tech")
#     video = request.form.get("video")
#     github = request.form.get("github")
#     demo = request.form.get("demo")

#     image = request.files.get("image")
#     image_path = None

#     if image:
#         filename = secure_filename(image.filename)
#         filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#         image.save(filepath)
#         image_path = f"/uploads/{filename}"

#     new_project = Project(
#         title=title,
#         description=description,
#         tech=tech,
#         image=image_path,
#         video=video,
#         github=github,
#         demo=demo
#     )

#     db.session.add(new_project)
#     db.session.commit()

#     return jsonify({"message": "Project added successfully"})


# -----------------------------
# UPDATE PROJECT
# -----------------------------
# @app.route("/api/projects/<int:id>", methods=["PUT"])
# def update_project(id):

#     auth = request.headers.get("Admin-Password")

#     if auth != ADMIN_PASSWORD:
#         return jsonify({"message": "Unauthorized"}), 401

#     project = Project.query.get_or_404(id)

#     project.title = request.form.get("title", project.title)
#     project.description = request.form.get("description", project.description)
#     project.tech = request.form.get("tech", project.tech)
#     project.video = request.form.get("video", project.video)
#     project.github = request.form.get("github", project.github)
#     project.demo = request.form.get("demo", project.demo)

#     image = request.files.get("image")

#     if image:
#         filename = secure_filename(image.filename)
#         filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#         image.save(filepath)
#         project.image = f"/uploads/{filename}"

#     db.session.commit()

#     return jsonify({"message": "Project updated"})


# -----------------------------
# DELETE PROJECT
# -----------------------------
# @app.route("/api/projects/<int:id>", methods=["DELETE"])
# def delete_project(id):

#     auth = request.headers.get("Admin-Password")

#     if auth != ADMIN_PASSWORD:
#         return jsonify({"message": "Unauthorized"}), 401

#     project = Project.query.get_or_404(id)

#     db.session.delete(project)
#     db.session.commit()

#     return jsonify({"message": "Project deleted"})


# -----------------------------
# SERVE UPLOADED IMAGES
# -----------------------------
# @app.route("/uploads/<filename>")
# def uploaded_file(filename):
#     return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


# -----------------------------
# CONTACT FORM
# -----------------------------
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
<!DOCTYPE html>
<html>
<head>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f4f6f8;
      margin: 0;
      padding: 0;
    }}
    .container {{
      max-width: 600px;
      margin: 30px auto;
      background: #ffffff;
      padding: 25px;
      border-radius: 10px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}
    .header {{
      background: #111827;
      color: #ffffff;
      padding: 15px;
      text-align: center;
      border-radius: 10px 10px 0 0;
      font-size: 20px;
      font-weight: bold;
    }}
    .content {{
      padding: 20px;
      color: #333;
      line-height: 1.6;
    }}
    .field {{
      margin-bottom: 12px;
    }}
    .label {{
      font-weight: bold;
      color: #111827;
    }}
    .message-box {{
      background: #f9fafb;
      padding: 12px;
      border-left: 4px solid #3b82f6;
      margin-top: 10px;
      white-space: pre-line;
    }}
    .footer {{
      text-align: center;
      font-size: 12px;
      color: #888;
      margin-top: 20px;
    }}
  </style>
</head>

<body>
  <div class="container">
    
    <div class="header">
      New Portfolio Contact 🚀
    </div>

    <div class="content">

      <div class="field">
        <span class="label">Name:</span> {name}
      </div>

      <div class="field">
        <span class="label">Email:</span> {email}
      </div>

      <div class="field">
        <span class="label">Phone:</span> {phone}
      </div>

      <div class="field">
        <span class="label">Budget:</span> {budget}
      </div>

      <div class="field">
        <span class="label">Timeline:</span> {timeline}
      </div>

      <div class="field">
        <span class="label">Message:</span>
        <div class="message-box">
          {user_message}
        </div>
      </div>

    </div>

    <div class="footer">
      Sent from your Portfolio Contact Form
    </div>

  </div>
</body>
</html>
"""

        sender_email = "quadrikhalid33@gmail.com"
        receiver_email = "quadrikhalid33@gmail.com"
        app_password = "vcjy vixn phve dxqd"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = f"Portfolio Contact from {name or 'Unknown'}"

        msg.attach(MIMEText(body, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, app_password)
            server.send_message(msg)

        return jsonify({
            "success": True,
            "message": "Email sent successfully"
        }), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":

    # with app.app_context():
    #     db.create_all()

    app.run(host="127.0.0.1", port=5001, debug=True)
