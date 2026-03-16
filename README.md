# Project Scaffold Generator

A simple Python tool that generates folder and file structures from a text file.

## Example structure file

```
myProject
    src
        main.py
        utils
            helper.py
    docs
        README.md
```

## Usage

```
python scaffold.py
```

The script reads `treeStructure.txt` and creates the folders and files automatically.

## Rules

* 4 spaces = new level
* names with `.` are treated as files
* names without `.` are folders
