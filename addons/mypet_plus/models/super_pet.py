from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class SuperPet(models.Model):
    _name = 'super.pet'
    _inherit = 'my.pet'
    _description = 'Prototype inheritance'


    # add new fields
    is_super_strength = fields.Boolean('Is Super Strength',default=False)
    is_fly=fields.Boolean('Is Super Strength',default=False)
    planet = fields.Char('Planet')


    product_ids = fields.Many2many(comodel_name='product.prodcut',
                                    string='Related Product',
                                    relation='super_pet_product_rel',
                                    column1='col-pet_id',column2='col-product_id')
