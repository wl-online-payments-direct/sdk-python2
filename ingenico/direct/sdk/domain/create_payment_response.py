# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.merchant_action import MerchantAction
from ingenico.direct.sdk.domain.payment_creation_output import PaymentCreationOutput
from ingenico.direct.sdk.domain.payment_response import PaymentResponse


class CreatePaymentResponse(DataObject):
    """
    | Object that contains details on the created payment in case one has been created.
    """

    __creation_output = None
    __merchant_action = None
    __payment = None

    @property
    def creation_output(self):
        """
        | Object containing the details of the created payment.

        Type: :class:`ingenico.direct.sdk.domain.payment_creation_output.PaymentCreationOutput`
        """
        return self.__creation_output

    @creation_output.setter
    def creation_output(self, value):
        self.__creation_output = value

    @property
    def merchant_action(self):
        """
        | Object that contains the action, including the needed data, that you should perform next, like showing instructions, showing the transaction results or redirect to a third party to complete the payment

        Type: :class:`ingenico.direct.sdk.domain.merchant_action.MerchantAction`
        """
        return self.__merchant_action

    @merchant_action.setter
    def merchant_action(self, value):
        self.__merchant_action = value

    @property
    def payment(self):
        """
        | Object that holds the payment related properties

        Type: :class:`ingenico.direct.sdk.domain.payment_response.PaymentResponse`
        """
        return self.__payment

    @payment.setter
    def payment(self, value):
        self.__payment = value

    def to_dictionary(self):
        dictionary = super(CreatePaymentResponse, self).to_dictionary()
        if self.creation_output is not None:
            dictionary['creationOutput'] = self.creation_output.to_dictionary()
        if self.merchant_action is not None:
            dictionary['merchantAction'] = self.merchant_action.to_dictionary()
        if self.payment is not None:
            dictionary['payment'] = self.payment.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreatePaymentResponse, self).from_dictionary(dictionary)
        if 'creationOutput' in dictionary:
            if not isinstance(dictionary['creationOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['creationOutput']))
            value = PaymentCreationOutput()
            self.creation_output = value.from_dictionary(dictionary['creationOutput'])
        if 'merchantAction' in dictionary:
            if not isinstance(dictionary['merchantAction'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['merchantAction']))
            value = MerchantAction()
            self.merchant_action = value.from_dictionary(dictionary['merchantAction'])
        if 'payment' in dictionary:
            if not isinstance(dictionary['payment'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['payment']))
            value = PaymentResponse()
            self.payment = value.from_dictionary(dictionary['payment'])
        return self
