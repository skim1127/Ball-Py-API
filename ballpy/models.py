from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Reptile(db.Model):
    __tablename__ = 'reptiles'

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(100))
    scientific_name = db.Column(db.String(100))
    conservation_status = db.Column(db.Text)
    native_habitat = db.Column(db.String(100))
    fun_fact = db.Column(db.Text)