__author__ = "Pablo Leon Alcaide"
#just a little help to find your repositories, can add it to bigger scripts
import subprocess

print 'List of git repositories: '
#you may need to use 'sudo'
subprocess.call('find /home/ -type d -name .git', shell=True)
