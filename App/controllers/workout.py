from App.models import User, Workout, UserWorkout
from App.database import db
from App.controllers import(
    add_workout,
    remove_workout
)

def get_workouts():
    workouts=Workout.query.all()

    return workouts

def get_workout(workout_id=1):
    workout=Workout.query.get(workout_id)

    return workout

def add_workout_to_user(user_id,workout_id):
    workout=Workout.query.filter_by(id=workout_id).first()
    user=User.query.filter_by(id=user_id).first()

    add_workout(user.id, workout.id)

def remove_workout_from_user(user_id,user_workout_id):
    workout=UserWorkout.query.filter_by(id=user_workout_id).first()
    user=User.query.filter_by(id=user_id).first()

    remove_workout(user.id,workout.id) 

def get_user_workouts(user_id):
    userWorkouts = UserWorkout.query.filter_by(user_id=user_id).all()
    
    return userWorkouts