from dotenv import load_dotenv
load_dotenv(dotenv_path='app/.variables.env')

from app.server import app as application
if __name__ == "__main__":
    print("running flask app")
    application.run(host='0.0.0.0', debug=True, port=5009)
