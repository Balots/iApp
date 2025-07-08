from scripts import SoftExec
import subprocess as sp
from os import remove
from logger import *
import re

class ProgramExec:
    def __init__(self, dname=None):
        self.__dname = dname
        self.__tname = self.__class__.__name__
        self.__data = None

        SoftExec(self.__tname, self.__dname)._gen()
        self.__file = self.__tname + '.bat'
        self.__rfile = self.__tname + '.log'
        logger.info(f'{self.__file} created')

    def _runScript(self):
        try:
            sp.run(f'{self.__file}', shell=True)
            logger.info(f'{self.__file} executed')
            return 'Soft'
        except Exception as e:
            logger.info(f'Script did not execute. Error:{e}.')

    def _getResults(self):
        file = open(self.__rfile, 'r', encoding='ISO-8859-5')
        self.__data = map(lambda string: string.encode('ascii', errors='ignore').decode('ascii').replace('\n', ''), file.readlines())
        ans = set()
        pattern = r"\\Uninstall\\([^\\]+)$"
        for line in self.__data:
            if line == ' ':
                continue
            try:
                line = line.replace('\n', '')
                logger.info(f'Start line: \n <{line}>')
                match = re.search(pattern, line)
                program = match.group(1)
                logger.info(f'Captured program: {program}')
                if program[0] == '{':
                    tmp = sp.run(['bat\\GUID.bat'], input=program, capture_output=True, text=True)
                    program = tmp.stdout
                if line != '': ans.add(program.replace('\n', ''))
            except Exception as e:
                logger.info(f'Parsing error: {e} in line: \n<{line}>')
        file.close()
        remove(self.__file)
        remove(self.__rfile)
        logger.info(f"Thread {self.__tname} removed temp files")
        return list(ans)