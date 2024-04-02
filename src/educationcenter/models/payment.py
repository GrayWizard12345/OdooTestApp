"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models, api


class Payment(models.Model):
    _name = "educationcenter.payment"
    _description = "Payment"

    student = fields.Many2one('educationcenter.student')
    course_group = fields.Many2one('educationcenter.course_group')
    is_paid = fields.Boolean(string="Payment Status", default=False)
    payment_date = fields.Date(string="Payment Date", default=fields.Date.today())
    paid_amount = fields.Float(string="Paid Amount")
    comment = fields.Text(string="Comments to Payment")

    student_name = fields.Char(string="Student Name", related="student.name")
    course_name = fields.Char(string="Course Name", related="course_group.course_name")
    group_id = fields.Char(string="Group ID", related="course_group.group_id")

    def print_recipe(self):
        print('Recipe Printed')
        # return self.env.ref('educationcenter.action_report_payment').report_action(self)

    @api.onchange('student')
    def onchange_field_student(self):
        if self.student:
            # filter products by seller
            group_ids = self.student.groups.ids
            return {'domain': {'course_group': [('id', 'in', group_ids)]}}
        else:
            # filter all products -> remove domain
            return {'domain': {'course_group': []}}