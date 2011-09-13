# -*- coding: utf-8 -*-
"""Base interfaces and schemas"""

from zope.interface import Interface

from zope.i18nmessageid import MessageFactory
_ = MessageFactory("shaura_example")


class IApplication(Interface):
    """Pseudo root object factory"""

    def __call__(request):
        """Root object is initialized with request"""
        pass
