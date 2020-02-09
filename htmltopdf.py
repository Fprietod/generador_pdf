from passlib.context import CryptContext
# Renderizar HTML
from bottle import SimpleTemplate
# PDF
import pdfkit
# QR
try:
	import qrcode
except ImportError:
	qrcode = None
try:
	import base64
except ImportError:
	base64 = None
from io import BytesIO



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
# Genera el codigo QR
url_server = "http://www.google.com.mx"
url_certificado = url_server + "HOla a todos"+"esta funcionando"
qr = qrcode.QRCode(
	version=1,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=20,
	border=2,
)
qr.add_data(url_certificado)
qr.make(fit=True)
img = qr.make_image()
temp = BytesIO()
img.save(temp, format="PNG")
qr_img = base64.b64encode(temp.getvalue())

parameters = {
	'nombre': "Felipe Prieto de la Cruz",
	'cargo' : "Presiente",
	'fecha' : "15/02/2019",
	'firma' : "Felipe Prieto de la Cruz",
	'firma_director' : "HOla",
	'qr_code' : qr_img,
}

html = render_template(file, parameters)
pdf = pdfkit.from_string(html,'out.pdf')
#pdf = pdfkit.from_string(html, False, options=options)
print(type(pdf))