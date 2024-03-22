import os
import dao.daoConnection as dao
import models.clases as clases

os.system('cls')
#conectar bd
conex = dao.Connection("localhost", "root", "", "dbregisters")
conex.connect()

#instanciar dao
daoCity = dao.DaoCity(conex)

'''
#instanciar modelo
city1=clases.City("Managua",1)
city2=clases.City("Leon",1)
city3=clases.City("Granada",1)
city4=clases.City("Masaya",1)
city5=clases.City("Estelí",1)
city6=clases.City("Jinotepe",1)

#insertar
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)

'''
#Consultar
cities = daoCity.get_all()
for city in cities:
    print(city)
