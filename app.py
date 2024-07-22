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

    items = []

    current_dir = os.path.join('/', current_dir)
    
    # in case the user clicks and gets redirected to a file in the url
    if os.path.isfile(current_dir):
        return send_file(current_dir)

    if not os.path.exists(current_dir):
        return "<p>Path not found.</p>"

    for item in os.listdir(current_dir):
        """
        '/' is being added in between because the url doesn't end with a slash.
        results are like directoryfile'
        """
        if os.path.isfile(current_dir + '/' + item):
            items.append(item)
        else:
            # Append '/' to distinguish between directory and folders
            item += '/'
            items.append(item)

    return render_template('ui.html', path=current_dir, items=items)
