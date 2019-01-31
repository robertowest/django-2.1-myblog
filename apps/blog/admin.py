# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Comment, Message, Profile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Profile)
