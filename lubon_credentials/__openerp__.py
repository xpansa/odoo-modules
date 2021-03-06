# -*- coding: utf-8 -*-
{
    'name': "lubon_credentials",

    'summary': """
        Provides a way to manage 3rd party credentials is a secure way.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Lubon bvba",
    'website': "http://www.lubon.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'base_setup'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'templates.xml',
        'wizard/lubon_credentials_update.xml',
        'wizard/lubon_credentials_reveal.xml',
        'views/assets.xml',
        'views/res_config.xml',
        'views/lubon_credentials.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'qweb': ['static/src/xml/widget.xml'],
}
