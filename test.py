
"""
import os

root = '/Users/ks1v/Stage/movie-screenshots/png'
target = '/Users/ks1v/Stage/movie-screenshots/new'

for dirpath, dirnames, filenames in os.walk(root):
    # Calculate the relative path from the root directory
    relative_path = os.path.relpath(dirpath, root)
    # Create the corresponding directory in the target location
    target_path = os.path.join(target, relative_path)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"Created: {target_path}")
    else: 
        print(relative_path + " exists")
"""
import os
import shutil
import subprocess

root = '/Users/ks1v/Stage/movie-screenshots/png'
target = '/Users/ks1v/Stage/movie-screenshots/new'


for dirpath, dirnames, filenames in os.walk(target):
    # Calculate the relative path from the root directory
    relative_path = os.path.relpath(dirpath, target)
    # Create the corresponding directory in the target location
    root_path = os.path.join(root, relative_path)
    
    for filename in filenames:
        target_file = os.path.join(dirpath, filename)
        root_file = os.path.join(root_path, filename)
        file_extension = os.path.splitext(filename)[-1].lower()
        
        if file_extension == '.png':
            png_filename = os.path.splitext(filename)[0] + '.png'
            root_file = os.path.join(root_path, png_filename)
            
            print(f"Converted and saved: {target_file}")
        else:
            # Copy other files
            shutil.copy2(source_file, target_file)
            print(f"Copied: {target_file}")



""" import re

regex = r"^(.+)[sS](\d{1,2}).+[eE](\d{1,2}).+(\d{4})[^pi].+(\d{2}_\d{2}_\d{2}).+(\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}).+\.(\w{3,4})"

test_str = "Kiberderevnya.s01.e08.2023.WEB-DL.2160p.SDR_00_02_48 2023-10-30 23-16-25.515.png"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

print("END") """