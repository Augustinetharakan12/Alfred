from reportlab.lib import colors
from reportlab.lib.pagesizes import letter,inch,A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from  reportlab.lib.styles import ParagraphStyle as PS

# c = canvas.Canvas("sample.pdf");
# c.drawString(150,200,"Halalal");
# c.save()
def generatepdf(win):
	s=win[0].event
	filename=s+"-shortlisted.pdf"

	data=[['EXCELID','NAME']]
	doc = SimpleDocTemplate(filename, pagesize=A4)
	elements = []
	centered = PS(name = 'centered',
		fontSize = 25,
		leading = 16,
		alignment = 1,
		spaceAfter = 30,
		)
	for obj in win:
		data.append([obj.excelid,obj.name])
	t=Table(data,2*[2*inch], len(data)*[0.3*inch])
	t.setStyle(TableStyle([
		('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
		('BOX', (0,0), (-1,-1), 0.25, colors.black),
		('TEXTCOLOR',(0,0),(-1,0),colors.green),
		]))
	k="<b>"
	k=k+obj.event+"-SHORTLIST"
	k=k+"</b>"
	elements.append(Paragraph(k,centered))
	elements.append(t)
	doc.build(elements)

 

	

win=winners.objects.all()
generatepdf(win)

