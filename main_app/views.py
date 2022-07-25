from main_app.settings import app

@app.route('/')
@app.route('/index')
def index():
    return "Test page"
    