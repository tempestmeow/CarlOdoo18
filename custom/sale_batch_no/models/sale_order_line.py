from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    batch_no = fields.Char(string='Batch Number')
