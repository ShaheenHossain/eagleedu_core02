from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import datetime

class EeduadmissionPupil(models.Model):
    _name = 'eeduadmission.pupil'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Student record'

    # _rec_name = 'st_name'

    # _inherit = ['mail.thread']

    @api.model
    def create(self, vals):
        """Over riding the create method to assign sequence for the newly creating the record"""
        vals['admission_no'] = self.env['ir.sequence'].next_by_code('eeduadmission.pupil')
        res = super(EeduadmissionPupil, self).create(vals)
        return res

    partner_id = fields.Many2one(
        'res.partner', string='Partner', required=True, ondelete="cascade")

    abedon_date = fields.Datetime('Application Date', default=lambda
        self: fields.datetime.now())  # , default=fields.Datetime.now, required=True

    st_name = fields.Char(string='Student Name', required=True, help="Enter Name of Student")
    st_name_b = fields.Char(string='Student Bangla Name')
    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    st_father_name = fields.Char(string="Father's Name", help="Proud to say my father is", required=False)
    st_father_name_b = fields.Char(string="বাবার নাম", help="Proud to say my father is")
    father_mobile = fields.Char(string="Father's Mobile No", help="Father's Mobile No")
    st_mother_name = fields.Char(string="Mother's Name", help="Proud to say my mother is", required=False)
    st_mother_name_b = fields.Char(string="মা এর নাম", help="Proud to say my mother is")
    mother_mobile = fields.Char(string="mother's Mobile No", help="mother's Mobile No")
    date_of_birth = fields.Date(string="Date Of birth", help="Enter your DOB")
    st_gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
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
    pupil_id=fields.Char('Student Id')
    roll_no = fields.Integer('Roll No')
