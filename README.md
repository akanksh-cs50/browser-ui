# browser-ui

A web app to browse your server's files.

This flask app can be used can be used to access files over the network (the same wifi) on any device which has access to the network and has a web browser.

This makes it more convinient than setting up other wirless transfer protocols such as ftp, ssh, samba, webdav, etc.

This web app has features such as:

- [Nerd Font icons](https://www.nerdfonts.com/cheat-sheet) to distinguish fies/directories, eg. a file ending in .py, a python file has a python icon next to it in the web app.
- Search through entries, javascript is used on the client side to filter through the directory entries. This can be used as soon as it's loaded as the search bar is auto-focused.
- Respects light/dark mode preference. This can be changed in ``static/style.css`` with the ``:root`` property, the default dark mode mimics the matrix theme.

# About

This project was made as a replacement to the default directory listing when visiting a http server
![Big text showing the path and all the items below it in a filesystem directory](doc/example.png)

and make it look like this
![Filesystem directory contents with icons beside them to distinguish their type](doc/new.png)

It is an overhaul of the default.

# Demo

Video: https://youtu.be/u4Zy3ViEe-8

[![Thumbnail for the youtube video showcasing 'browser-ui'](http://img.youtube.com/vi/u4Zy3ViEe-8/0.jpg)](http://www.youtube.com/watch?v=u4Zy3ViEe-8)

Thanks to [this stackoverflow answer for the above markdown](https://stackoverflow.com/a/16079387) :)

# Usage

This project requires Python to be installed on the server.

In my case I have used python 3.12 and Flask 3.0.3.

First step is to download the source code with ``git clone https://github.com/akanksh-cs50/browser-ui.git`` or ``https://github.com/akanksh-cs50/browser-ui/archive/refs/heads/main.zip`` and open a terminal in the directory.

## Windows

On Windows you can run ```pip install -r requirements.txt```, and then run ```flask run --host=0.0.0.0```

## macOS / Linux

Unix-based systems such as macOS and linux require a virtual evironment to be used.

Which can be achieved with the below commands.

More details about this change is present in [PEP 668](https://peps.python.org/pep-0668/)

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
