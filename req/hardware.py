from scripts import HardExec
import subprocess as sp
from os import remove
from logger import *

class RequestExec:
    def __init__(self, dname=None, method=None, attrib=None, count=0):
        self.__method = method
        self.__dname = dname
        self.__attrib = attrib
        self.__tname = self.__class__.__name__ + count.__str__()
        self.__data = None

        HardExec(self.__tname, dname, method, attrib)._gen()
        self.__file = self.__tname + '.bat'
        self.__rfile = self.__tname + '.log'
        logger.info(f'{self.__file} created')

    def _runScript(self):
        try:
            sp.run(f'{self.__file}', shell=True)
            logger.info(f'{self.__file} executed')
            return self.__method
        except Exception as e:
            logger.info(f'Script did not execute. Error:{e}.')

    def _getResults(self):
        file = open(self.__rfile, 'r', encoding='ISO-8859-5')
        self.__data = map(lambda string: string.encode('ascii', errors='ignore').decode('ascii').replace('\n', ''), file.readlines())
        ans = []
        for line in self.__data:
            if line != ' ':
                ans.append(line)
        file.close()
        remove(self.__file)
        remove(self.__rfile)
        logger.info(f"Thread {self.__tname} removed temp files")
        return ans