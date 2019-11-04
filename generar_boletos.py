from fpdf import FPDF

import datetime
x = datetime.datetime.now()
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

fecha_x = [60,160,180]
fecha_y = [15,30,100,140]
pos_x = [[15,30,45],[15,30,45],[15,30,45],[15,30,45]]
pos_y = [10,50,130,180]
#iteramos segun las filas solicitadas
while i != paginas:
	pdf.add_page()
	pdf.image('fondo.png',0,0, 216, 279)
	#son las posiciones en las que nos vamos a mover para poner los numeros
	for k in range(len(pos_y)):
		pdf.set_font('Arial', 'B', 16)
		for w in range(len(pos_x[k])):
			pdf.set_xy(pos_x[k][w],pos_y[k])
			print(repr(pos_x[k][w])+"-"+repr(pos_y[k]))
			pdf.multi_cell(40, 10, repr(folio))
			folio = folio+1

		pdf.set_font('Arial', 'B', 10)
		for w in range(len(fecha_x)):
			pdf.set_xy(fecha_x[w],fecha_y[k])
			print(repr(fecha_x[w])+"-"+repr(fecha_y[k]))
			pdf.multi_cell(40, 10, x.strftime("%d"+"/"+"%m"+"/"+"%Y"))
	i=i+1

file = open('salida.txt','w+')
file.write('$$$ '+x.strftime("%d"+"/"+"%m"+"/"+"%Y")+' $$$ \n')
file.write('Se han generado '+repr(paginas)+' con folio de: '+repr(folio_inicial)+' a '+repr(folio-1)+' \n')

pdf.output('tuto1.pdf', 'F')