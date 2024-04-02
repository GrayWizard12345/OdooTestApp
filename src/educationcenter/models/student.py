"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models


class Student(models.Model):
    _name = "educationcenter.student"
    _description = "Student"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    groups = fields.Many2many('educationcenter.course_group')

    payments = fields.One2many('educationcenter.payment', 'student')
