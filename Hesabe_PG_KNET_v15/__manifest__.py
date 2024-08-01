# -*- coding: utf-8 -*-
{
    'name': "Hesabe PG For KNET",
    'author': "Hesabe",
    'website': "https://developer.hesabe.com/docs/2.0/kits/odoo",
    'version': '15.0.0.0',
    'price': 49.99,
    'currency': 'USD',
    'sequence': -98,
    'maintainer' : 'Jamal shah',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'Payment Acquirer: Hesabe Implementation',
    'description': """Hesabe Payment Gateway For KNET""",
    'company': 'Hesabe Company for Electronic Payments & Settlements',
    'depends': ['payment'],
    'data': [
        'views/payment_hesabe_templates.xml',
        'views/payment_views.xml',
        'data/payment_acquirer_data.xml',
    ],
    'images': ['static/description/banner.png'],
    
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
