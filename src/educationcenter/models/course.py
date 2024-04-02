"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models


class Course(models.Model):
    _name = "educationcenter.course"
    _description = "Course"

    name = fields.Char(string="Course Name")
    price = fields.Float(string="Price")
    groups = fields.One2many('educationcenter.course_group', 'course')
