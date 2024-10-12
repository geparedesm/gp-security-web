# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class web_porfolio(models.Model):
#     _name = 'web_porfolio.web_porfolio'
#     _description = 'web_porfolio.web_porfolio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

