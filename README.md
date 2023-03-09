# sync-folders

Usage main.py COMMAND [ARGS]

Options:

&emsp;--init -i -> create a repository in current directory

&emsp;&emsp;&emsp;&ensp;[source] [replica] [log] [period_of_time] -> custom arguments. If not provided, it will be default argument

&emsp;--help -h -> helper of this program

&emsp;--run -r -> run this program

&emsp;--sync_now -s -> syncronize replica and source now

&emsp;--set_period_of_sync [integer] -> set custom period of syncronization, by default 1 minute. The number entered must be in seconds.

&emsp;--set_replica_path [path] -> set the path of the replica folder

&emsp;--set_source_path [path] -> set the path of the source folder

&emsp;--set_log_path [path] -> set the path of the log file. The name will be sync.log

```python
#Examples of how to use this tool
python main.py -h
python main.py --help
python main.py -s #sync now
python main.py --set_log_path "sync2.log"
python main.py --set_period_of_sync 30
python main.py -r #to run continuously
```
