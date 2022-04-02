#!/usr/bin/env python3

"""Rename feedback files for Moodle assignments."""

import sys
import os
import shutil

if __name__ == '__main__':
    orig_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    os.makedirs(dest_dir, exist_ok=True)
    for (topdir, subdirs, files) in os.walk(orig_dir):
        for in_file in files:
            basename, ext = os.path.splitext(in_file)
            if ext == '.pdf':
                orig_path = os.path.join(topdir, in_file)
                dest_file = os.path.basename('_'.join([topdir, in_file]))
                dest_path = os.path.join(dest_dir, dest_file)
                shutil.copy(orig_path, dest_path)
