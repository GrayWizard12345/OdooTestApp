# noinspection PyStatementEffect


{
    'name': "Education Center Management",
    'version': '1.0',
    'depends': [],
    'author': "Muslimbek Abduganiev",
    'category': 'Administration',
    'license': 'LGPL-3',
    'description': """
    This is a test odoo app for Education Center.
    """,
    # data files always loaded at installation
    'data': [
        'data/groups.xml',
        'data/users.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/course.xml',
        'views/teacher.xml',
        'views/student.xml',
        'views/group.xml',
        'views/payment.xml',

    ],
    # data files containing optionally loaded demonstration data
    'installable': True,
    'auto_install': False,
    'application': True,
    'css': [],
}
