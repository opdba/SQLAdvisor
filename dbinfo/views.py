# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import DBCreate
from .models import DBinfo
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
@login_required
def dbsettings(request):
    if request.method == 'POST':
        form = DBCreate(request.POST)

        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = User.objects.get(username="wangchao")
            bet.save()

    dbinfos = DBinfo.objects.all()
    return render(request, 'settings.html',locals())


@login_required
def validate_item_name(request):
    if request.method == 'POST':
        valid = True
        itemName = request.POST.get('itemName')
        dbinfo_count = DBinfo.objects.filter(db_name=itemName).count()
        if dbinfo_count > 0:
            valid = False
        return JsonResponse({'valid': valid})
    else:
        return HttpResponse("wrong http request mothod")
