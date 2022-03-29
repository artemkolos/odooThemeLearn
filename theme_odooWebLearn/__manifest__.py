{
    'name': 'Tutorial theme',
    'description': 'Tutorial theme from odoo learn',
    'category': 'Theme',
    'sequence': 999,
    'version': '1.0',
    'depends': ['website'],
    'data': [ 'views/layout.xml', 'views/pages.xml', 'views/snippets.xml','views/options.xml'],
    'assets': {
        'web.assets_frontend': [
            "/theme_odooWebLearn/static/scss/style.scss", ],
        'web._assets_primary_variables': [
            '/theme_odooWebLearn/static/scss/primary_variables.scss', ],
        'web._assets_frontend_helpers': [
            '/theme_odooWebLearn/static/scss/bootstrap_overridden.scss',
        ],
        'website.assets_editor': [
            '/theme_odooWebLearn/static/js/tutorial_editor.js',
        ],
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}