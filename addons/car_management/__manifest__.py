# addons/car_management/__manifest__.py
{
    'name': 'Gestion des véhicules',
    'version': '1.0',
    'category': 'Logistics/Transport',
    'summary': 'Module de gestion des véhicules pour la société IT CAR By Idriss',
    'author': 'Idrys',
    'depends': ['base','hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/change_driver_wizard_views.xml',
        'views/car_views.xml',
        'views/travel_views.xml',
        'views/ticket_views.xml',


    ],
    'images': ['static/images/car.png'],
    'installable': True,
    'application': True,
}