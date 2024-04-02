"""
Copyright (c) 2024, Muslimbek Abduganiev
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree.
"""

from odoo import fields, models


class Payment(models.Model):
    _name = "educationcenter.payment"
    _description = "Payment"

    student = fields.Many2one('educationcenter.student')
    course_group = fields.Many2one('educationcenter.course_group')
    is_paid = fields.Boolean(string="Payment Status", default=False)
    payment_date = fields.Date(string="Payment Date")
    paid_amount = fields.Float(string="Paid Amount")
    comment = fields.Text(string="Comments to Payment")