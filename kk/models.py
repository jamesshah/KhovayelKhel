from kk import db


class participants(db.Model):

    __tablename__ = "participants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    mobile = db.Column(db.String(13), nullable=False, unique=True)
    en_num = db.Column(db.String, nullable=False)
    sem = db.Column(db.String, nullable=False)
    branch = db.Column(db.String, nullable=False)

    def __init__(self, name, email, mobile, en_num, sem, branch):
        self.name = name
        self.branch = branch
        self.email = email
        self.en_num = en_num
        self.mobile = mobile
        self.sem = sem

    def __repr__(self):
        return f"participants('{self.id}','{self.name}', '{self.mobile}' , '{self.email}','{self.en_num}','{self.sem}','{self.branch}')"


# class pagathiya(db.Model):

#     __tablename__ = "pagathiya"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, db.ForeignKey(
#         'participants.id'), nullable=False)

#     def __repr__(self):
#         return f"pagathiya('{self.id}','{self.name}')"
