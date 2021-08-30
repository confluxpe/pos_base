# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PosOrder(models.Model):
	_inherit = 'pos.order'

	#cancel = fields.Boolean(string='Anulado', default=False)
