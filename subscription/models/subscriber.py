from odoo import models,fields

class Subscription(models.Model):
    _name ='subscriber.plan'
    _description ='Subscription plan'
    _auto = True

    name = fields.Char(string='Name', required=True)
    age = fields.Integer('Age', default=20)
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    price = fields.Float('Price', digits=(16, 2))
    description = fields.Text(string='Description')
    template = fields.Html('Template')
    birthdate = fields.Date('Birthdate')
    start_date = fields.Datetime(string='Start Date', default=fields.Date.today(), required=True)
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    # recurring_rule_type = fields.Selection([
    #     ('daily', 'Daily'),
    #     ('weekly', 'Weekly'),
    #     ('monthly', 'Monthly'),
    #     ('yearly', 'Yearly')
    # ], string='Recurrence', default='monthly')
    subscriber_code = fields.Char('subscriber Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    url = fields.Char('URL')
    phone = fields.Char('Phone')
    sign_in = fields.Float('Sign In')
    review = fields.Selection([(str(ele), str(ele)) for ele in range(5)], 'Review')

    type_id = fields.Many2one('subscription.plans', 'Plans', ondelete='restrict')

    subtypes_ids = fields.One2many('subscription.subtype', 'subscriber_id', 'Types', limit=2)

    premium_ids = fields.Many2many('subscription.premium', string='Premiums')

    ref = fields.Reference([('subscriber.plan', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')


    currency_id = fields.Many2one('res.currency', 'Currency')
    final_price_amount = fields.Monetary(currency_field='currency_id', string='Price Amount')
    document = fields.Binary('Document')
    file_name = fields.Char('File Name')
    photo = fields.Image('Photo')


    total_obt_prices = fields.Float(compute='_calc_total_prices', string='Total Obtained Prices')
    total_prices = fields.Float(compute='_calc_total_prices', string='Total prices')
    # NOTE : You can calculate multiple values in a single compute method as well.
    # Usually the compute method is called when you open the record or you save the record.

    state = fields.Selection([('applied', 'Applied'),
                              ('draft', 'draft'),
                              ('confirmed', 'Confirmed'),
                              ('joined', 'Joined'),
                              ('left', 'Left')], 'State', default='applied')

    sequence = fields.Integer('Sequence')

    def _calc_total_prices(self):
        """
        This method will calculate multiple fields.
        -------------------------------------------
        @param self : object pointer / recordset
        """
        for subscriber in self:
            print("NORMAL FIELD", subscriber.name)
            print("M2O FIELD", subscriber.type_id)
            print("O2M FIELD", subscriber.subtypes_ids)
            print("M2M FIELD", subscriber.premium_ids)
            print("REF FUELD", subscriber.ref)
            total = 0.0
            total_obt = 0.0
            for subtypes in subscriber.subtypes_ids:
                total += subtypes.month  # total = total + exam.total_marks
                total_obt += subtypes.year
            subscriber.total_obt_prices = total_obt
            subscriber.total_prices = total

# RESERVED FIELDS
# name - It is used as the recognized name of the record and gets displayed in the relational fields such as M2O and M2M.
# active - This defined whether the recrod is active or archived. By default only active recrods are displayed.
# state - This field is used for the process flow of your model
# sequence - This is a reserved filed which is used for priority or preference.







