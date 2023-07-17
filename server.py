from flask import Flask, render_template, redirect, request
# import the class from friend.py
from flask_app import app
from flask_app.controllers import dojos_controller, ninjas_controller






if __name__ == "__main__":
    app.run(debug=True)