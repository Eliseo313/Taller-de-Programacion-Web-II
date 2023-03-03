# -*- coding: utf-8 -*-
from odoo import models,fields

class arbitros(models.Model):
    _name = 'helloworld.arbitros'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    liga_id = fields.Many2one('helloworld.ligas',string='Liga')

    _order = 'liga_id,name'
