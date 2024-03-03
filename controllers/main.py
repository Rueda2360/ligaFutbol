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
    def eliminarEmpates(self, **kwargs):
        #Recibimos los partidos empatados
        empates = request.env['liga.partido'].search([('goles_casa', '=', 'goles_fuera')])
        #Calculamos la longitud del array
        nEmpates=len(empates)
        #unlink():Borra de la base de datos un registro.
        empates.unlink()

        #Ya están los datos borrados, pero debemos actualizar los puntos de los partidos
        equipos = request.env['liga.equipo'].search([])
        for equipo in equipos:
            equipo.actualizoRegistrosEquipo()

        #Devolvemos la cantidad de partidos eliminados
        return "Empates eliminados " + str(nEmpates)

