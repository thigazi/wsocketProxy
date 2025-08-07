from time import sleep
from sys import argv
from psutil import Process
import pidfile
from yaml import load, FullLoader
from os.path import join
from pathlib import Path


class Apploader(object):
    def __init__(self):
        current_path = Path(__file__).parent
        with open(join(current_path, 'config.yaml'), 'r') as fcfg:
            self.__yaml_cfg = load(fcfg, Loader=FullLoader)

    def Task(self, task_action):
        action_methods = {'start': self.__startUp, 'stop': self.__shutDown}
        action_methods[task_action]()

    def __startUp(self):
        try:
            with pidfile.PIDFile(self.__yaml_cfg['PidFileLocation']):
                print('Process started.')
                sleep(1000)

        except pidfile.AlreadyRunningError:
            print('Process is already running.')

    def __shutDown(self):
        with open(self.__yaml_cfg['PidFileLocation'], 'r') as pid_file:
            Process(int(pid_file.read())).terminate()


if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == 'start':
            Apploader().Task(task_action='start')
        if argv[1] == 'stop':
            Apploader().Task(task_action='stop')
