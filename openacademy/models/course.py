# -*- coding: utf-8 -*-

from odoo import models, fields

class OpenAcademyCourse(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Course'
    
    name = fields.Char(string='Course Title', required=True, indexed=True, help='Enter your course title')
    description = fields.Html(string='Description')
    banner = fields.Binary(string='Banner')
    price = fields.Float(string='Price', digits=[5,4])

