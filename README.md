Basically a custom ui / rice instead of whatever the default looks like when doing ```python -m http.server``` and looking at a directory.
I'll have search, icons for every entry like audio file, directory, text, programming language file.
I'll use fontawesome or symbols only nerd font for that.
It will look like a fancy ls like [eza](https://github.com/eza-community/eza).
[Reference screenshot](https://github.com/sebastiencs/ls-icons/raw/master/image/ls.jpg)

The default is like this:

# Directory listing for /

- bin@
- boot/
- dev/
- etc/
- home/
- initrd.img@
- initrd.img.old@
- lib@
- lib64@
- lost+found/
- media/
- mnt/
- opt/
- proc/
- root/
- run/
- sbin@
- srv/
- sys/
- tmp/
- usr/
- var/
- vmlinuz@
- vmlinuz.old@

But with mine I'll have something which combines the look of explorer.exe and ls-icons.

## TODO

Take ``htmlgen.py`` as a base and make a flask app which lists directory content.
The route should match the directory content.
Eg: 'localhost:5000/home/akanksh/' should show all the files in my directory.
Need to figure out file associations to use the appropriate icons too.
Like devicons, [vim-devicons](https://github.com/ryanoasis/vim-devicons) and [vscode-icons](https://github.com/vscode-icons/vscode-icons)
