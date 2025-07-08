from asyncio import gather
from logger import *
from req.hardware import RequestExec
from req.software import ProgramExec

__METHODS__ = [
    ('os', 'caption'),
    ('cpu', 'Name'),
    ('memorychip', 'Capacity'),
    ('path win32_VideoController', 'Name'),
    ('diskdrive', 'Size')
]

class RequestCollector:
    def __init__(self, host):
        self.__host__ = host
        self.__requests__ = []
        self.__results__ = {}

    async def execute_gather(self):
        await self._create_request()
        await gather(
            *[self._exec(request) for request in self.__requests__]
        )
        return 0

    def get_results(self):
        return self.__results__

    async def _create_request(self):
        for count, (method, attrib) in enumerate(__METHODS__):
            request = RequestExec(
                dname=self.__host__,
                method=method,
                attrib=attrib,
                count=count
            )
            self.__requests__.append(request)
        self.__requests__.append(
            ProgramExec(dname=self.__host__)
        )

    async def _exec(self, request):
        method = request._runScript()
        result = request._getResults()
        self.__results__[method] = result
        logger.info(f"RESULTS: {self.__results__}")