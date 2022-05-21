from src import db, ma

class Chiste(db.Model):
    __tablename__ = 'chiste'
    id = db.Column(db.Integer, primary_key=True)
    chiste = db.Column(db.String(500))

    def __init__(self, chiste):
        self.chiste = chiste

    def __repr__(self):
        return '<Chiste %r>' % self.chiste

class ChisteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Chiste
        load_instance = True
        sqla_session = db.session
        fields = ('id', 'chiste')