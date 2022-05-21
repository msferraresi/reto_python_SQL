DEBUG=False
SECRET_KEY='dev'
TESTING=True
USER_DB = 'root'
PASS_DB = 'Lepo#1867'
HOST_DB = 'localhost'
PORT_DB = 3306
NAME_DB = 'reto_prod_db'
#Confiuracion Base de Datos
SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@{}:{}/{}'.format(USER_DB, PASS_DB, HOST_DB, PORT_DB, NAME_DB)
SQLALCHEMY_TRACK_MODIFICATIONS=False
#Configuracion de URLs Chistes
DAD_URL = "https://icanhazdadjoke.com/slack"
CHUCK_URL = "https://api.chucknorris.io/jokes/random"