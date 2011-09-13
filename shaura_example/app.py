# -*- coding: utf-8 -*-
"""Application root and root views"""

import os

from zope.interface import implements

from shaura.interfaces import ICollection
from shaura.response import Response

from shaura_example.interfaces import IApplication


class Application(object):
    """Response non-persistent root object"""
    implements(IApplication)

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        """Looks up for named collection multiadapters to find
        some children for this non-persistent root object"""
        registry = self.request.registry
        try:
            return registry.getAdapter(self, ICollection, name=key)
        except:
            raise KeyError(key)


###
# Special root attached views

here = os.path.dirname(__file__)

main_data = open(os.path.join(here, "index.html")).read()
main_response = Response(main_data, "text/html")

favicon_data = open(os.path.join(here, "favicon.ico")).read()
favicon_response = Response(favicon_data, "image/x-icon")

robots_data = open(os.path.join(here, "robots.txt")).read()
robots_response = Response(robots_data, "text/plain")


def main(context, request):
    return main_response


def favicon(context, request):
    return favicon_response


def robots(context, request):
    return robots_response
