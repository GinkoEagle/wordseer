"""
Various methods helpful in the wordseer flask app.
"""
import os

from flask import abort, render_template
from flask_security.core import current_user
from sqlalchemy.orm.exc import NoResultFound

from app import app

def really_submitted(form):
    """ WTForms can be really finnicky when it comes to checking if a form
    has actually been submitted, so this method runs validate_on_submit()
    on the given form and checks if its "submitted" field has any data. Useful
    for pages that have two forms on them.

    :arg Form form: A form to check for submission.
    :returns boolean: True if submitted, false otherwise.
    """

    if form.submitted.data == "true":
        return form.validate_on_submit()
    return False

#TODO: add more conditions
def get_object_or_exception(model, condition, exception=None):
    """Either get the requested object or raise an exception.

    :arg model model: The Model of the requested object.
    :arg condition: The condition to pass to the query object.
    :arg exception: The exception to raise on failure.
    """

    try:
        return model.query.filter(condition).one()
    except NoResultFound:
        try:
            raise exception
        except TypeError:
            abort(404)

def not_found(item):
    """Render the item_not_found.html template with item set to the given item,
    and return a 404 code.

    :arg str item: The name of the item not found.
    """
    return render_template("item_not_found.html", item=item), 404

def get_structure_file(files):
    """Given a list of Document objects, return the Document that is a structure
    file. Assumes that there is only one structure file in this list.

    Arguments:
        files (list of Documents): The list of Documents to check.
    """
    for file in files:
        ext = os.path.splitext(file.path)[1][1:]
        if ext == app.config["STRUCTURE_EXTENSION"]:
            return file

