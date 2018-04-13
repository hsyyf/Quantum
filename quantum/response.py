# -*- coding: utf-8 -*-
"""
    author: Q.Y.
"""
from json import dumps

from aiohttp.web import Response as BaseResponse
from aiohttp.web import FileResponse as BaseFileResponse

from quantum import __version__, __sever_name__


class Response(BaseResponse):
    def __init__(self, *args, **kwargs):
        super(Response, self).__init__(*args, **kwargs)
        self.headers["Server"] = "{} {}".format(__sever_name__, __version__)


def text(body=None, status=200, reason=None, headers=None, content_type="text/plain", charset="utf-8"):
    if not isinstance(body, str):
        raise TypeError
    return Response(body=body, status=status, reason=reason, headers=headers, content_type=content_type,
                    charset=charset)


def json(body=None, status=200, reason=None, headers=None, content_type="application/json", charset="utf-8"):
    if not isinstance(body, dict):
        raise TypeError
    return Response(body=dumps(body), status=status, reason=reason, headers=headers, content_type=content_type,
                    charset=charset)


def xml(body=None, status=200, reason=None, headers=None, content_type="text/xml", charset="utf-8"):
    return Response(body=body, status=status, reason=reason, headers=headers, content_type=content_type,
                    charset=charset)


def html(body=None, status=200, reason=None, headers=None, content_type="text/html", charset="utf-8"):
    return Response(body=body, status=status, reason=reason, headers=headers, content_type=content_type,
                    charset=charset)


def file(location, status=200, reason=None, headers=None, filename=None):
    headers = headers or {}
    if filename:
        headers["Content-Disposition"] = "attachment; filename='{}'".format(filename)
    return BaseFileResponse(path=location, status=status, reason=reason, headers=headers)
