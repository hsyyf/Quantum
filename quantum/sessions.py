# -*- coding: utf-8 -*-
"""
    author: Q.Y.
"""
import uuid


class Session:
    def __init__(self):
        self.session_id = uuid.uuid1()


session = Session()
