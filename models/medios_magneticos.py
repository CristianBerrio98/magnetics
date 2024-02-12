from odoo import models, fields

class MediosMagneticos(models.Model):
    _name = 'o.magnetics'
    _description = 'Medios Magnéticos'

    name = fields.Char(string='Nombre', required=True)