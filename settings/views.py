from django.shortcuts import render,redirect
from .models import Sector,Document_Type,Contractor
from django.contrib import messages

def base(request):
    return render(request,'base.html',{})


# sector functions
def sector(request):
    sectors=Sector.objects.all()
    context={
        'sectors':sectors
    }
    return render(request,'settings/sector.html',context)

def add_sector(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Sector.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'ok done add sector ')
        return redirect('/settings/sector')
    
def delete_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        sector=Sector.objects.get(id=sector_id)

        sector.delete()
        messages.success(request,'تم حذف هذا لقطاع بنجاح مبروووك')
        return redirect('/settings/sector')
    
def edit_sector(request):
    if request.method=='POST':
        sector_id=request.POST['id']
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        sector=Sector.objects.get(id=sector_id)
        sector.code=code
        sector.name=name
        sector.notes=notes

        sector.save()

        messages.success(request,'مبرووووووك تم التعديل بنجاج')
        return redirect('/settings/sector')


       

def contractor(request):
    return render(request,'settings/contractor.html',{})

def document_type(request):
    return render(request,'settings/document_type.html',{})
