from flask import Flask, redirect, url_for
app = Flask(__name__)


@app.route('/admin/<admin>')  # decorator for route(argument) function
def hello_admin(admin):  # binding to hello_admin call
    return 'Hello Admin %s' %admin
@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>/<admin>')
def hello_user(name,admin):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin',admin=admin))
    else:
        return redirect(url_for('hello_guest', guest=name))

if __name__ == '__main__':
    app.run(debug=True)