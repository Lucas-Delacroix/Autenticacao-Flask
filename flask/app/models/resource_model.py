from app import db

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'), nullable=False, unique=True)
    controller_id = db.Column(db.Integer, db.ForeignKey('controller.id'), nullable=False, unique=True)

    privilegies = db.relationship('Privilege', backref='resource', lazy=True)

    def __repr__(self):
        return '<Resource %r>' % self.id

    def to_dict(self):
        return {
            "id": self.id,
            "action_id": self.action_id,
            "action": self.action.to_dict(),
            "controller_id": self.controller_id,
            "controller": self.controller.to_dict()
        }