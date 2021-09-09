# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.hosted_checkout_specific_output import HostedCheckoutSpecificOutput
from ingenico.direct.sdk.domain.operation_output import OperationOutput
from ingenico.direct.sdk.domain.payment_output import PaymentOutput
from ingenico.direct.sdk.domain.payment_status_output import PaymentStatusOutput


class PaymentDetailsResponse(DataObject):
    """
    | Object that holds the payment details properties
    """

    __operations = None
    __hosted_checkout_specific_output = None
    __id = None
    __payment_output = None
    __status = None
    __status_output = None

    @property
    def operations(self):
        """
        | Object that contains the complete list of operations executed on the payment.

        Type: list[:class:`ingenico.direct.sdk.domain.operation_output.OperationOutput`]
        """
        return self.__operations

    @operations.setter
    def operations(self, value):
        self.__operations = value

    @property
    def hosted_checkout_specific_output(self):
        """
        | Hosted Checkout specific information. Populated if the payment was created on the platform through a Hosted Checkout.

        Type: :class:`ingenico.direct.sdk.domain.hosted_checkout_specific_output.HostedCheckoutSpecificOutput`
        """
        return self.__hosted_checkout_specific_output

    @hosted_checkout_specific_output.setter
    def hosted_checkout_specific_output(self, value):
        self.__hosted_checkout_specific_output = value

    @property
    def id(self):
        """
        | Our unique payment transaction identifier

        Type: str
        """
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def payment_output(self):
        """
        | Object containing payment details

        Type: :class:`ingenico.direct.sdk.domain.payment_output.PaymentOutput`
        """
        return self.__payment_output

    @payment_output.setter
    def payment_output(self, value):
        self.__payment_output = value

    @property
    def status(self):
        """
        | Current high-level status of the payment in a human-readable form.

        Type: str
        """
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def status_output(self):
        """
        | This object has the numeric representation of the current payment status, timestamp of last status change and performable action on the current payment resource. In case of failed payments and negative scenarios, detailed error information is listed.

        Type: :class:`ingenico.direct.sdk.domain.payment_status_output.PaymentStatusOutput`
        """
        return self.__status_output

    @status_output.setter
    def status_output(self, value):
        self.__status_output = value

    def to_dictionary(self):
        dictionary = super(PaymentDetailsResponse, self).to_dictionary()
        if self.operations is not None:
            dictionary['Operations'] = []
            for element in self.operations:
                if element is not None:
                    dictionary['Operations'].append(element.to_dictionary())
        if self.hosted_checkout_specific_output is not None:
            dictionary['hostedCheckoutSpecificOutput'] = self.hosted_checkout_specific_output.to_dictionary()
        if self.id is not None:
            dictionary['id'] = self.id
        if self.payment_output is not None:
            dictionary['paymentOutput'] = self.payment_output.to_dictionary()
        if self.status is not None:
            dictionary['status'] = self.status
        if self.status_output is not None:
            dictionary['statusOutput'] = self.status_output.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentDetailsResponse, self).from_dictionary(dictionary)
        if 'Operations' in dictionary:
            if not isinstance(dictionary['Operations'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['Operations']))
            self.operations = []
            for element in dictionary['Operations']:
                value = OperationOutput()
                self.operations.append(value.from_dictionary(element))
        if 'hostedCheckoutSpecificOutput' in dictionary:
            if not isinstance(dictionary['hostedCheckoutSpecificOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['hostedCheckoutSpecificOutput']))
            value = HostedCheckoutSpecificOutput()
            self.hosted_checkout_specific_output = value.from_dictionary(dictionary['hostedCheckoutSpecificOutput'])
        if 'id' in dictionary:
            self.id = dictionary['id']
        if 'paymentOutput' in dictionary:
            if not isinstance(dictionary['paymentOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentOutput']))
            value = PaymentOutput()
            self.payment_output = value.from_dictionary(dictionary['paymentOutput'])
        if 'status' in dictionary:
            self.status = dictionary['status']
        if 'statusOutput' in dictionary:
            if not isinstance(dictionary['statusOutput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['statusOutput']))
            value = PaymentStatusOutput()
            self.status_output = value.from_dictionary(dictionary['statusOutput'])
        return self
