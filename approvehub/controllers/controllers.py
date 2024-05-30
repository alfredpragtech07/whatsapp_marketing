# -*- coding: utf-8 -*-
# from odoo import http


# class Approvehub(http.Controller):
#     @http.route('/approvehub/approvehub', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approvehub/approvehub/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approvehub.listing', {
#             'root': '/approvehub/approvehub',
#             'objects': http.request.env['approvehub.approvehub'].search([]),
#         })

#     @http.route('/approvehub/approvehub/objects/<model("approvehub.approvehub"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approvehub.object', {
#             'object': obj
#         })
