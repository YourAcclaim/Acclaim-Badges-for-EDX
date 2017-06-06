# -*- coding: utf-8 -*-
"""
URLs for acclaim_badges.
"""
from __future__ import absolute_import, unicode_literals
from django.contrib.auth.decorators import login_required

from django.conf.urls import url
from django.views.generic import TemplateView
# from lms.djangoapps.acclaim_badges import views
from .views import BadgeCourseList
from .views import BadgeCourseCreate
from .views import BadgeCourseDelete
from .views import BadgeCourseUpdate

from .views import AcclaimTokenList
from .views import AcclaimTokenCreate
from .views import AcclaimTokenDelete
from .views import AcclaimTokenUpdate

urlpatterns = [
    url(r'^tokens/', AcclaimTokenList.as_view(), name='acclaim-tokens'),
    url(r'^token/add/$', AcclaimTokenCreate.as_view(), name='acclaim-token-add'),
    url(r'^token/update/(?P<pk>[0-9]+)/$', AcclaimTokenUpdate.as_view(), name='acclaim-token-update'),
    url(r'^token/delete/(?P<pk>[0-9]+)/$', AcclaimTokenDelete.as_view(), name='acclaim-token-delete'),

    url(r'badge-course/add/$', BadgeCourseCreate.as_view(), name='badge-course-add'),
    url(r'^badge-courses/$', BadgeCourseList.as_view(), name='badge-courses'),
    url(r'^badge-course/delete/(?P<pk>[0-9]+)/$', BadgeCourseDelete.as_view(), name='badge-course-delete'),
    url(r'^badge-course/update/(?P<pk>[0-9]+)/$', BadgeCourseUpdate.as_view(), name='badge-course-update'),
]
