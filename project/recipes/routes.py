#################
#### imports ####
#################

from flask import render_template

from . import recipes_blueprint


################
#### routes ####
################

@recipes_blueprint.route('/')
def index():
    # return render_template('recipes/index.html')
    from flask import current_app
    return current_app.secret_key
