from odoo import fields,models,api


class AddSubscription(models.Model):
    _name ='subscription.addsubscription'
    _description = 'Add Subscription'

    type_id = fields.Many2one('subscription.type', 'Subscription', required=True)
    plan_id = fields.Many2one('subscription.plan', 'Plan', required=True)
    price_depend = fields.Float(compute='_compute_price_depend', string='Price')
    user_id = fields.Many2one('subscription.user', 'User', ondelete='cascade')



    @api.depends('type_id', 'plan_id')
    def _compute_price_depend(self):
        for user in self:
            if user.type_id and user.plan_id:
                plan_code = user.plan_id.code.lower()
                if plan_code == 'monthly':
                    user.price_depend = user.type_id.monthly_price
                elif plan_code == 'daily':
                    user.price_depend = user.type_id.daily_price
                elif plan_code == 'weekly':
                    user.price_depend = user.type_id.weekly_price
                elif plan_code == 'yearly':
                    user.price_depend = user.type_id.yearly_price
                else:
                    user.total_price = total
                    user.price_depend = 0.0
            else:
                user.price_depend = 0.0
