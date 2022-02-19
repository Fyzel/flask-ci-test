# Example from https://gitlab.com/patkennedy79/flask_user_management_example
# and https://testdriven.io/blog/flask-pytest/

from project import create_app

# Call the application factory function to construct a Flask application
# instance using the development configuration
app = create_app('flask.cfg')
