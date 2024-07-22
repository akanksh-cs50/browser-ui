from flask import Flask, render_template, send_file, redirect
import os
from icons import icon_name

app = Flask(__name__)

app.jinja_env.filters["icon_name"] = icon_name

# deal with this later
@app.route('/favicon.ico')
def favicon():
    return redirect('/')

@app.route('/<path:current_dir>')
def ui(current_dir):

    items = []

    current_dir = os.path.join('/', current_dir)
    print(current_dir)

    if not os.path.exists(current_dir):
        return "<p>Path not found.</p>"

    for item in os.listdir(current_dir):
        """
        '/' is being added in between because the url doesn't end with a slash.
        results are like directoryfile'
        """
        if os.path.isfile(current_dir + '/' + item):
            print(f'{item} is considered a FILE with {current_dir + item} as full path')
            items.append(item)
        else:
            # Append '/' to distinguish between directory and folders
            print(f'{item} is considered a DIRECTORY with {current_dir + item} as full path')
            item += '/'
            items.append(item)

    return render_template('ui.html', path=current_dir, items=items)