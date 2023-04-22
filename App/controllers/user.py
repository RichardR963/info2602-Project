from App.models import User, Workout, UserWorkout
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def add_workout(id,workout_id):
    user = get_user(id)
    workout=Workout.query.get(workout_id)

    if workout:
        try:
            new_workout=UserWorkout(user.id,workout_id)
            db.session.add(new_workout)
            db.session.commit()
        except Exception:
            db.session.rollback()
            return None
    return None

def remove_workout(id,workout_id):
    workout=UserWorkout.query.get(workout_id)

    if workout:
        db.session.delete(workout)
        db.session.commit()
        return True
    return None