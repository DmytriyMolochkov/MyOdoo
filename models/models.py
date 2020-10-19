# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FeedbackForm(models.Model):
    _name = 'feedbackform'
    _userName = "Name"
    _userMail = "Mail"
    _text = "Text"

    name = fields.Char(string="Тема", required=True)
    userName = fields.Char(string="Ваше имя", required=True)
    userMail = fields.Char(string="Ваша почта", required=True)
    text = fields.Text(string="Текст сообщения", required=True)
