from odoo import fields, models, api, _

class EagleeduRegistration(models.Model):
    _name = 'eagleedu.registration'
    _description = 'This the Registration for student'
    _order = 'id desc'

    name = fields.Char(sting = 'Student Name', required=True)
    registration_no = fields.Char(string='registration  No', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    st_image = fields.Binary(string='Image', help="Provide the image of the Student")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    email = fields.Char(string="student Email", help="Enter E-mail id for contact purpose")
    phone = fields.Char(string="student Phone", help="Enter Phone no. for contact purpose")
    mobile = fields.Char(string="Student Mobile", help="Enter Mobile num for contact purpose")
    nationality = fields.Many2one('res.country', string='Nationality', ondelete='restrict',default=19,
                                  help="Select the Nationality")


    state = fields.Selection([('draft', 'Draft'), ('verification', 'Verify'),
                              ('approve', 'Approve'), ('reject', 'Reject'), ('done', 'Done')],
                             string='State', required=True, default='draft', track_visibility='onchange')


    @api.model
    def create(self, vals):
        """Overriding the create method and assigning the the sequence for the record"""
        if vals.get('registration_no', _('New')) == _('New'):
            vals['registration_no'] = self.env['ir.sequence'].next_by_code('eagleedu.registration') or _('New')
        res = super(EagleeduRegistration, self).create(vals)
        return res

    # @api.multi
    # def send_to_verify(self):
    #     """Button action for sending the application for the verification"""
    #     for rec in self:
    #         rec.write({
    #             'state': 'verification'
    #         })

    @api.multi
    def send_to_approve(self):
        """Button action for sending the application for the verification"""
        for rec in self:
            rec.write({
                'state': 'verification'
            })

    @api.multi
    def create_student(self):
        """Create student from the application and data and return the student"""
        for rec in self:
            values = {
                'name': rec.name,
                'registration_no': rec.registration_no,

            }
            student = self.env['eagleedu.student'].create(values)
            rec.write({
                'state': 'done'
            })
            return {
                'name': _('Student'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'eagleedu.student',
                'type': 'ir.actions.act_window',
                'res_id': student.id,
                'context': self.env.context
            }
