# -*- coding: utf-8 -*-
from odoo import http


# class FeedbackForm(http.Controller):
#     @http.route('/feedback_form/feedback_form/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/feedback_form/feedback_form/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('feedback_form.listing', {
#             'root': '/feedback_form/feedback_form',
#             'objects': http.request.env['feedback_form.feedback_form'].search([]),
#         })

#     @http.route('/feedback_form/feedback_form/objects/<model("feedback_form.feedback_form"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('feedback_form.object', {
#             'object': obj
#         })
