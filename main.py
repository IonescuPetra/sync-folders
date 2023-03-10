from datetime import datetime
import time
import os
import pathlib
import sys
import argparse

from data import ConfigCustom
from sync_file import SyncronizeFiles
sync_folders = None



# https://www.geeksforgeeks.org/command-line-arguments-in-python/ -> good explanation of args


def get_args():

    cf = ConfigCustom()

    try:
        argument_list = sys.argv[1:]

        if argument_list[0] == "--help" or argument_list[0] == "-h":
            help()

        elif argument_list[0] == "--init" or argument_list[0] == "-i":
            if len(argument_list) == 5:
                source_path = argument_list[1]
                replica_path = argument_list[2]
                log_path = argument_list[3]
                period = argument_list[4]

                init(source_path,replica_path,log_path,period)

            else:
                # global sync_folders
                sync()

        elif argument_list[0] == "--set_period_of_sync":
            period_of_sync = argument_list[1]
            cf.set_period_of_time(period_of_sync)

        elif argument_list[0] == "--run" or argument_list[0] == "-r":
            print("\t\tProgram Start\n")
            run()

        elif argument_list[0] == "--sync_now" or argument_list[0] == "-s":
            sync()

        elif argument_list[0] == "--set_replica_path":
            replica_path = argument_list[1]
            cf.set_replica_path(replica_path)

        elif argument_list[0] == "--set_source_path":
            source_path = argument_list[1]
            cf.set_source_path(source_path)


        elif argument_list[0] == "--set_log_path":
            log_path = argument_list[1]
            cf.set_log_path(log_path)
            
        else:
            print("The command doesn't exist.")

    except Exception as e:
        print(e)


def help():
    help_string = "\n\nUsage main.py COMMAND [ARGS]\n\n"
    help_string += "Options:\n"
    help_string += "\t--init  -i\t\t\t\t -> create a repository in current directory\n"
    help_string += "\t       \t[source] [replica] [log] [period_of_time]\t -> custom arguments. If not provided, it will be default argument\n"

    help_string += "\t--help  -h\t\t\t\t -> helper of this program\n"
    help_string += "\t--run   -r\t\t\t\t -> run this program\n"
    help_string += "\t--sync_now  -s\t\t\t\t -> syncronize replica and source now\n"
    help_string += "\t--set_period_of_sync [integer] \t\t -> set custom period of syncronization, by default 5 minutes\n"
    help_string += "\t--set_replica_path [path] \t\t -> set the path of the replica folder \n"
    help_string += "\t--set_source_path [path] \t\t -> set the path of the source folder \n"
    help_string += "\t--set_log_path [path] \t\t\t -> set the path of the log file. The name will be sync.log \n"

    print(help_string)


def init(source_path:str,replica_path:str,log_path:str,period):
    cf = ConfigCustom()
    cf.set_log_path(log_path)
    cf.set_period_of_time(period)
    cf.set_replica_path(replica_path)
    cf.set_source_path(source_path)
    sync_folders = SyncronizeFiles(
        cf.get_source_path(), cf.get_replica_path(), cf.get_log_path(), cf.get_period())

    sync_folders.sync()


def sync():
    cf = ConfigCustom()
    sync_folders = SyncronizeFiles(
        cf.get_source_path(), cf.get_replica_path(), cf.get_log_path(), cf.get_period())

    sync_folders.sync()


def run():

    cf = ConfigCustom()
    sync_folders = SyncronizeFiles(
        cf.get_source_path(), cf.get_replica_path(), cf.get_log_path(), cf.get_period())

    while(True):

        print(cf.get_source_path(), cf.get_replica_path(),
              cf.get_log_path(), cf.get_period())

        cf.update_from_config()

        sync_folders.set_log_path(cf.get_log_path())
        sync_folders.set_period_of_time(cf.get_period())
        sync_folders.set_replica_path(cf.get_replica_path())
        sync_folders.set_source_path(cf.get_source_path())

        sync_folders.sync()
        time.sleep(cf.get_period())

# Main function


def main() -> None:

    get_args()

    # sync_folders.sync()


if __name__ == "__main__":
    main()
