# -*- encoding: utf-8 -*-
import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _

class sale_order(osv.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    _columns = {
        'entrance':fields.char('Entrance', size=20, required=True, help="Numero de Entrada"),
        'currency_local':fields.selection([('MXP','MXP'),
 		('USD','USD')],'Currency_local',required=True, help="Moneda de Venta"),
        'remission':fields.char('Remision', size=20, required=True, help="Numero de Remision"),
        'purchase_order':fields.char('Purchase Order', size=20, required=True, help="Numero de Orden de Compra"),
        'consumption_order':fields.char('Consumption Order', size=20, help="Numero de Orden de Consumo"),
    }
 