# -*- coding: utf-8 -*-
# from odoo import http


# class WebPorfolio(http.Controller):
#     @http.route('/web_porfolio/web_porfolio', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_porfolio/web_porfolio/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_porfolio.listing', {
#             'root': '/web_porfolio/web_porfolio',
#             'objects': http.request.env['web_porfolio.web_porfolio'].search([]),
#         })

#     @http.route('/web_porfolio/web_porfolio/objects/<model("web_porfolio.web_porfolio"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_porfolio.object', {
#             'object': obj
#         })

