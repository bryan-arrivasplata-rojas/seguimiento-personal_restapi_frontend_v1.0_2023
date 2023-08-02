
from flask import Flask
from src.Routes.user import userRoute
from src.Routes.profile import profileRoute
from src.Routes.history import historyRoute
from src.Routes.role import roleRoute
from src.Routes.recognition import recognitionRoute
import ssl
from pyngrok import ngrok
ssl._create_default_https_context = ssl._create_unverified_context
ngrok.set_auth_token('2SY66hL2TWooDqMNX0sXyemTQdE_5ykXcLAZJepP13bF6edtf')

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World! My name is Bryan Arrivasplata Rojas, creador de esta RestApi\n <br> WebSite: <a href="https://www.bryanarrivasplata.com">https://www.bryanarrivasplata.com</a> \n Linkedin: <a href="https://www.linkedin.com/in/bryan-daniell-arrivasplata-rojas-156508213/">bryan-daniell-arrivasplata-rojas</a> '

profileRoute(app)
userRoute(app)
historyRoute(app)
roleRoute(app)
recognitionRoute(app)

if __name__ == "__main__":
    public_url = ngrok.connect(5000)
    # Obtener la URL pública generada por Ngrok
    public_url_str = str(public_url)
    print('URL pública de Ngrok:', public_url_str)
    app.run()