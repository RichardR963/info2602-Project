from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views
from .user import user_views

from App.controllers import (
    get_workouts,
    get_workout,
    add_workout_to_user,
    remove_workout_from_user
)

workout_views=Blueprint('workout_views',__name__,template_folder='../templates')

@workout_views.route('/workouts', methods=['GET'])
@workout_views.route('/workouts/<int:workout_id>', methods=['GET'])
@login_required
def get_workouts_action(workout_id=1):
    user=current_user

    selected_workout=get_workout(workout_id)
    workout=get_workouts()

    return render_template('index.html',selected_workout=selected_workout,workout=workout)

@workout_views.route('/workouts/<int:workout_id>', methods=['POST'])
@login_required
def add_workout_action(workout_id):
    user=current_user

    add_workout_to_user(user.id,workout_id)

    flash('Workout added!')

    return redirect('/workouts')

@workout_views.route('/workouts/<int:user_workout_id>', methods=['POST'])
@login_required
def remove_workout_action(user_workout_id):
    user=current_user

    remove_workout_from_user(user.id,workout_id)

    flash('Workout removed!')

    return redirect('/workouts')