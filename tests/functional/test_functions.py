"""
This file (test_functions.py) contains the functional tests for the project.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the blueprint.
"""
from project import create_app


def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello, World!" in response.data
