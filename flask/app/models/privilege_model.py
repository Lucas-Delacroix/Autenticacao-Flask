from app import db

class Privilege(db.Model):
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=False, primary_key=True)
    allow = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return '<Privilege %r>' % self.role_id

    def to_dict(self):
        return {
            "role_id": self.role_id,
            "role": self.role.to_dict(),
            "resource_id": self.resource_id,
            "resource": self.resource.to_dict(),
            "allow": self.allow
        }