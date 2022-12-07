"""Functions for the December 7 task."""

from typing import Set, Dict
from helpers import split_input


class Folder:
    def __init__(self, parent=None):
        self.files: Set[File] = set()
        self.folders: Dict[Folder] = {}
        self._parent = None

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


def parse_folder_ls(ls: str) -> Folder:
    new_folder = Folder()
    for line in split_input(ls, "\n"):
        if line[:3] == "dir":
            name = line[4:]
            new_folder.add_folder(name)
        else:
            size, name = line.split(" ")
            new_folder.add_file(name, int(size))
    return new_folder


def parse_complete_tree(commands: str) -> Folder:
    splitted = split_input(commands, "\n")
    root_ls = ""
    for line in splitted[2:]:
        if line[0] != "$":
            root_ls += line + "\n"
        else:
            break
    print(root_ls)
    root = parse_folder_ls(root_ls)
    return root


if __name__ == "__main__":
    with open("december6_input.txt") as file:
        december6_signal = file.read()
