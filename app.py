from flask import Flask, render_template

# Flask instance
app = Flask(__name__)

# a route decorator
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def profile(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(debug=True, port=8000)