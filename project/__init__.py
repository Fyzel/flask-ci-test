from flask import Flask


#######################
#### Configuration ####
#######################


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):
    """Create the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    """Initialize extensions"""
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    pass


def register_blueprints(app):
    """Register blueprints"""
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    pass
