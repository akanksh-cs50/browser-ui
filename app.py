from flask import Flask, render_template, send_file, redirect
import os
from icons import icon_name

app = Flask(__name__)

app.jinja_env.filters["icon_name"] = icon_name

# deal with this later
@app.route('/favicon.ico')
def favicon():
    return redirect('/')

@app.route('/', defaults={'current_dir': ''})
@app.route('/<path:current_dir>')
def ui(current_dir):

    current_dir = os.path.join('/', current_dir)

    # Checking for PermissionError
    try:
        if os.path.isfile(current_dir):
            open(current_dir)
        else:
            os.scandir(current_dir)
    except PermissionError:
        return render_template('error.html', error=f'Permission denied: {current_dir}')
   
    # in case the user clicks and gets redirected to a file in the url
    if os.path.isfile(current_dir):
        return send_file(current_dir)

    if not os.path.exists(current_dir):
        return render_template('error.html', error='File not found')
    items = os.scandir(current_dir)

    return render_template('ui.html', path=current_dir, items=items)
