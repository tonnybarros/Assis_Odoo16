# -*- coding: utf-8 -*-
{
    'name': "Assistencia Técnica em Produto",

    'summary': """
        Módulo com função Marca, modelo e número de serie dos aparelhos """,

    'description': """
        This module helps to track the number of repaired products per production batch 
    """,

    'author': "Tonny Barros",
    'website': "https://www.tectonny.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Repair',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['repair'],

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
    'installable': True
}
