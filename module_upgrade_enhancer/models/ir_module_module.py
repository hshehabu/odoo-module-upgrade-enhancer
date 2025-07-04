#-*- coding: utf-8 -*-

from odoo import models

class IrModuleModule(models.Model):
    _inherit = 'ir.module.module'

    def _button_immediate_function(self, function):
        super()._button_immediate_function(function)
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }