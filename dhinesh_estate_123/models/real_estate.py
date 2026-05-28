from odoo import models,fields

class RealEstate(models.Model):
    _name = "real_estate"
    _description = "test model"

    name = fields.Char(default="Home",required = True)
    price = fields.Float()
    