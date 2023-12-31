# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  
import io 
from html import escape

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     ##result = io.BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
   #   pdf = pisa.pisaDocument(io.BytesIO (html.encode("utf-8")), result)
     
     if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

    #  if not pdf.err:
    #      return HttpResponse(result.getvalue(), content_type='application/pdf')
    #  return None