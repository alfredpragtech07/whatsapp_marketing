from odoo import models, fields

class ApproveHubFormRequest(models.Model):
    _name = 'approvehub.form.request'               
    _description = 'Approval Request'

    name = fields.Char(string='Reference', required=True)
    email = fields.Char(string='Email', required=True)
    model_list = fields.Many2one('ir.model', string='Model Name')
    model_form_view_id = fields.Many2one('ir.ui.view', string='Form View')
    user_id = fields.Many2one('res.users', string='Approver')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Request Status', default='pending')

    # New fields to store additional information
    customer_name = fields.Char(string='Customer Name')
    customer_email = fields.Char(string='Customer Email')
    current_admin = fields.Many2one('res.users', string='Current Admin')


    # Method to approve the request
    def approve_request(self):
        for request in self:
            request.status = 'approved'
            # You can add additional logic here, such as sending notifications

    # Method to reject the request
    def reject_request(self):
        for request in self:
            request.status = 'rejected'
            # You can add additional logic here, such as sending notifications

    # # Method to create a request
    # def create_request(self):
    #     # Add logic to create a request here, e.g., when sending the approval request from the Sale Order
    #     pass
