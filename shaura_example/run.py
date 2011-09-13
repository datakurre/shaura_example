# -*- coding: utf-8 -*-
"""WSGI runner"""

import pyramid_zcml

from pyramid.config import Configurator
from shaura_example.app import Application


def wsgi_app(**settings):
  config = Configurator(root_factory=Application, settings=settings, autocommit=True)
  config.include(pyramid_zcml)
  config.load_zcml("shaura_gae:configure.zcml")
  config.load_zcml("shaura:configure.zcml")
  config.load_zcml("configure.zcml")
  return config.make_wsgi_app()
