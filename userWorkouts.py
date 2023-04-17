from App.database import db

class UserWorkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    workout = db.relationship('Workout')

    def __init__(self,user_id,workout_id):
        self.user_id=user_id
        self.workout_id=workout_id
    
    def get_json(self):
        return{
            'id':self.id,
            'user_id':self.user_id,
            'workout_id':self.workout_id
        }