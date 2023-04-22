from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from App.models import db, User, UserWorkout, Workout
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
@index_views.route('/index', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

#signup view route
@index_views.route('/signup', methods=['GET'])
def signup_page():
    return render_template('signup.html')

@index_views.route("/signup", methods=['POST'])
def signup_user():
  data = request.form     #gets data entered (username, pw)
  user = User.query.filter_by(username=data['username']).first()      #finds possible matching entry
  if user:
    flash("username taken, try another")       #if entry exists, display error and redirect to sign up page
    return redirect("/signup")
  else:
    user = User(username=data['username'], password=data['password'])
    db.session.add(user)        #else, add user to db and redirect to login
    db.session.commit()
    return redirect("/login")

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')

    with open('workouts.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            workout=Workout(name=row['name'],reps=row['reps'],sets=row['sets'],muscle_group=row['muscle_group'],description=row['description'])

            db.session.add(workout)
        db.session.commit()

    print('database intialized')


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})
