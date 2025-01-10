from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from email_sender import send_email

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the UserInteraction model
class UserInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    clicked_link = db.Column(db.Boolean, default=False)

# Create all database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_phishing_email/<string:to_email>')
def send_phishing_email(to_email):
    subject = "Important Update Required"
    body = render_template('phishing_email.html', link=url_for('track_click', email=to_email))
    
    try:
        send_email(to_email, subject, body)
        return jsonify(message=f"Phishing email sent to {to_email}!")
    except Exception as e:
        return jsonify(message=f"Failed to send email: {str(e)}"), 500

@app.route('/track_click/<string:email>')
def track_click(email):
    interaction = UserInteraction(email=email, clicked_link=True)
    db.session.add(interaction)
    db.session.commit()
    
    return render_template('thank_you.html')

@app.route('/report')
def report():
    interactions = UserInteraction.query.all()
    return render_template('report.html', interactions=interactions)

if __name__ == '__main__':
    app.run(debug=True)