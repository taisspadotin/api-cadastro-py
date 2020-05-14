from flask import Flask

def create_app():
	app = Flask(__name__)
	
	from .person import bp_person
	app.register_blueprint(bp_person)

	return app