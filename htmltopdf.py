from passlib.context import CryptContext
# Renderizar HTML
from bottle import SimpleTemplate
# PDF
import pdfkit



def render_template(html_file, datos):
	template = open(html_file, "r")
	tpl = SimpleTemplate(template)
	return tpl.render(datos)


options = {
	'page-size': 'Letter',
	'orientation' : 'Landscape',
	'margin-top': '0.1in',
	'margin-right': '0.1in',
	'margin-bottom': '0.1in',
	'margin-left': '0.1in',
	'encoding': "UTF-8",

}

module_path = ""
file = module_path + "index.html"

parameters = {
	'nombre': "Felipe Prieto de la Cruz",
	'cargo' : "Presiente",
	'fecha' : "15/02/2019",
}

html = render_template(file, parameters)

pdf = pdfkit.from_string(html, False, options=options)
print(type(pdf))