from App.database import db

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    reps= db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    muscle_group=db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(255))

    def __init__(self,name,reps,sets,muscle_group,description):
        self.name=name
        self.reps=reps
        self.sets=sets
        self.muscle_group=muscle_group
        self.description=description
    
    def get_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'sets':self.sets,
            'muscle_group':self.muscle_group,
            'description':self.description
        }