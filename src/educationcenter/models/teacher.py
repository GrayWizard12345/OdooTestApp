"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models


class Teacher(models.Model):
    _name = "educationcenter.teacher"
    _description = "Teacher"

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    groups = fields.One2many('educationcenter.course_group', 'teacher')