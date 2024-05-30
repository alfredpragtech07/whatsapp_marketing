from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ApproveHubForm(models.Model):
    _name = 'approvehub.form'
    _description = 'Approval Form'

    name = fields.Char(string='Reference', required=True)
    model_list = fields.Many2one('ir.model', string='Model Name')
    partner_id=fields.Many2one('res.partner',string='user')
    email=fields.Char(related='partner_id.email',string='email')
    user_ids = fields.One2many('approvehub.form.user.line', 'approvehub_form_id', string='Approvers')
    approval_status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Approval Status', default='draft')

    @api.constrains('user_ids')
    def _check_unique_users(self):
        for record in self:
            selected_users = record.user_ids.mapped('user_id')
            if len(selected_users) != len(set(selected_users)):
                raise ValidationError("Each user can only be selected once.")

class ApproveHubFormUserLine(models.Model):
    _name = 'approvehub.form.user.line'
    _description = 'Approval Form User Line'

    user_id = fields.Many2one('res.users', string='User')
    status = fields.Selection([
        ('mandatory', 'Mandatory'),
        ('not_mandatory', 'Not Mandatory'),
    ], string='Status', default='mandatory')

    approvehub_form_id = fields.Many2one('approvehub.form', string='Approval Form')
