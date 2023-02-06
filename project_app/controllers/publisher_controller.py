from flask import Flask, render_template, request, redirect
from repositories import game_repository
from repositories import publisher_repository
from models.publisher import Publisher

from flask import Blueprint

publishers_blueprint = Blueprint("publishers", __name__)

@publishers_blueprint.route("/publishers")
def publishers():
    publishers = publisher_repository.select_all()
    return render_template("publishers/index.html", publishers = publishers)

@publishers_blueprint.route("/publishers/new", methods=['GET'])
def new_publisher():
    return render_template("publishers/new.html")

@publishers_blueprint.route("/publishers", methods=['POST'])
def create_publisher():
    publisher_name = request.form['publisher_name']
    contact_details = request.form['contact_details']
    publisher = Publisher(publisher_name, contact_details)
    publisher_repository.save(publisher)
    return redirect('/publishers')

@publishers_blueprint.route("/publishers/<id>", methods=['GET'])
def show_publisher(id):
    publisher = publisher_repository.select(id)
    return render_template('publishers/show.html', showPublisher = publisher)

@publishers_blueprint.route("/publishers/<id>/edit")
def edit_publisher(id):
    publisher = publisher_repository.select(id)
    return render_template('publishers/edit.html', publisher = publisher)

@publishers_blueprint.route('/publishers/<id>', methods=['POST'])
def update_publisher(id):
    publisher_name = request.form['publisher_name']
    contact_details = request.form['contact_details']
    publisher = Publisher(publisher_name, contact_details, id)
    publisher_repository.update(publisher)
    return redirect('/publishers')

@publishers_blueprint.route('/publishers/<id>/delete', methods=['POST'])
def delete_publisher(id):
    publisher_repository.delete(id)
    return redirect('/publishers')
