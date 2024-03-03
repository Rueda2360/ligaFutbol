# -*- coding: utf-8 -*-
from odoo import models, fields

#Esta clase observamos que hereda de "models.TransientModel" una clase especial
#que crea un modelo, pero es temporal y no hacer permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class LigaEquipoWizard(models.TransientModel):
    _name = 'liga.partido.wizard'

    equipo_casa = fields.Many2one('liga.equipo', string='Equipo local', required=True)
    goles_casa = fields.Integer(string='Goles equipo local', required=True)

    equipo_fuera = fields.Many2one('liga.equipo', string='Equipo visitante', required=True)
    goles_fuera = fields.Integer(string='Goles equipo visitante', required=True)

    def add_liga_partido(self):
        # Lógica para crear el partido utilizando los datos del Wizard
        partidos = self.env['liga.partido']
        partidoTemp = {
            'equipo_casa': self.equipo_casa.id,
            'goles_casa': self.goles_casa,
            'equipo_fuera': self.equipo_fuera.id,
            'goles_fuera': self.goles_fuera,
        }
        partidos.create(partidoTemp)
