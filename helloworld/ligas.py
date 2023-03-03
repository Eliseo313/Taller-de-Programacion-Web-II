# -*- coding: utf-8 -*-
from odoo import models,fields

class ligas(models.Model):
    _name = 'helloworld.ligas'
    
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    
    _order = 'photo,name'
