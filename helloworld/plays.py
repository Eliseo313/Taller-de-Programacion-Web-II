# -*- coding: utf-8 -*-
from odoo import models,fields


class plays(models.Model):
    _name = 'helloworld.plays'

    name = fields.Char(string='Folio')
    fecha = fields.Datetime(string='Fecha')
    liga_id = fields.Many2one('helloworld.ligas',string='Liga')
    team1_id = fields.Many2one('helloworld.teams',string='Equipo Local')
    team2_id = fields.Many2one('helloworld.teams',string='Equipo Visitante')
    estadio_id = fields.Many2one('helloworld.estadios',string='Estadio')
    arbitro_ids = fields.One2many('helloworld.plays_arbitros',string='Arbitros')

    _order = 'name'
    _sql_constraints = [('plays_uniq', 'unique(name)', 'Juegoa duplicado, intenta con otro...'),]


class plays_arbitros(models.Model):
    _name = 'helloworld.plays_arbitros'

    play_id = fields.Many2One('helloworld.plays'string='Play')
    arbitro_id = fields.Many2One('helloworld.arbitros'string='Arbitro')
    posicion = fields.Selection([('central','Central'),('band','Bandera'),('otro','Otro')],string='Posicion')

    _order = 'play_id,arbitro_id'
    _sql_constraints = [('plays_uniq', 'unique(play_id,arbitro_id)', 'Arbitro duplicad, intenta con otro...'),]