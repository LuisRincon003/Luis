from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db=client['empresa'] #Abre la db

num_emp = input('Ingrese el numero de empleado: ')
nombre = raw_input('Dame el nombre del empleado: ')
sueldo = input('Dame el sueldo: ')
puesto = raw_input('Dame el puesto: ')

_id = db['empleados'].update({'num_emp': num_emp },{'$set': {'nombre': nombre ,'sueldo': sueldo ,'puesto': puesto}})

