# -*- coding: utf-8 -*-
{
    'name': "Hr Employees",
    'version': '1.1',
    'category': 'Human Resources/Employees',

    'summary': """Centralize employee information""",

    'description': """""",

    # 'author': "My Company",
    'website': "https://www.odoo.com/page/employees",
    'images': [
        'images/hr_department.jpeg',
        'images/hr_employee.jpeg',
        'images/hr_job_position.jpeg',
        'static/src/img/default_image.png',
    ],
    # any module necessary for this one to work correctly
    'depends': ['base_setup',
                'mail',
                'resource',
                'web', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_profile_views.xml',
        'views/hr_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/hr_demo.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
        'static/src/bugfix/bugfix.xml',
        'static/src/xml/hr_templates.xml',
    ],
}
