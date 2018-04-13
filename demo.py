# -*- coding: utf-8 -*-
"""
    author: Q.Y.
"""

from quantum import Quantum
from quantum.response import json, file
from quantum.templating import template

app = Quantum(__name__)


@app.route("/favicon.ico", method="GET")
async def favicon(request):
    return file("templates/index.html")


@app.route("/", method="GET")
async def index(request):
    return json({"code": 1})


@app.route("/{url}", method="GET")
async def get_url(request):
    # return xml({"url": request.match_info.get("url", None)})
    return template("index.html", h2_title=request.match_info.get("url", None))


if __name__ == "__main__":
    app.run()
