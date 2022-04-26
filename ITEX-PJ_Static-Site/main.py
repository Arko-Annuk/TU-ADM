from flask import Flask, render_template, request, redirect
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
Markdown(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reserv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
 
class reserv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    adults = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Integer, nullable=False)
    checkin = db.Column(db.String, nullable=False)
    checkout = db.Column(db.String, nullable=False)   
    room = db.Column(db.String, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

@app.route("/")
def landing():
    return render_template('1-landing.html')

@app.route("/fitness")
def fitness():
    return render_template('2-fitness.html')

@app.route("/programming")
def programming():
    return render_template('3-programming.html')

@app.route("/rentals", methods=['POST', 'GET'])
def rentals():
    if request.method == 'POST':
        p_name = request.form['name']
        p_email = request.form['email']
        p_phone = request.form['phone']
        p_adults = request.form['adults']
        p_children = request.form['children']
        p_checkin = request.form['checkin']
        p_checkout = request.form['checkout']
        p_room = request.form['room']
        new_reserv = reserv(name=p_name, email=p_email, phone=p_phone, adults=p_adults, children=p_children, checkin=p_checkin, checkout=p_checkout, room=p_room)
        db.session.add(new_reserv)
        db.session.commit()
        return redirect('/rentals')
    else:
        #all_reserv = reserv.query.order_by(reserv.time).all()
        return render_template('4-rentals.html')



if __name__ == "__main__":
    app.run()

'''Rentals HTML textarea field transmitable to db TODO'''