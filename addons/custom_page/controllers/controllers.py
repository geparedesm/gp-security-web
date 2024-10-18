# -*- coding: utf-8 -*-
from odoo import http


class CustomPage(http.Controller):
    @http.route('/gp-developer', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('custom_page.webpage')




