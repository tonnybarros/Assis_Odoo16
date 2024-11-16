# -*- coding: utf-8 -*-
# from odoo import http


# class QualityTracking(http.Controller):
#     @http.route('/quality_tracking/quality_tracking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quality_tracking/quality_tracking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quality_tracking.listing', {
#             'root': '/quality_tracking/quality_tracking',
#             'objects': http.request.env['quality_tracking.quality_tracking'].search([]),
#         })

#     @http.route('/quality_tracking/quality_tracking/objects/<model("quality_tracking.quality_tracking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quality_tracking.object', {
#             'object': obj
#         })
