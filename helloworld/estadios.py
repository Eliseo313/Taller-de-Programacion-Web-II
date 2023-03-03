# -*- coding: utf-8 -*-
from odoo import models,fields

class estadios(models.Model):
    _name = 'helloworld.estadios'

    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'photo,name'
