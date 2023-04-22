from App.models import User, Workout, UserWorkout
from App.database import db

def get_workouts():
    workouts=Workout.query.all()

    return workouts

def get_workout(workout_id=1):
    workout=Workout.query.get(workout_id)

    return workout

def add_workout_to_user(user_id,workout_id):
    workout=Workout.query.filter_by(id=workout_id).first()
    user=User.query.filter_by(id=user_id).first()

    user.add_workout(workout.id)

def remove_workout_from_user(user_id,user_workout_id):
    workout=UserWorkout.query.filter_by(id=user_workout_id).first()
    user=User.query.filter_by(id=user_id).first()

    user.remove_workout(workout.id) 

def get_user_workouts(user_id):
    userWorkouts = UserWorkout.query.filter_by(user_id=user_id).all()
    
    return userWorkouts