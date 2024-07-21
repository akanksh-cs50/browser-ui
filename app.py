from flask import Flask, render_template, send_file
import os
from icons import icon_name

app = Flask(__name__)

app.jinja_env.filters["icon_name"] = icon_name

# deal with this later
@app.route('/favicon.ico')
def favicon():
    return ''


@app.route('/<path:current_dir>')
def ui(current_dir):

    items = []

    if not os.path.exists(current_dir):
        return "<p>Path not found.</p>"

    for item in os.listdir(current_dir):
        if os.path.isfile(item):
            items.append(item)
        else:
            items.append(
                    str(list(item).append('/')))


    return render_template('ui.html', path=f'{os.getcwd()}', items=items)
