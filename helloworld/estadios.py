# -*- coding: utf-8 -*-
from odoo import models,fields

class estadios(models.Model):
    _name = 'helloworld.estadios'

    estadio_id = fields.Many2one('helloworld.estadios',string='ID')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'estadio_id,name'
