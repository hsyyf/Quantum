# -*- coding: utf-8 -*-
"""
    author: Q.Y.
"""

import asyncio

from aiohttp import web


class Quantum:
    def __init__(self, name, loop=None):
        self.name = name
        if not loop:
            self.loop = asyncio.get_event_loop()
        self._app = web.Application(loop=self.loop)
        self.config = None

    def run(self, host=None, port=None):

        if not self.config:
            self.config = {}

        if not host:
            host = self.config.get("host", None) or "127.0.0.1"

        if not port:
            port = self.config.get("port", None) or 9000

        self.loop.run_until_complete(
            self.init_start(self.loop, host=host, port=port))
        self.loop.run_forever()

    async def init_start(self, _loop, host, port):
        await _loop.create_server(self._app.make_handler(), host=host,
                                  port=port)
        print('Server started at http://{}:{}...'.format(host, port))

    def route(self, url, method=None):
        if not method:
            method = "GET"

        def wrapper(func):
            self._app.router.add_route(method, url, func)
            return func

        return wrapper
