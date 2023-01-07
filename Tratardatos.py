import csv
import numpy as np
from datetime import datetime, timedelta


# ARCHIVOS DE ENTRADA ------------------------------------------------------------------------------------------

with open('/home/juan/Ayapel/Datos/IDEAM/Dir_Viento/brutos/San_Bern_Viento.csv','r') as file:
	reader = csv.reader(file)
	datai = [data for data in reader]
data = np.asarray(datai)

# EXTRAER LOS DATOS QUE SE NECESITEN ---------------------------------------------------------------------------

f,c = np.shape(data)
Nam = []
Dat = []


for i in range(f):
	if data[i,0] == '13070010' and data[i,13] == 'DVAG_CON':
		n = float(data[i,17])
		d = data[i,16]
		md = datetime.strptime(d,"%Y-%m-%d %H:%M")   # Esto convierte el formato de datos a formato de fechas de python (datetime)
		Dat.append(md)
		Nam.append(n)
#print(Dat)

# Introducimos los datos dentro de un arreglo Numpy para evitar errores de listas

# Tratemos de manejar fechas -----------------------------------------------------------------------------------

#r = pd.date_range(start='2001-05-16 12:00',end='2008-07-03 21:00',freq='1H')

#start = datetime(2010,1,1,0,0)
#end = datetime(2008,7,3,21,0)

#Numd = 62530  #Numero de datos que debería tener el arreglo
#print(np.size(Dat))
#Haber = []
#for k in range(0,Numd):
#	Haber.append(start + timedelta(hours= k))    #Una lista de datetimes con las fechas completas sin huecos

#Magic trick ----------------------------------------------------------------------------------------------------
# Muestra que fechas faltan
date_set = set(Dat)
one_hour = timedelta(hours=1)
test = Dat[0]
missing = []

while test < Dat[-1]:
	if test not in date_set:
		missing.append(test)
		print(test)
	test += one_hour

# -----------------------------------------------------------------------------------------------------------------

# EXPORTAR LOS ARCHIVOS EN UN ARCHIVO ASCII --------------------------------------------------------------------

archivo = "/home/juan/Ayapel/Datos/IDEAM/Fechas_ARBOLETES_Velocidad_viento.txt" 
 
f = open(archivo,'w')


#for j in range(ntim):
#	f.write("%8.4f\n" % (Dates[j]))
#f.close()



