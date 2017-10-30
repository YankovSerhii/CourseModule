# -*- coding: utf-8 -*-
from odoo import http

# class AcademyCourseModule(http.Controller):
#     @http.route('/academy_course_module/academy_course_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy_course_module/academy_course_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy_course_module.listing', {
#             'root': '/academy_course_module/academy_course_module',
#             'objects': http.request.env['academy_course_module.academy_course_module'].search([]),
#         })

#     @http.route('/academy_course_module/academy_course_module/objects/<model("academy_course_module.academy_course_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy_course_module.object', {
#             'object': obj
#         })