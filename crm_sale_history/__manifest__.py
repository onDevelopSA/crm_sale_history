# -*- coding: utf-8 -*-
# © 2021 onDevelop.sa
# Autor: Idelis Gé Ramírez
# Part of onDevelop.SA. See LICENSE file for full copyright and licensing details.

{
    'name': "crm_sale_history",
    'summary': """
    Add the Total Invoiced, Total Due, Paid Percentage of the customer in CRM
    Leads.
    """,
    'description': """""",
    'author': "onDevelop.SA",
    'website': "https://ondevelop.tech/",
    'category': 'Sales/CRM',
    'version': '13.0.1',
    'license': 'LGPL-3',
    'price': 9,
    'currency': 'USD',
    'support': "ondevelop.sa@gmail.com",
    'depends': ['base', 'sale', 'crm', 'account'],
    'images': ['static/description/crm_sale_history_cover.png'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False
}
