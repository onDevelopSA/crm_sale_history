# -*- coding: utf-8 -*-
# from odoo import http


# class CrmSaleHistory(http.Controller):
#     @http.route('/crm_sale_history/crm_sale_history/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_sale_history/crm_sale_history/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_sale_history.listing', {
#             'root': '/crm_sale_history/crm_sale_history',
#             'objects': http.request.env['crm_sale_history.crm_sale_history'].search([]),
#         })

#     @http.route('/crm_sale_history/crm_sale_history/objects/<model("crm_sale_history.crm_sale_history"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_sale_history.object', {
#             'object': obj
#         })
