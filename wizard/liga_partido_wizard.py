# -*- coding: utf-8 -*-
from odoo import models, fields


class LigaPartidoWizard(models.TransientModel):
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
