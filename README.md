# sync-folders

Usage main.py COMMAND [ARGS]

Options:
--init -i -> create a repository in current directory
[source] [replica] [log] [period_of_time] -> custom arguments. If not provided, it will be default argument
--help -h -> helper of this program
--run -r -> run this program
--sync_now -s -> syncronize replica and source now
--set_period_of_sync [integer] -> set custom period of syncronization, by default 5 minutes
--set_replica_path [path] -> set the path of the replica folder
--set_source_path [path] -> set the path of the source folder
--set_log_path [path] -> set the path of the log file. The name will be sync.log
