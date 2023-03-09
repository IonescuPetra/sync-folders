import os
import os.path
import json
from os import path
from datetime import datetime


class ConfigCustom():

    def __init__(self):

        try:
            f = open('config.json', 'r')
            data = json.loads(f.read())
            f.close()
        except:
            self.create_config_file()
        finally:
            f = open('config.json', 'r')
            data = json.loads(f.read())
            f.close()

        self.data = data
        self.log_path = data['log_path']
        self.source_path = data['source_path']
        self.replica_path = data['replica_path']
        self.period_of_time = data['period_of_time']

    def create_config_file(self):
        config_path = self.sanitize_path("config.json", "FILE")
        log_path = self.sanitize_path("sync.log", "FILE")

        source_path = self.sanitize_path("source", "DIR")
        replica_path = self.sanitize_path("replica", "DIR")

        dict = {
            "period_of_time": 60,
            "log_path": log_path,
            "source_path": source_path,
            "replica_path": replica_path
        }
        config_obj = json.dumps(dict, indent=4)

        with open(config_path, "w") as outfile:
            outfile.write(config_obj)

    def update_from_config(self):
        f = open('config.json', 'r')
        self.data = json.loads(f.read())
        f.close()

    def get_log_path(self):
        return self.data['log_path']

    def get_source_path(self):
        return self.data['source_path']

    def get_replica_path(self):
        return self.data['replica_path']

    def get_period(self):
        return int(self.data['period_of_time'])

    def set_log_path(self, path):
        self.data["log_path"] = self.sanitize_path(path,"FILE")
        self.write_to_config()

    def set_source_path(self, path):
        self.data["source_path"] = self.sanitize_path(path)
        self.write_to_config()

    def set_replica_path(self, path):
        self.data["replica_path"] = self.sanitize_path(path)
        self.write_to_config()

    def set_period_of_time(self, period):
        if int(period) <= 0:
            print("Value of period is incorrect")
            return
        self.data["period_of_time"] = period
        self.write_to_config()

    def sanitize_path(self, path_name, type="DIR"):
        BASE_DIR = os.path.abspath(os.getcwd())

        if BASE_DIR not in path_name:
            path_name = os.path.join(BASE_DIR, path_name)

        if(path.exists(path_name)):
            if (path.isdir(path_name) and type == "DIR"):
                print(f"Dir {path_name} was set!")
                # self.write_to_log(f"Dir {path_name} was set!")
                return path_name

            elif (path.isfile(path_name) and type == "FILE"):
                print(f"Path {path_name} is a file!")
                return path_name

        else:
            if (type == "DIR"):
                print("Try to create new path")
                os.mkdir(path_name)
                print(f"Path {path_name } was set!")
                # self.write_to_log(f"Dir {path_name} was created!")

                return path_name

            elif(type == "FILE"):
                file = open(path_name, "w")
                timestamp = datetime.utcnow()
                file.write(str(timestamp) + ": " +
                           f"File {path_name} was created" + "\n")
                file.close()
                print(f"File {path_name} was created!")

                return path_name

    def write_to_config(self):

        config_obj = json.dumps(self.data, indent=4)
        with open("config.json", "w") as outfile:
            outfile.write(config_obj)
