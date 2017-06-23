class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(80), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(70))
    city = db.Column(db.String(40))
    guide = db.Column(db.Boolean())
    
    def __init__(self, username, email, first_name, last_name, city, guide):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.guide = guide
