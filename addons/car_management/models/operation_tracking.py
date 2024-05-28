from odoo import models, fields, api

class OperationTracking(models.Model):
    _name = 'operation.tracking'
    _description = 'Suivi des Opérations'

    vehicle_id = fields.Many2one('car.car', string="Véhicule", required=True)
    user_id = fields.Many2one('res.users', string="Utilisateur", required=True)
    operation_type = fields.Selection([
        ('create', 'Création'),
        ('update', 'Mise à jour'),
        ('delete', 'Suppression')
    ], string="Type d'opération", required=True)
    operation_date = fields.Datetime(string="Date d'opération", default=fields.Datetime.now, required=True)
