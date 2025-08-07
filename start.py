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
        if task_action == 'start':
            try:
                with pidfile.PIDFile(self.__yaml_cfg['PidFileLocation']):
                    print('Process started.')
                    sleep(1000)

            except pidfile.AlreadyRunningError:
                print('Process is already running.')

        elif task_action == 'stop':
            with open(self.__yaml_cfg['PidFileLocation'],'r') as pid_file:
                pid_process = Process(int(pid_file.read()))
                pid_process.terminate()

    def __startUp(self):
        pass

    def __shutDown(self):
        pass


if __name__ == '__main__':
    print(argv)
    if len(argv) == 2:
        if argv[1] == 'start':
            Apploader().Task(task_action='start')
        if argv[1] == 'stop':
            Apploader().Task(task_action='stop')
