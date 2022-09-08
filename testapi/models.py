


from testapi import db
from datetime import datetime



#Widget table definition
class Widget(db.Model):

    

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    parts = db.Column(db.Integer, nullable = False)
    date_create = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    date_update = db.Column(db.DateTime, default = None)

    def __repr__():
        return f"Widget('{self.name}', '{self.parts}', '{self.create_date}', '{self.update_date}')"

    def as_dict(self):
        return{c.name: getattr(self, c.name) for c in self.__table__.columns}