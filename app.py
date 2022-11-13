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

# custom error page

#invalid error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)