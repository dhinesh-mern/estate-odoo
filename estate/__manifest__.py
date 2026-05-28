{
    'name': 'real estate',
    'version': '1.0',
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
    'demo':[
        "demo/demo.xml"
    ]
}
