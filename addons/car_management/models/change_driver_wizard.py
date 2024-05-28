# wizard/change_driver_wizard.py
from odoo import models, fields, api

class ChangeDriverWizard(models.TransientModel):
    _name = 'change.driver.wizard'
    _description = 'Change Driver Wizard'

    car_id = fields.Many2one('car.car', string='Car', required=True)
    new_driver_id = fields.Many2one('hr.employee', string='New Driver', required=True)

    def change_driver(self):
        self.ensure_one()
        self.car_id.driver_id = self.new_driver_id
