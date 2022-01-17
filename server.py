import connexion
from flask import Flask,render_template


#def create_app():
app = connexion.FlaskApp(
__name__, specification_dir="./",options={"swagger_ui": True, "serve_spec": True}
)
app.add_api("swagger.yaml", strict_validation=True)
flask_app = app.app
#flask_app.json_encoder = encoder.JSONEncoder

#return flask_app
	
#@app.route("/")
#def home():
    #return flask_app
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    flask_app.run()
