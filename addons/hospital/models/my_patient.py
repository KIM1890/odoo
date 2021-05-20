from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class PatientHospital(models.Model):
    _name = 'my.patient'
    _description = 'Managing patient information'

    name = fields.Char('Patient', required=True)
    nickname = fields.Char('Nickname')
    age = fields.Integer('Patient age', default=1)
    weight = fields.Float('Weight(kg)')
    dob = fields.Date('DOB', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='male')
    patient_image = fields.Binary(
        'Patient Image', attachment=True, help='Patient Image')
