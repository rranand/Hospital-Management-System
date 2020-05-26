from fpdf import FPDF
from .models import p_payment
import os


def create_invoice(id):
    pat = p_payment.objects.get(id=id)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    string = ['HMS', 'Invoice', str('Patient Name: ' + str(pat.pat.user.get_full_name())), str('Bill: Rs ' + str(pat.outstanding))]
    for x in string:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    name = 'invoice'+str(pat.id)+'.pdf'
    path = os.path.join(os.getcwd(), os.path.join('media', 'invoices'))
    os.chdir(path)
    if os.path.exists(path+name):
        os.remove(path + name)
    pdf.output(name)
    return [path, name]
