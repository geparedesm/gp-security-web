# -*- coding: utf-8 -*-
{
    'name': "custom_page",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'custom_page/static/src/css/open-iconic-bootstrap.min.css',
            'custom_page/static/src/css/animate.css',
            'custom_page/static/src/css/owl.carousel.min.css',
            'custom_page/static/src/css/owl.theme.default.min.css',
            'custom_page/static/src/css/magnific-popup.css',
            'custom_page/static/src/css/ionicons.min.css',
            'custom_page/static/src/css/flaticon.css',
            'custom_page/static/src/css/icomoon.css',
            'custom_page/static/src/css/style.css',
        ],
    },
}
