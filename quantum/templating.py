# -*- coding: utf-8 -*-
"""
    author: Q.Y.
"""
from jinja2 import Environment as BaseEnvironment, TemplateNotFound, PackageLoader, select_autoescape
from .response import html


class Environment(BaseEnvironment):
    def __init__(self, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)


env = Environment(
    loader=PackageLoader(package_name=__name__, package_path='../templates/'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']))


def template(tpl, **kwargs):
    try:
        templates = env.get_template(tpl)
        return html(templates.render(kwargs))
    except TemplateNotFound as err:
        raise TemplateNotFound(err)
    except Exception as err:
        raise Exception(err)
