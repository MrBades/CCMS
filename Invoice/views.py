from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import render, redirect
from html2image import Html2Image
from .process import html_to_pdf 
from datetime import date
hti = Html2Image()
from ccmsMain.models import *
from .models import *
import json
from .forms import Invoiceform

# Create your views here.
def invoice(request):
    return render(request, "Invoice/invoiceIndex.html", {"invoices":Invoice.objects.all()})

def generate(request):  
    bank = Bank_Details.objects.all()
    return render(request, 'Invoice/generate.html', {'today': date.today(), 'bank':bank})

def IIEdit(request, id):
    IF = Invoiceform(request.POST)
    I = Invoice.objects.get(id=id)
    if IF.is_valid():
        I.Customer_Name = IF.cleaned_data.get('Customer_Name')
        I.Order_Date = IF.cleaned_data.get('Order_Date')
        I.Due_Date = IF.cleaned_data.get('Due_Date')
        I.Phone = IF.cleaned_data.get('Phone')
        I.AW = IF.cleaned_data.get('AW')
        I.Orders = IF.cleaned_data.get('Orders')
        I.Count = IF.cleaned_data.get('Count')
        I.Curency = IF.cleaned_data.get('Curency')
        I.Amount = IF.cleaned_data.get('Amount')
        I.Shipping = IF.cleaned_data.get('Shipping')
        I.Subtotal = IF.cleaned_data.get('Subtotal')
        I.NameId = IF.cleaned_data.get('VAT')
        I.VAT = IF.cleaned_data.get('Customer_Name')
        I.Total = IF.cleaned_data.get('Total')
        I.save()
    return render(request, "Invoice/edit.html", {"invoice":I, "IF":Invoiceform, "id":id})
    
    

def IISave(request, id, name:str, phone:str, orders:str, count:str, total:str, aw:str, DD:str, shipping:str, Cur:str):
    redirect("/delete/{id}/NONE")
    totals = json.loads(total)
    curency = CUR.objects.get(name = Cur)
    update = Invoice.objects.get(id=id)
    update.Customer_Name = name,
    # update.Phone = phone,
    # update.AW = aw,
    # # update.Orders = orders,
    # update.Count = count,
    # update.Due_Date = DD,
    # Curency = curency,
    # update.Amount = '0',
    # update.Shipping = shipping,
    # update.Subtotal = totals['subT'],
    # update.NameId = name+id,
    # update.VAT = totals['VAT'],
    # update.Total = totals['mainT']
    update.save()
    # return HttpResponse(name + '\'s Updated <br> <a href="http://127.0.0.1:8000/">Back to Main</a>')
    return HttpResponse(name + " " + update.Customer_Name)

def IIView(request, id:int):
    orderdic = json.loads(Invoice.objects.get(id=id).Orders)
    bank = Bank_Details.objects.all()
    return render(request, "Invoice/view.html", {"invoice":Invoice.objects.get(id=id), "orders":orderdic, "bank":bank, "id":id})

def IIDelete(request, id, action):
    if action == "YES":
        invoice = Invoice.objects.get(id = id)
        invoice.delete()
        return redirect('/invoice')

    return render(request, "Invoice/delete.html", {"ID":id, "invoice":Invoice.objects.get(id=id)})


def genPDFInvoice(request, name:str, phone:str, orders:str, count:str, total:str, aw:str, DD:str, shipping:str, Cur:str):
    curen = {'Dollars': "USD", 'Naira':"NGN", 'Pound':"GBP", 'Euro':"EU", 'Canadian Dollars':"CAD", 'Australian Dollar':"AUD"}
    bank = Bank_Details.objects.all()
    totals = json.loads(total)
    orderdic = json.loads(orders)
    curency = CUR.objects.get(name = curen[Cur])
    
    Invoice.objects.create(
                Customer_Name = name,
                Order_Date = date.today(),
                Phone = phone,
                AW = aw,
                Orders = orders,
                Count = count,
                Due_Date = DD,
                Curency = curency,
                Amount = '0',
                Shipping = shipping,
                Subtotal = totals['subT'],
                NameId = models.CharField(max_length=1000, null=True, default='non'),
                VAT = totals['VAT'],
                Total = totals['mainT']
        )
    data = {
        'today': date.today(), 
        'customer_name': name,
        "phone": phone,
        "dueDate":DD,
        "curency": Cur,
        "shipping": shipping,
        "orders": orderdic,
        "count": count,
        "totals": totals,
        "AW":aw,
        "bank":bank,
    }

    pdf1 = html_to_pdf('pdfInvoice2.html', data)

    response = HttpResponse(pdf1, content_type='application/pdf') 
    st = 'attachment; filename="{}\'s invoice.pdf"'
    response['Content-Disposition'] = st.format(name)  
    return response
    # return HttpResponse(curency)

def printPDF(request, id):
    invoice = Invoice.objects.get(id=id)
    orderdic = json.loads(invoice.Orders)
    name = invoice.Customer_Name
    totals = {
            "subT":invoice.Subtotal,
            "VAT":invoice.VAT,
            "mainT":invoice.Total,
                }
    data = {
        'today': date.today(), 
        'customer_name': name,
        "phone": invoice.Phone,
        "dueDate": invoice.Order_Date,
        "curency": invoice.Due_Date,
        "shipping": invoice.Shipping,
        "orders": orderdic,
        "count": invoice.Count,
        "totals": totals,
        "AW": invoice.AW,
        "bank": Bank_Details.objects.all(),
    }

    pdf1 = html_to_pdf('pdfInvoice2.html', data)

    response = HttpResponse(pdf1, content_type='application/pdf') 
    st = 'attachment; filename="{}\'s invoice.pdf"'
    response['Content-Disposition'] = st.format(name)  
    return response


def genIMG(request, ni:str, id:int):
    LogoPurpose = Purpose.objects.get(name = "Logo")
    logo = WebsiteResources.objects.get(Purpose = LogoPurpose)
    ClientO = ClientOrder.objects.get(id = id)
    nameId = ClientO.Client_Name + id
    invoice = Invoice.objects.get(NameId= nameId)
    bank = Bank_Details.objects.all()
    data = {
        'today': date.today(), 
        'amount': ClientO.Client_C_Number,
        'customer_name': ClientO.Client_Name,
        "details": ClientO.Design_Details,
        "invoice": invoice,
        "bank":bank
    }

    return render(request, 'imgInvoice.html', data)
  # return redirect(url)

def genIMGInvoice(request, ni:str, id:int):
  ClientO = ClientOrder.objects.get(id = id)
  hti.screenshot(url='http://127.0.0.1:8000/gImg/' + ni + '/' + str(id), save_as='invoice.png', size = (1040, 620))
  img = open("invoice.png", 'rb')
  response = FileResponse(img)
  response['Content-Disposition'] = img
  url='http://127.0.0.1:8000/gImg/' + ni + '/' + str(id)

  response = HttpResponse(img, content_type='image/png') 
  documentDes = 'attachment; filename= "{}\'s invoice.png"' 
  response['Content-Disposition'] = documentDes.format(ClientO.Client_Name)
  return response

from xhtml2pdf import pisa  # importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

def myPDF(request):
    data = {
        'today': date.today(), 
        'customer_name': 'name',
        "phone": 'phone',
        "dueDate":'DD',
        "curency": 'Cur',
        "shipping": 'shipping',
        "orders": 'orderdic',
        "count": 'count',
        "totals": 'totals',
        "AW":'aw',
        "bank":'bank',
    }
    response = HttpResponse(content_type='application/pdf') 
    st = 'attachment; filename="{}\'s invoice.pdf"'
    response['Content-Disposition'] = st.format("name")  
    template = get_template('pdfInvoice2.html')
    html  = template.render(data)

    pisa_status = pisa.CreatePDF(
        html, dest=response, link="static link")