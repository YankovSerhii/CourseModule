# -*- coding: utf-8 -*-
{
    'name': "AcademyCourseModule",

    'summary': """Training""",

    'description': """
        Open Academy module for training:
            - trining courss
            - Sessions
            - etc...
    """,

    'author': "Serhii Yankov",
    'website': "http://github.com/YankovSerhii",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
