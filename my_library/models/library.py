from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'  # library_book#=====>for security#

    name = fields.Char()
    date_release = fields.Date()
    notes = fields.Text()
    state = fields.Selection([('not available', 'Not Available'), ('available', 'Avaialble'), ('lost', 'Lost')])
    description = fields.Html()
    cover = fields.Binary()
    update_date = fields.Datetime()
    pages = fields.Integer()
    reader_rate = fields.Float()
    active = fields.Boolean()
