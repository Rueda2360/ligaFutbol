# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result
    

    @http.route('/eliminarempates', type='http', auth='none')
    def eliminarEmpates(self):

        #Recibimos los partidos y los equipos
        equipos = request.env['liga.equipo'].sudo().search([])

        nEmpates=0
        #Los recorremos
        for recordEquipo in equipos:
            for recordPartido in request.env['liga.partido'].sudo().search([]):
                #Si el partido es empate, lo borramos
                if recordPartido.goles_casa==recordPartido.goles_fuera:
                    nEmpates+=1
                    #unlink():Borra de la base de datos un registro.
                    recordPartido.unlink()

        #Vuelvo a pedirlo por si acaso. No sé si es obligatorio pero por si da errores de registro al haber estado eliminando la base de datos prefiero no arriesgarme
        partidos = request.env['liga.partido'].sudo().search([])
        #Ya están los datos borrados, pero debemos actualizar los puntos de los partidos

        for partido in partidos:
            partido.actualizoRegistrosEquipo()

        #Devolvemos la cantidad de partidos eliminados
        return "Empates eliminados " + str(nEmpates)

