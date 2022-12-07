"""Test for the functions for the December 6 task."""


import pytest

from december7 import Folder, File, parse_folder_ls, parse_complete_tree

EXAMPLE = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

FOLDER_E_LS = """
584 i
"""

FOLDER_E = Folder().add_file("i", 584)


FOLDER_D_LS = """
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

FOLDER_D = (
    Folder()
    .add_file("j", 4060174)
    .add_file("d.log", 8033020)
    .add_file("d.ext", 5626152)
    .add_file("k", 7214296)
)

FOLDER_A_LS = """
dir e
29116 f
2557 g
62596 h.lst
"""

FOLDER_A = (
    Folder()
    .add_file("f", 29116)
    .add_file("g", 2557)
    .add_file("h.lst", 62596)
    .add_folder("e")
)


FOLDER_ROOT = (
    Folder()
    .add_file("b.txt", 14848514)
    .add_file("c.dat", 8504156)
    .add_folder("a")
    .add_folder("d")
)

FOLDER_ROOT_LS = """
dir a
14848514 b.txt
8504156 c.dat
dir d
"""


@pytest.mark.parametrize(
    "ls_output, folder",
    [
        (FOLDER_A_LS, FOLDER_A),
        (FOLDER_D_LS, FOLDER_D),
        (FOLDER_E_LS, FOLDER_E),
        (FOLDER_ROOT_LS, FOLDER_ROOT),
    ],
)
def test_parse_single_ls(ls_output, folder):
    print(folder)
    print(parse_folder_ls(ls_output))
    assert parse_folder_ls(ls_output) == folder


def test_parse_complete_tree():
    root = parse_complete_tree(EXAMPLE)
    a_nested = FOLDER_A.update_folder("e", FOLDER_E)
    root_nested = FOLDER_ROOT.update_folder("a", a_nested).update_folder(
        "d", FOLDER_D
    )
    assert root == root_nested


def test_folder_equal():
    assert Folder().add_file("j", 4060174) == Folder().add_file("j", 4060174)
    assert Folder().add_file("j", 4060174) != Folder().add_file("j", 4160174)
    assert Folder().add_file("j", 4060174) != Folder().add_file("k", 4160174)
    assert Folder().add_file("j", 4060174).add_file(
        "k", 4160174
    ) == Folder().add_file("j", 4060174).add_file("k", 4160174)
    assert Folder().add_file("j", 4060174).add_file(
        "k", 4160174
    ) == Folder().add_file("k", 4160174).add_file("j", 4060174)
    assert Folder().add_folder("j") == Folder().add_folder("j")
    assert Folder().add_folder("k") != Folder().add_folder("j")
