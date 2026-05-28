{
    'name': 'Dhinesh Estate 123',
    'version': '1.0',
    'summary': 'Estate Management Module',
    'description': """
Estate Management Module for Odoo 17
===================================

Features:
- Property Management
- Property Types
- Menu Management
- Security Groups
""",

    'author': 'Dhinesh Kumar',
    'website': 'https://github.com/dhinesh-mern',
    'category': 'Real Estate',
    'license': 'LGPL-3',

    'depends': ['base'],

    'application': True,

    'data': [

        # security
        'security/res_groups.xml',
        'security/ir.model.access.csv',

        # views
        'views/estate_property_views.xml',
        'views/property_type_views.xml',
        'views/estate_menu.xml',
    ],

    'demo': [
        'demo/demo.xml'
    ],

    'images': [
        'static/description/banner.png',
    ],
}