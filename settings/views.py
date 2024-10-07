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
    contractor=Contractor.objects.all()
    sector=Sector.objects.all()

    context={
        'contractor':contractor,
        'sector':sector
    }
    return render(request,'settings/contractor.html',context)

def add_contractor(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']

        Contractor.objects.create(
            code=code,
            name=name,
            sector_id=sector,
            project=project,
            item=item,
            notes=notes
        )
        messages.success(request,'تم إضافة مقاول بنجاح مبروووووك')
        return redirect('/settings/contractor')
    
def edit_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']

        code=request.POST['code']
        name=request.POST['name']
        sector=request.POST['sector']
        project=request.POST['project']
        item=request.POST['item']
        notes=request.POST['notes']

        contractor=Contractor.objects.get(id=contractor_id)

        contractor.code=code
        contractor.name=name
        contractor.sector_id=sector
        contractor.project=project
        contractor.item=item
        contractor.notes=notes

        contractor.save()

        messages.success(request,'تم التعديل بنجاح')
        return redirect('/settings/contractor')





def delete_contractor(request):
    if request.method=='POST':
        contractor_id=request.POST['id']

        contractor=Contractor.objects.get(id=contractor_id)

        contractor.delete()

        messages.success(request,'تم الحذف بنجاح مبرووك')
        return redirect('/settings/contractor')


def document_type(request):
    document_type=Document_Type.objects.all()
    context={
        'document_type':document_type
    }

    return render(request,'settings/document_type.html',context)

def add_document_type(request):
    if request.method=='POST':
        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        Document_Type.objects.create(
            code=code,
            name=name,
            notes=notes
        )
        messages.success(request,'تم إضافة مستند جديد بنجاح')
        return redirect('/settings/document_type')
    
def delete_document_type(request):
    if request.method=='POST':
        document_id=request.POST['id']
        document_type=Document_Type.objects.get(id=document_id)
        document_type.delete()
        messages.success(request,'مبروك تم الحذف بنجاح')
        return redirect('/settings/document_type')
    
def edit_document_type(request):
    if request.method=='POST':
        document_type_id=request.POST['id']

        code=request.POST['code']
        name=request.POST['name']
        notes=request.POST['notes']

        document_type=Document_Type.objects.get(id=document_type_id)

        document_type.code=code
        document_type.name=name
        document_type.notes=notes
        document_type.save()

        messages.success(request,'تم التعديل بنجاج')
        return redirect('/settings/document_type')



