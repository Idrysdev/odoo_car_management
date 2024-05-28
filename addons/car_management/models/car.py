from odoo import models, fields , api

class Car(models.Model):
    _name = 'car.car'
    _inherit = 'mail.thread'
    _description = 'Voiture'

    name = fields.Char(string='Nom', required=True)
    model = fields.Char(string='Modèle', required=True)
    manufacturer = fields.Char(string='Fabricant', required=True)
    seat_count = fields.Integer(string='Nombre de places', required=True)
    fuel_type = fields.Selection([
        ('petrol', 'Essence'),
        ('diesel', 'Diesel'),
        ('electric', 'Électrique'),
        ('hybrid', 'Hybride')],
        string='Type de carburant', required=True)
    driver_id = fields.Many2one('hr.employee', string='Chauffeur')
    operation_tracking_ids = fields.One2many('operation.tracking', 'vehicle_id', string="Opérations")

    def open_driver_details(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Driver',
            'res_model': 'hr.employee',
            'view_mode': 'form',
            'res_id': self.driver_id.id,
            'target': 'new',
        }

    def open_change_driver_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Change Driver',
            'res_model': 'change.driver.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_car_id': self.id},
        }

    @api.model
    def create(self, vals):
        record = super(Car, self).create(vals)
        self.env['operation.tracking'].create({
            'vehicle_id': record.id,
            'user_id': self.env.uid,
            'operation_type': 'create',
        })
        return record

    def write(self, vals):
        result = super(Car, self).write(vals)
        for record in self:
            self.env['operation.tracking'].create({
                'vehicle_id': record.id,
                'user_id': self.env.uid,
                'operation_type': 'update',
            })
        return result

    def unlink(self):
        for record in self:
            self.env['operation.tracking'].create({
                'vehicle_id': record.id,
                'user_id': self.env.uid,
                'operation_type': 'delete',
            })
        return super(Car, self).unlink()