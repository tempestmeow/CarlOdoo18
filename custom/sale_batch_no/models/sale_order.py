from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    batch_no = fields.Char(string="Batch No")