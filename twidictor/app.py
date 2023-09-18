from flask import Flask

def create_app():
	'''
	Create and configure an instance of the Flask application.
	'''

	app = Flask(__name__)

	@app.route('/')
	def root():
		return '''I AM THE TWIDICTOR!
			  TREMBLE BEFORE MY PREDICTIVE POWER'''

	return app
