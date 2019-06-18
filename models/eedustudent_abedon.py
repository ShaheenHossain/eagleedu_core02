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

    st_abedon_id = fields.Char(string="Abedon No", readonly=True, required=True, copy=False, default='New')

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
    student_id=fields.Char('Student Id')
    roll_no = fields.Integer('Roll No')
    section=fields.Char('Section')
    status = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'),
                               ('approve', 'Approve'), ('reject', 'Reject'), ('done', 'Done')],
                              string='Status', required=True, default='draft', track_visibility='onchange')

    # _sql_constraints = [
    #     ('unique_student_id', 'unique(student_id)', 'Student Id must be unique'),
    # ]


    @api.model
    def create(self, vals):
    #     """Overriding the create method and assigning the the sequence for the record"""
         if vals.get('st_abedon_id', 'New') == 'New':
            vals['st_abedon_id'] = self.env['ir.sequence'].next_by_code('eedustudent.abedon') or 'New'
         result = super(EedustudentAbedon, self).create(vals)
         return result


    @api.multi
    def approve_call(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'status': 'verification'
            })

    @api.multi
    def for_verify(self):
        """Return the state to done if the documents are perfect"""
        for rec in self:
            rec.write({
                'status': 'approve'
            })


    @api.multi
    def create_student(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'st_name': rec.st_name,
                'st_name_b': rec.st_name_b,
                'st_abedon_id': rec.id,
                'st_father_name': rec.st_father_name,
                'st_father_name_b': rec.st_father_name_b,
                'father_mobile': rec.father_mobile,
                'st_mother_name': rec.st_mother_name,
                'st_mother_name_b': rec.st_mother_name_b,
                'mother_mobile': rec.mother_mobile,
                'st_gender': rec.st_gender,
                'date_of_birth': rec.date_of_birth,
                'st_blood_group': rec.st_blood_group,
                'nationality': rec.nationality,
                'academic_year': rec.academic_year,
                'house_no': rec.house_no,
                'road_no': rec.road_no,
                'post_office': rec.post_office,
                'city': rec.city,
                'bd_division_id': rec.bd_division_id,
                'country_id': rec.country_id,
                'per_village': rec.per_village,
                'per_po': rec.per_po,
                'per_ps': rec.per_ps,
                'per_dist_id': rec.per_dist_id,
                'per_country_id': rec.per_country_id,
                'guardian_name': rec.guardian_name,
                'religious_id': rec.religious_id,
                'is_student': True,
                'student_id': rec.student_id,
                'roll_no': rec.roll_no,
                'st_abedon_id': rec.st_abedon_id,
            }
            member = self.env['eedustudent.member'].create(values)
            rec.write({
                'status': 'done'
            })
            return {
                'name': _('Member'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'eedustudent.member',
                'type': 'ir.actions.act_window',
                'res_id': member.id,
                'context': self.env.context
            }



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

class EedustudentOrganization(models.Model):
    _inherit = 'res.company'

class EedustudentResPartner(models.Model):
    _inherit = 'res.partner'
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict',default=19)
    is_pupil = fields.Boolean(string="Is a Member")
#    is_parent = fields.Boolean(string="Is a Parent")
