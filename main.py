import commonmark
import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/p/<name>')
def page(name):
    for ch in name:
        if not ch in 'abcdefghijklmnopqrstuvwxyz_':
            flask.abort(404)

    try:
        with open('pages/{}.md'.format(name), 'r') as f:
            content = commonmark.commonmark(f.read())
    except FileNotFoundError as e:
        flask.abort(404)

    title = name.replace('_', ' ').title()

    return flask.render_template('page.html', content=content, title=title)


