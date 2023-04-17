from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def add_workout(self,workout_id):
        workout=Workout.query.get(workout_id)

        if workout:
            try:
                new_workout=UserWorkout(self.id,workout_id)
                db.session.add(new_workout)
                db.session.commit()
            except Exception:
                db.session.rollback()
                return None
        return None
    
    def remove_workout(self,workout_id):
        workout=UserWorkout.query.get(workout_id)

        if workout.user == self:
            db.session.delete(workout)
            db.session.commit()
            return True
        return None

