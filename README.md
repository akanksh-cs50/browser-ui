# browser-ui

A web app to browse your server's files.

# About
This project was made as a replacement to the default directory listing when visiting a http server
![Big text showing the path and all the items below it in a filesystem directory](doc/example.png)

and make it look like this
![Filesystem directory contents with icons beside them to distinguish their type](doc/new.png)

# Usage

This project requires Python to be installed.

## Windows

On Windows you can run ```pip install -r requirements.txt```, and then run ```flask run --host=0.0.0.0```

## macOS / Linux

Unix-based systems such as macOS and linux require a virtual evironment to be used, which can be achieved with the below commands.

```
python3 -m venv .venv # creating a virtual environment in .venv/
source .venv/bin/activate # activating the virtual environment
pip install -r requirements.txt # installing dependencies
flask run --host=0.0.0.0 # running the server
```

# Configuration

You can edit the ``BASE_DIR`` variable in ``app.py`` with an _absolute_ path to use as the starting directory or the 'root'.

The default is '/'.

You might need to restart flask if you update the ``BASE_DIR`` variable.

Hot-reloading is possible with the --debug flag.

Enjoy browsing :)
