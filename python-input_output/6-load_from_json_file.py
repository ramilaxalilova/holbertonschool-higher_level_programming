#!/usr/bin/python3
"""load_from_json_file"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
