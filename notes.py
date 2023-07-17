#!/usr/bin/env python3
"""Notepad

$ notes.py new "My Notes"
tag: tech
text:
New note about technology field

$ notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

cmds = ("read", "new")
if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
elif arguments[0] == "read".lower():
    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"Title: {title}")
            print(f"Text: {text}")
            print("-" * 30)
            print()

elif arguments[0] == "new".lower():
    title = arguments[1]
    text = [
        f"{title}",
        input("Tag: ").strip(),
        input("Text:\n").strip(),
    ]
    # \t - tsv (TAB)
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")