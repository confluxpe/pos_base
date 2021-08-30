# -*- coding: utf-8 -*-
{
    'name': 'POS Extra Buttons',
    'version': '13.0.1',
    'category': 'Point Of Sale',
    'author': 'Conflux',
    'sequence': 10,
    'summary': 'Modification to POS to add extra buttons',
    'description': "",
    'depends': ['point_of_sale'],
    'data': [
        'views/templates.xml',
        'views/pos_config_view.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],
    "currency": "EUR",
    "auto_install": False,
    "installable": True,
    'application': False,
    'license': 'OPL-1',
    'images': ['static/description/pos_base_image.jpg'],
}