#!/usr/bin/env python3

"""Convert to pdf all html files under a directory."""

import sys
import os
import subprocess

if __name__ == '__main__':
    curr_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    for (topdir, subdirs, files) in os.walk(curr_path):
        for in_file in files:
            basename, ext = os.path.splitext(in_file)
            if ext == '.html':
                html_file = os.path.join(topdir, in_file)
                out_file = os.path.join(topdir, basename + '.pdf')
                args = ['wkhtmltopdf',
                        '--footer-center', 'Uploaded as html',
                        '--footer-font-size', '6',
                        html_file, out_file]
                print(f'\n=======> Processing {html_file} ...')
                try:
                    subprocess.run(args, check=True)
                except subprocess.CalledProcessError:
                    print("======> ERROR\n")
