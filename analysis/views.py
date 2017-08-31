# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dbinfo.models import DBinfo


# Create your views here.
@login_required
def analysis(request):
    dbinfos = DBinfo.objects.all()
    return render(request, 'analysis.html', locals())


@login_required
def analysishis(request):
    return render(request, 'analysis_his.html')
