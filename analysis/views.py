# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def analysis(request):
    return render(request, 'analysis.html')


@login_required
def analysishis(request):
    return render(request, 'analysis_his.html')
