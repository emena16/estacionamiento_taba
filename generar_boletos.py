from fpdf import FPDF
import datetime
fecha = datetime.date.today()
#Creamos el objeto pdf que es quien se encargara de dibujar el PDF
pdf = FPDF()
folio_inicial = int(input("Ingresa folio inicial: "))
folio = folio_inicial

paginas = int(input("Numero de paginas necesarias: "))
#igualamos a 1 pagina en caso de que no se haya ingresado el numero de pag paginas.
if paginas < 1:
	paginas = 1;

pdf.set_font('Arial', 'B', 16)
i= k = 0
fecha = []
pos_x = [[15,30,45],[15,30,45],[15,30,45],[15,30,45]]
pos_y = [10,20,30,40]
#iteramos segun las filas solicitadas
while i != paginas:
	pdf.add_page()
	pdf.image('fondo.png',0,0, 216, 279)
	#son las posiciones en las que nos vamos a mover para poner los numeros
	for k in range(len(pos_y)):
		for w in range(len(pos_x[k])):
			pdf.set_xy(pos_x[k][w],pos_y[k])
			print(repr(pos_x[k][w])+"-"+repr(pos_y[k]))
			pdf.multi_cell(40, 10, repr(folio))
			folio = folio+1
	i=i+1


# pdf.set_xy(25, 10)
# pdf.multi_cell(40, 10, 'Hello World!',)
# pdf.set_xy(40, 62)
# pdf.multi_cell(40, 10, 'Hello World!',)
pdf.output('tuto1.pdf', 'F')