from odoo import models, fields

class RejectWizard(models.TransientModel):
    _name = 'reject.wizard'
    _description = 'Reject Confirmation Wizard'

    reason = fields.Text(string='Rejection Reason', required=True)
   

    def submit_action(self):
        context = dict(self._context)
        context['reason'] = self.reason
        template = self.env.ref('approvehub.reject_email_template')
        active_id=self._context.get('active_id')
        sale_record = self.env['sale.order'].browse(active_id)

        print(active_id)
        for record in self:
            sale_record.write({'reason':self.reason})
            template.with_context(context).send_mail(active_id, force_send=True)
            return True
