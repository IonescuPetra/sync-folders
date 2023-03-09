
from datetime import datetime
import os.path
from os import path


class SyncronizeFiles:

    def __init__(self, source="source", replica="replica", log_path="sync.log", period_of_time=5):

        self.log_file = log_path
        self.source_dir = source
        self.replica_dir = replica
        self.period_of_time = period_of_time

    def get_period_of_time(self):
        return self.period_of_time

    def set_replica_path(self, replica_path):
        self.replica_dir = replica_path

    def set_source_path(self, source_path):
        self.source_dir = source_path

    def set_log_path(self, log_path):
        self.log_file = log_path

    def set_period_of_time(self, period):
        self.period_of_time = period

    def get_files_names(self, filename):
        dict_files = dict()
        files = os.listdir(filename)

        for file in files:
            file_path = path.join(filename, file)
            dict_files[file] = os.stat(file_path).st_mtime

        return dict_files

    def sync(self):
        source_files = self.get_files_names(self.source_dir)
        replica_files = self.get_files_names(self.replica_dir)

        # print(f"Source_files {source_files}")
        # print(f"Replica_files {replica_files}")

        for file in source_files.keys():

            if file not in replica_files.keys():
                check = self.copy_file(file)
                if check:
                    self.write_to_log(
                        f"Failed to create {file} in {self.replica_dir} directory!")
                else:
                    self.write_to_log(
                        f"Creating {file} in {self.replica_dir} directory!")

                    new_file_in_replica = path.join(self.replica_dir, file)
                    replica_files[file] = os.stat(new_file_in_replica).st_mtime

            if source_files[file] != replica_files[file]:
                print(
                    f"File = {file}  {source_files[file]} {replica_files[file]}")

                check = self.copy_file(file)
                if check:
                    self.write_to_log(
                        f"Failed to copy {file} in {self.replica_dir} directory!")
                else:
                    self.write_to_log(
                        f"Copying {file} in {self.replica_dir} directory!")

                    replica_files[file] = source_files[file]

        for file in replica_files.keys():
            if file not in source_files.keys():
                check = self.remove_file(file)
                if check:
                    self.write_to_log(
                        f"Failed to remove {file} in {self.replica_dir} directory!")
                else:
                    self.write_to_log(
                        f"Removing {file} in {self.replica_dir} directory!")

    def remove_file(self, filename):
        file_to_remove = path.join(self.replica_dir, filename)
        check = os.remove(file_to_remove)
        return check

    def copy_file(self, filename):
        source_file = path.join(self.source_dir, filename)
        command = "copy \"" + source_file + "\" \"" + self.replica_dir + "\""
        check = os.system(command)

        return check

    def write_to_log(self, message):
        file = open(self.log_file, "a")
        timestamp = datetime.utcnow()
        file.write(str(timestamp) + ": " + str(message) + "\n")
        file.close()
