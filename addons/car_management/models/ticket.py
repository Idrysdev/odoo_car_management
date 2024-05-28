# -*- coding: utf-8 -*-
from odoo import models, fields

class Ticket(models.Model):
    _name = 'car.ticket'
    _description = 'Ticket'

    customer_id = fields.Many2one('res.partner', string='Client', required=True)
    date = fields.Datetime(string='Date', required=True)
    amount = fields.Float(string='Montant', required=True)
    destination = fields.Char(string='Destination', required=True)
    car_id = fields.Many2one('car.car', string='Voiture', required=True)
    departure_time = fields.Datetime(string='Heure de départ', required=True)