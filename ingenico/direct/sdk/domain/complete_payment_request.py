# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput
from ingenico.direct.sdk.domain.order import Order


class CompletePaymentRequest(DataObject):

    __card_payment_method_specific_input = None
    __order = None

    @property
    def card_payment_method_specific_input(self):
        """
        Type: :class:`ingenico.direct.sdk.domain.complete_payment_card_payment_method_specific_input.CompletePaymentCardPaymentMethodSpecificInput`
        """
        return self.__card_payment_method_specific_input

    @card_payment_method_specific_input.setter
    def card_payment_method_specific_input(self, value):
        self.__card_payment_method_specific_input = value

    @property
    def order(self):
        """
        | Order object containing order related data 
        |  Please note that this object is required to be able to submit the amount.

        Type: :class:`ingenico.direct.sdk.domain.order.Order`
        """
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value

    def to_dictionary(self):
        dictionary = super(CompletePaymentRequest, self).to_dictionary()
        if self.card_payment_method_specific_input is not None:
            dictionary['cardPaymentMethodSpecificInput'] = self.card_payment_method_specific_input.to_dictionary()
        if self.order is not None:
            dictionary['order'] = self.order.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompletePaymentRequest, self).from_dictionary(dictionary)
        if 'cardPaymentMethodSpecificInput' in dictionary:
            if not isinstance(dictionary['cardPaymentMethodSpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['cardPaymentMethodSpecificInput']))
            value = CompletePaymentCardPaymentMethodSpecificInput()
            self.card_payment_method_specific_input = value.from_dictionary(dictionary['cardPaymentMethodSpecificInput'])
        if 'order' in dictionary:
            if not isinstance(dictionary['order'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['order']))
            value = Order()
            self.order = value.from_dictionary(dictionary['order'])
        return self
