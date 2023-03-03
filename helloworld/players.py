# -*- coding: utf-8 -*-
from odoo import models,fields

class players(models.Model):
    _name = 'helloworld.players'

    team_id = fields.Many2one('helloworld.teams',string='Teams')
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')
    numero = fields.Integer(string='Numero de playera')
    posicion = fields.Selection([('del','Delantero'),('def','Defensa'),('por','Portero'),('cen','Central')],string='Numero de playera')

    _order = 'photo,team_id,name'
