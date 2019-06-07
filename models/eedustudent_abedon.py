from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class EedustudentAbedon(models.Model):
    _name = 'eedustudent.abedon'
    _description = 'abedons for the admission'
    _order = 'id desc'
    # _rec_name = 'name'
    # _inherit = ['mail.thread']

    #_inherit = 'res.partner'

    eedustudent_abedon_id = fields.Char(string="Abedon No", readonly=True, required=True, copy=False, default='New')

    abedon_date = fields.Datetime('Application Date', default=lambda
        self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    eedustudent_name = fields.Char(string='Student Name', required=True, help="Enter Name of Student")
    eedustudent_name_b = fields.Char(string='Student Bangla Name')
    eedustudent_image = fields.Binary(string='Image', help="Provide the image of the Student")
    eedustudent_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    eedustudent_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    eedustudent_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    eedustudent_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="mother's Mobile No", help="mother's Mobile No")
    date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")
    eedustudent_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                                string='Gender', required=False, track_visibility='onchange',
                                help="Your Gender is ")
    st_blood_group = fields.Selection([('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('o+', 'O+'), ('o-', 'O-'),
                                    ('ab-', 'AB-'), ('ab+', 'AB+')],
                                   string='Blood Group', track_visibility='onchange',
                                   help="Your Blood Group is ")

    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                help="Select the Nationality")

    academic_year = fields.Many2one('eedustudent.academicyear', string='Academic Year',
                                       help="Choose Academic year for which the admission is choosing")

    house_no = fields.Char(string='House No.', help="Enter the House No.")
    road_no = fields.Char(string='Area/Road No.', help="Enter the Area or Road No.")
    post_office = fields.Char(string='Post Office', help="Enter the Post Office Name")
    city = fields.Char(string='City', help="Enter the City name")
    bd_division_id = fields.Many2one('eedustudent.bddivision', string= 'Division')

    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19,
                                 help="Select the Country")
    if_same_address = fields.Boolean(string="Permanent Address same as above", default=True,
                                     help="Tick the field if the Present and permanent address is same")
    per_village = fields.Char(string='Village Name', help="Enter the Village Name")
    per_po = fields.Char(string='Post Office Name', help="Enter the Post office Name ")
    per_ps = fields.Char(string='Police Station', help="Enter the Police Station Name")
    per_dist_id = fields.Many2one('eedustudent.bddistrict', string='District', help="Enter the City of District name")

    per_country_id = fields.Many2one('res.country', string='Country', ondelete='restrict', default=19,
                                     help="Select the Country")
    guardian_name = fields.Char(string="Guardian's Name", help="Proud to say my guardian is")

    religious_id = fields.Many2one('eedustudent.religious', string="Religious", help="My Religion is ")


    status = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'),
                               ('approve', 'Approve'), ('reject', 'Reject'), ('done', 'Done')],
                              string='Status', required=True, default='draft', track_visibility='onchange')
    #
    # _sql_constraints = [
    #     ('unique_student_id', 'unique(student_id)', 'Student Id must be unique'),
    # ]


    @api.model
    def create(self, vals):
    #     """Overriding the create method and assigning the the sequence for the record"""
         if vals.get('eedustudent_abedon_id', 'New') == 'New':
            vals['eedustudent_abedon_id'] = self.env['ir.sequence'].next_by_code('eedustudent.abedon') or 'New'
         result = super(EedustudentAbedon, self).create(vals)
         return result

    def approve_call(self):
        print("this is the button for approve")

    def reject_call(self):
        print("this is the button for approve")


# class EedustudentDocuments(models.Model):
#     _name = 'eedustudent.neccessay_documents'
#     _description = "Student Documents"
#     _inherit = ['mail.thread']
#
#     @api.multi
#     def send_to_verify(self):
#         """Button action for sending the application for the verification"""
#         for rec in self:
#             document_ids = self.env['eedustudent.neccessay_documents']#.search([('application_ref', '=', rec.id)])
#             if not document_ids:
#                 raise ValidationError(_('No Documents provided'))
#             rec.write({
#                 'status': 'verification'
#             })


class EedustudentBddivision(models.Model):
    _name = 'eedustudent.bddivision'
    name = fields.Char()

class EedustudentBddistrict(models.Model):
    _name = 'eedustudent.bddistrict'
    name = fields.Char()

class EedustudentReligious(models.Model):
    _name = 'eedustudent.religious'
    name = fields.Char()

class EedustudentAcademicyear(models.Model):
    _name = 'eedustudent.academicyear'
    name = fields.Char()


#         religious_id = fields.Many2one('eedustudent.religious', string="Religious", help="My Religion is ")