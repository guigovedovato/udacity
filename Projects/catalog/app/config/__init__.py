#!/usr/bin/env python3
import os


def open_file(config_type):
    return os.path.join(os.getcwd(), 'app\\config', config_type + '.json')
