"""Functions for the December 7 task."""

from typing import Set, Dict
from helpers import split_input


class Folder:
    def __init__(self, parent=None):
        self.files: Set[File] = set()
        self.folders: Dict[Folder] = {}
        self._parent = parent

    def add_file(self, file_name: str, size: int):
        self.files.add(File(file_name, size))
        return self

    def add_folder(self, folder_name: str):
        self.folders[folder_name] = Folder(parent=self)
        return self

    def __eq__(self, other: object):
        if not isinstance(other, Folder):
            return NotImplemented
        return (self.files == other.files) & (self.folders == other.folders)

    def __str__(self):
        return (
            ", ".join([str(f) for f in self.files])
            + ", "
            + ", ".join([k for k in self.folders.keys()])
        )

    def update_folder(self, folder_name: str, folder_value: object):
        self.folders[folder_name] = folder_value
        return self

    @property
    def parent(self):
        if self._parent == None:
            return self
        else:
            return self._parent


class File:
    def __init__(self, file_name: str, file_size: int):
        self.file_name = file_name
        self.file_size = file_size

    def __eq__(self, other: object):
        if not isinstance(other, File):
            return NotImplemented
        return (self.file_name == other.file_name) & (
            self.file_size == other.file_size
        )

    def __hash__(self):
        return hash((self.file_name, self.file_size))

    def __str__(self):
        return f"{self.file_name}, {self.file_size}"


def add_from_ls_line(folder: Folder, line: str):
    if line[:3] == "dir":
        name = line[4:]
        folder.add_folder(name)
    else:
        size, name = line.split(" ")
        folder.add_file(name, int(size))
    return folder


Folder.add_from_ls_line = add_from_ls_line


def parse_folder_ls(ls: str) -> Folder:
    new_folder = Folder()
    for line in split_input(ls, "\n"):
        new_folder = add_from_ls_line(new_folder, line)
    return new_folder


def parse_complete_tree(commands: str) -> Folder:
    splitted = split_input(commands, "\n")
    root = Folder()
    current_folder = root
    for line in splitted[1:]:
        if line[0] != "$":
            current_folder.add_from_ls_line(line)
            print(current_folder)
            continue
        elif line == "$ cd ..":
            current_folder = current_folder.parent
        elif line == "$ cd /":
            continue
        elif line[:4] == "$ cd":
            current_folder = current_folder.folders[line[5:]]
        else:
            continue
    return root


if __name__ == "__main__":
    with open("december6_input.txt") as file:
        december6_signal = file.read()
