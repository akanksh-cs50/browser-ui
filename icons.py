"""
This file is used for giving the icon name when given a file extension.

Example:

.rs -> nf nf-dev-rust
.png -> nf-md-file_png_box

This file will grow as development goes.
"""

associations = {
    'txt': 'nf nf-fa-file-text',
    'jpg': 'nf nf-fa-file-image',
    'png': 'nf nf-fa-file-image',
    'rs': 'nf nf-dev-rust'
}

def icon_name(filename:str):
    return associations[filename.split('.')[-1]] # Using -1 index which gives us the last element in the list.
