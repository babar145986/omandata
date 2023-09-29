from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import AddRecord
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/admin')
def view_record(request):
	all_records = AddRecord.objects.all()
	context = {'all_records': all_records}
	return render(request, 'view_record.html', context)

def single_record_information(request, pk):
	get_record = AddRecord.objects.get(id=pk)
	context = {'get_record': get_record}
	return render(request, 'info.html', context)

def noor_ul_ship(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'noor_ul_shipa.html', context)

def al_gharbia(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'al_gharbia.html', context)

def badr_al_sama(request, pk):
    get_record = AddRecord.objects.get(id=pk)
    context = {'get_record': get_record}
    return render(request, 'badr_al_sama.html', context)

def confirm_print(request, pk):
	get_record = AddRecord.objects.get(id=pk)
	context = {'get_record': get_record}
	return render(request, 'confirm_print.html', context)

def al_razi(request, pk):
	get_record = AddRecord.objects.get(id=pk)
	context = {'get_record': get_record}
	return render(request, 'confirm_print_2.html', context)