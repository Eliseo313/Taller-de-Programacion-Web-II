# -*- coding: utf-8 -*-
from odoo import models,fields


class coachs(models.Model):
    _name = 'helloworld.coachs'
    name = fields.Char(string='Nombre')
    photo = fields.Binary(string='Foto')

    _order = 'name'


class teams(models.Model):
    _name = 'helloworld.teams'

    name = fields.Char(string='Nombre')
    coach_id = fields.Many2one('helloworld.coachs',string='Coach')
    liga_id = fields.Many2one('helloworld.ligas',string='Liga')
    photo = fields.Binary(string='Foto')
    players_ids = fields.One2many('helloworld.players','team_id',string='Team')

    _order = 'photo,name,liga_id'
