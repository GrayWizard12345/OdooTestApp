"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models, api


class CourseGroup(models.Model):
    _name = "educationcenter.course_group"
    _description = "Course Group"

    group_id = fields.Char(string="Group ID")
    course = fields.Many2one('educationcenter.course')
    course_name = fields.Char(string="Course Name", related="course.name")
    students = fields.Many2many('educationcenter.student')
    teacher = fields.Many2one('educationcenter.teacher')
    teacher_name = fields.Char(string="Teacher Name", related="teacher.name")

    payments = fields.One2many('educationcenter.payment', 'course_group')