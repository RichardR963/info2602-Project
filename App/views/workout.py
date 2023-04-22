from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views
from .user import user_views

from App.controllers import (
    get_workouts,
    get_workout,
    add_workout_to_user,
    remove_workout_from_user,
    get_user_workouts
)

workout_views=Blueprint('workout_views',__name__,template_folder='../templates')

@workout_views.route('/workouts', methods=['GET'])
@workout_views.route('/workouts/<int:workout_id>', methods=['GET'])
@login_required
def get_workouts_action(workout_id=1):
    user=current_user

    selected_workout=get_workout(workout_id)
    workouts=get_workouts()
    userWorkouts = get_user_workouts(user.id)
    return render_template('home.html', user=user, selected_workout=selected_workout, workouts=workouts, userWorkouts=userWorkouts)

@workout_views.route('/add-workouts/<int:workout_id>', methods=['POST'])
@login_required
def add_workout_action(workout_id):
    user=current_user
    if user:
        flash('Doing something')
        
    add_workout_to_user(user.id,workout_id)

    flash('Workout added!')

    return redirect('/workouts')

@workout_views.route('/remove-workouts/<int:user_workout_id>', methods=['POST'])
@login_required
def remove_workout_action(user_workout_id):
    user=current_user

    remove_workout_from_user(user.id,workout_id)

    flash('Workout removed!')

    return redirect('/workouts')