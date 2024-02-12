{
    'name': 'Medios Magnéticos',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Gestión de Medios Magnéticos en Odoo',
    'description': """
        Descripción detallada de la aplicación.
    """,
    'author': 'Cristian Berrio',
    'depends': ['base'],
    'data': [
        'views/medios_magneticos_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
