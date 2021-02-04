# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.card_without_cvv import CardWithoutCvv


class CompletePaymentCardPaymentMethodSpecificInput(DataObject):

    __card = None

    @property
    def card(self):
        """
        Type: :class:`ingenico.direct.sdk.domain.card_without_cvv.CardWithoutCvv`
        """
        return self.__card

    @card.setter
    def card(self, value):
        self.__card = value

    def to_dictionary(self):
        dictionary = super(CompletePaymentCardPaymentMethodSpecificInput, self).to_dictionary()
        if self.card is not None:
            dictionary['card'] = self.card.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CompletePaymentCardPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'card' in dictionary:
            if not isinstance(dictionary['card'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['card']))
            value = CardWithoutCvv()
            self.card = value.from_dictionary(dictionary['card'])
        return self
