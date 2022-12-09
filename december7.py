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

    def sum_of_small_sub_folders(self):
        return sum(
            [
                folder.size
                for folder in self.folders.values()
                if folder.size <= 100000
            ]
        ) + sum(
            [
                folder.sum_of_small_sub_folders()
                for folder in self.folders.values()
            ]
        )

    def sizes_of_all_subdirectories(self):
        sizes = set([folder.size for folder in self.folders.values()]) | {
            self.size
        }
        for folder in self.folders.values():
            sizes = sizes | folder.sizes_of_all_subdirectories()
        return sizes

    @property
    def parent(self):
        if self._parent == None:
            return self
        else:
            return self._parent

    @property
    def size(self):
        return sum([file.size for file in self.files]) + sum(
            [folder.size for folder in self.folders.values()]
        )


class File:
    def __init__(self, file_name: str, size: int):
        self.file_name = file_name
        self.size = size

    def __eq__(self, other: object):
        if not isinstance(other, File):
            return NotImplemented
        return (self.file_name == other.file_name) & (self.size == other.size)

    def __hash__(self):
        return hash((self.file_name, self.size))

    def __str__(self):
        return f"{self.file_name}, {self.size}"


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


def get_smallest_subdir_above_threshold(folder: Folder, threshold: int) -> 0:
    return min(
        [
            size
            for size in folder.sizes_of_all_subdirectories()
            if size > threshold
        ]
    )


def get_threshold(folder: Folder):
    return -(70000000 - 30000000 - folder.size)


def size_of_file_to_delete(folder: Folder):
    threshold = get_threshold(folder)
    return get_smallest_subdir_above_threshold(folder, threshold)


if __name__ == "__main__":
    with open("december7_input.txt") as file:
        december7_commands = file.read()
    print(
        "What is the sum of the total sizes of those directories? ",
        parse_complete_tree(december7_commands).sum_of_small_sub_folders(),
    )

    print(
        "What is the total size of that directory?",
        size_of_file_to_delete(parse_complete_tree(december7_commands)),
    )
