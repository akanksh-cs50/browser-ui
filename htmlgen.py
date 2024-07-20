import os

with open('build/result.html', 'w+') as result:

    result.write("""
    <style>
        @import "https://www.nerdfonts.com/assets/css/webfont.css";
    </style>
    """)

    for item in os.listdir():
        if os.path.isfile(item):
            result.write(f'<i class="nf nf-cod-file"></i> {item}<br>\n')
        else:
            result.write(f'<i class="nf nf-oct-file_directory"></i> {item}<br>\n')

    result.close()
