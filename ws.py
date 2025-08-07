import asyncio
from websockets.asyncio.server import serve

class WSProxyHandler(object):
    def __init__(self,yml_cfg):
        self.__yml_cfg = yml_cfg

    def __wsocketHandler(self):
        pass
