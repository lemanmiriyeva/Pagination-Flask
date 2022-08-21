from extensions import db
# from admin import BlogsAdmin


class Blogs(db.Model):
    __tablename__ = "Blogs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable = False)
    description = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return f'{self.title}'

    def __init__(self, title, description):
        self.title = title 
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()