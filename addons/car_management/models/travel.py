from odoo import models, fields, api
from datetime import datetime

class Travel(models.Model):
    _name = 'car.travel'
    _description = 'Voyage'

    car_id = fields.Many2one('car.car', string='Voiture', required=True)
    departure_location = fields.Char(string='Lieu de départ', required=True)
    destination = fields.Char(string='Destination', required=True)
    departure_date = fields.Datetime(string='Date de départ', required=True)
    arrival_date = fields.Datetime(string='Date d\'arrivée', required=True)
    duration = fields.Float(string='Durée du voyage', compute='_compute_duration', store=True)
    seat_count = fields.Integer(string='Nombre de places', related='car_id.seat_count', store=True)

    @api.depends('departure_date', 'arrival_date')
    def _compute_duration(self):
        for travel in self:
            if travel.departure_date and travel.arrival_date:
                departure_datetime = fields.Datetime.from_string(travel.departure_date)
                arrival_datetime = fields.Datetime.from_string(travel.arrival_date)
                duration = arrival_datetime - departure_datetime
                travel.duration = duration.total_seconds() / 3600.0
            else:
                travel.duration = 0.0
