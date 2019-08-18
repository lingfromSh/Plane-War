import os
import json


class Reader(object):
    def __init__(self, setting_file_number=0):
        self.filename = "setting.json"
        self.filepath = os.getcwd() + self.filename

    def getContent(self, content_type=None):
        with open(self.filepath, "r+", encoding="utf8") as f:
            setting_string = f.read()
            f.close()
        if content_type:
            return json.loads(setting_string[content_type])
        else:
            return json.loads(setting_string)

class Writer(object):
    def __init__(self, setting_file_number=0):
        self.filename = "setting.json"
        self.filepath = os.getcwd() + self.filename
