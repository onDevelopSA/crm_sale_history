# © 2021 onDevelop.sa
# Autor: Idelis Gé Ramírez

from odoo import fields, models, api, _

class CrmLead(models.Model):
    _inherit = "crm.lead"
    _description = "Redefined for add the fields needed in the kanban view. "

    pay_percentage = fields.Integer(compute='_compute_pay_percentage')
    invoice_due = fields.Float()
    total_invoiced = fields.Float()
    priority = fields.Selection([('0', 'Low'),
                                 ('1', 'Medium'),
                                 ('2', 'High'),
                                 ('3', 'Very High'),
                                 ('4', 'immediately')])
      
    @api.depends('partner_id')
    def _compute_pay_percentage(self):
        '''Compute the fields total invoiced,  invoice due, pay percentage
        used in the kanban view to show the information of the selected
        partner.

        '''
        for lead in self:
            lead.pay_percentage = 0
            if lead.partner_id:
                moves = self.env['account.move'].search(
                    [('partner_id','=', lead.partner_id.id),
                     ('state','=','posted'),
                     ('type','in',('out_invoice', 'out_refund'))])
                if any(moves):
                    # Use 'or 1' to avoid zero division bug.
                    invoiced = sum(moves.mapped('amount_total_signed')) or 1
                    residual = sum(moves.mapped('amount_residual'))
                    total_pay = invoiced - residual
                    lead.total_invoiced = invoiced
                    lead.invoice_due = residual
                    if invoiced:
                        lead.pay_percentage = (total_pay * 100) / invoiced
                        lead.priority = '0'
                        if lead.pay_percentage >= 80:
                            lead.priority = '4'
                        elif lead.pay_percentage >= 60:
                            lead.priority = '3'
                        elif lead.pay_percentage >= 40:
                            lead.priority = '2'
                        elif lead.pay_percentage >= 20:
                            lead.priority = '1'
