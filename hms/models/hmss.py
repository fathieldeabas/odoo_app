from odoo import models, fields, api
class patient(models.Model):
    _name = 'patient.details' #patient_details
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    address = fields.Text()
    blood_type = fields.Selection([('o', 'o'), ('x', 'x'), ('y', 'y')])
    history = fields.Html()
    image = fields.Binary()
    aga = fields.Integer()
    cr_ratio = fields.Float()
    pcr = fields.Boolean()
    name_book = fields.Many2one('hms.department', index=True)

class department(models.Model):
    _name = 'hms.department' #hms_department

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean(default=True)
    patients_id = fields.One2many('patient.details','name_book', index=True)
    patient_birth_date = fields.Date(related='patients_id.birth_date', readonly=False, store=True)


# class patient(models.Model):
#     _name = 'patient.details' #patient_details
#     _rec_name = 'patient_name'
#
#     patient_name = fields.Char()
#     date_birth = fields.Date()

class doctor(models.Model):
    _name = 'hms.doctor'  # hms_doctor#=====>for security#

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Binary()