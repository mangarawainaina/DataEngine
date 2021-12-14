"""Here contains the factory function that starts our application"""
from flask import Flask
from views import routes
from routes import view


def create_app():
    
    app=Flask(__name__)
    
    app.register_blueprint(routes)
    app.register_blueprint(view)
    
    return app.run(debug=True)