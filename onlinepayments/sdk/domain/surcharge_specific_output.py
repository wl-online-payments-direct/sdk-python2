# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.amount_of_money import AmountOfMoney
from onlinepayments.sdk.domain.surcharge_rate import SurchargeRate


class SurchargeSpecificOutput(DataObject):
    """
    | Object containing specific surcharging attributes applied to an order.
    """

    __mode = None
    __surcharge_amount = None
    __surcharge_rate = None

    @property
    def mode(self):
        """
        | The surcharge mode which defines how a merchant will apply surcharging.
        | * pass-through - Merchant to define and apply surcharge amount for a transaction for processing. This mode is not supported on Create Hosted Checkout Session.
        | * on-behalf-of - Merchant to instruct the payment platform to calculate and apply a surcharge amount to a transaction, based on the merchant’s surcharge configuration, net amount, and payment product type.

        Type: str
        """
        return self.__mode

    @mode.setter
    def mode(self, value):
        self.__mode = value

    @property
    def surcharge_amount(self):
        """
        | Object containing amount and ISO currency code attributes

        Type: :class:`onlinepayments.sdk.domain.amount_of_money.AmountOfMoney`
        """
        return self.__surcharge_amount

    @surcharge_amount.setter
    def surcharge_amount(self, value):
        self.__surcharge_amount = value

    @property
    def surcharge_rate(self):
        """
        | A summary of surcharge details used in the calculation of the surcharge amount. null if result = NO_SURCHARGE

        Type: :class:`onlinepayments.sdk.domain.surcharge_rate.SurchargeRate`
        """
        return self.__surcharge_rate

    @surcharge_rate.setter
    def surcharge_rate(self, value):
        self.__surcharge_rate = value

    def to_dictionary(self):
        dictionary = super(SurchargeSpecificOutput, self).to_dictionary()
        if self.mode is not None:
            dictionary['mode'] = self.mode
        if self.surcharge_amount is not None:
            dictionary['surchargeAmount'] = self.surcharge_amount.to_dictionary()
        if self.surcharge_rate is not None:
            dictionary['surchargeRate'] = self.surcharge_rate.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(SurchargeSpecificOutput, self).from_dictionary(dictionary)
        if 'mode' in dictionary:
            self.mode = dictionary['mode']
        if 'surchargeAmount' in dictionary:
            if not isinstance(dictionary['surchargeAmount'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeAmount']))
            value = AmountOfMoney()
            self.surcharge_amount = value.from_dictionary(dictionary['surchargeAmount'])
        if 'surchargeRate' in dictionary:
            if not isinstance(dictionary['surchargeRate'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['surchargeRate']))
            value = SurchargeRate()
            self.surcharge_rate = value.from_dictionary(dictionary['surchargeRate'])
        return self
