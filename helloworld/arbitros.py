# -*- coding: utf-8 -*-
from odoo import models,fields

class arbitros(models.Model):
    _name = 'helloworld.arbitros'

    arbitro_id = fields.Many2one('helloworld.arbitros',string='ID')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'arbitro_id,name'
