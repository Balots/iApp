from pydantic import BaseModel
from typing import Optional

class BatchScript(BaseModel):
    script_name: str
    commands: list[str]
    variables: Optional[dict[str, str]] = None

class BatchGen:
    def __init__(self, name:str, variables:list[str], commands:list[str]):
        self._config = BatchScript(
        script_name=f'{name}.bat',
        variables={"logfile": f'{variables[0]}.log'},
        commands = commands,
        )

    def _gen(self):
        content = ["@echo off\n",
                   'chcp 65001 > nul\n',
                   'setlocal enabledelayedexpansion\n']

        # Добавляем переменные
        if self._config.variables:
            for key, value in self._config.variables.items():
                content.append(f"set {key}={value}\n")

        # Добавляем команды
        content.extend(self._config.commands)

        # Формируем bat-скрипт
        with open(self._config.script_name, "w") as f:
            f.writelines(content)

        return self._config.script_name[:-3]

class HardExec(BatchGen):
    def __init__(self, name, hostname, method, attrib):
        super().__init__(name, [name], commands=[
            f'for /f \"tokens=2 delims==" %%A in (\'psexec \\\\{hostname} wmic {method} get {attrib} /value\') do (\n',
            f'\tset "RESULT=%%A"\n',
            f'\techo !RESULT! >> "%logfile%"\n',
            ')\n',
            'exit /b 0'
        ])
        self.__method = method

class SoftExec(BatchGen):
    def __init__(self, name, hostname):
        super().__init__(name, [name], commands=[
            f'psexec \\\\{hostname} reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall >> "%logfile%"\n',
            f'psexec \\\\{hostname} reg query HKLM\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall >> "%logfile%"\n',
            'exit /b 0'
        ])

if __name__=='__main__':
    HardExec('test', 'upr5-temp', 'os', 'caption')._gen()