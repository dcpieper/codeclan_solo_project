from flask import Flask, render_template
from controllers.games_controller import games_blueprint
from controllers.publisher_controller import publishers_blueprint
app = Flask(__name__)

app.register_blueprint(games_blueprint)
app.register_blueprint(publishers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)