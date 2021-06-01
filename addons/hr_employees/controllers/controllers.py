# -*- coding: utf-8 -*-
# from odoo import http


# class HrEmployees(http.Controller):
#     @http.route('/hr_employees/hr_employees/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_employees/hr_employees/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_employees.listing', {
#             'root': '/hr_employees/hr_employees',
#             'objects': http.request.env['hr_employees.hr_employees'].search([]),
#         })

#     @http.route('/hr_employees/hr_employees/objects/<model("hr_employees.hr_employees"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_employees.object', {
#             'object': obj
#         })
