# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import fields, models, api, _

class EagleeduClassDivision(models.Model):
    _name = 'eagleedu.class_division'
    _description = "Class room"

    name = fields.Char(string='Name')
    display=fields.Char('Class Name')
    actual_strength = fields.Integer(string='Max student No', help="Total strength of the class")
    instructor_id = fields.Many2one('eagleedu.instructor', string='Class Teacher', help="Class teacher/Faculty")
    academic_year_id = fields.Many2one('eagleedu.academicyear', string='Academic Year',
                                       help="Select the Academic Year", required=True)
    standard_class = fields.Many2one('eagleedu.standard_class', string='Class', required=True,
                               help="Select the Class")
    division_id = fields.Many2one('eagleedu.group_division', string='Division',help="Select the Division")
    section_id = fields.Many2one('eagleedu.class_section', string='Section', help="Select the Section")
    student_id = fields.One2many('eagleedu.student', 'standard_class', string='Students')

    @api.model
    def create(self, vals):
        """Return the name as a str of class + division"""
        # res = super(EducationClassDivision, self).create(vals)
        standard_class = self.env['eagleedu.standard_class'].browse(vals['standard_class'])
        division_id = self.env['eagleedu.group_division'].browse(vals['division_id'])
        section_id = self.env['eagleedu.class_section'].browse(vals['section_id'])
        batch = self.env['eagleedu.academicyear'].browse(vals['academic_year_id'])
        className=''
        divisionName=''
        sectionName=''
        batchName=batch.academic_year
        if standard_class.id>0:
            className=standard_class.name
        if division_id.id>0:
            divisionName=division_id.name
        if section_id.id>0:
            sectionName=section_id.name
        name = str(className + '-' + divisionName+ '-' + sectionName+ '-' + batchName)
        vals['name'] = name
        return super(EagleeduClassDivision, self).create(vals)