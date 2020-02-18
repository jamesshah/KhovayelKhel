from kk import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    mobile = db.Column(db.String(13), nullable=False, unique=True)
    en_num = db.Column(db.String, nullable=False)
    sem = db.Column(db.String, nullable=False)
    branch = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.name}', '{self.mobile}' , '{self.email}','{self.en_num}','{self.sem}','{self.branch}')"
