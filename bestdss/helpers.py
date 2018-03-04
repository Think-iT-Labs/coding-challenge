import os


def get_subdirs(dir):
    "Get a list of immediate subdirectories"
    return next(os.walk(dir))[1]


def get_subfiles(dir):
    "Get a list of immediate subfiles"
    return next(os.walk(dir))[2]
