from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderInherited(models.Model):    
    _inherit = 'sale.order'

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submited'),
        ('waiting', 'Waiting For Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')],
        string="Status", default='draft', copy=False, readonly=True)

    approval_user_line_ids = fields.One2many('approvehub.user.line', 'sale_order_id', string='Users Line')
    reason= fields.Text(string='sale order')
        
    
    @api.model
    def default_get(self,fields_list):
        result = super(SaleOrderInherited, self).default_get(fields_list)
        approval_id = self.env['approvehub.form'].search([('model_list.model', '=', 'sale.order')], limit=1)
        approval_line_list = []
        if approval_id:
            if approval_id.user_ids:
                for user_line in approval_id.user_ids:
                    user_line_values = {
                        'user_id': user_line.user_id.id,
                        'status': 'waiting_approval',
                    }
                    approval_user_line_id=self.env['approvehub.user.line'].create(user_line_values)
                    approval_line_list.append(approval_user_line_id.id)
                    print("approval_user_line_id==================================",approval_user_line_id)
        result['approval_user_line_ids'] = [(6,0,approval_line_list)]
        print("result===================================",result)
        return result

    def action_submit(self):
        for order in self:
            order.write({'state': 'submit'})

    def action_approve(self):
        for order in self:
            order.state = "approved"

    def action_reject(self):
        for order in self:
            order.state = "rejected"

class ApprovalUserLine(models.Model):
    _name = 'approvehub.user.line'

    user_id = fields.Many2one('res.users', string='User', required=True)
    status = fields.Selection([
        ('waiting_approval', 'Waiting for Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', required=True, default='waiting_approval')

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')