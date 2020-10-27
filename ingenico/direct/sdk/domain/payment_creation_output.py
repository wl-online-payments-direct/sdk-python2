# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject


class PaymentCreationOutput(DataObject):
    """
    | Object containing the details of the created payment.
    """

    __external_reference = None
    __is_new_token = None
    __token = None
    __tokenization_succeeded = None

    @property
    def external_reference(self):
        """
        | The external reference identifier for this transaction. Data in this property will also be returned in our report files, allowing you to reconcile them

        Type: str
        """
        return self.__external_reference

    @external_reference.setter
    def external_reference(self, value):
        self.__external_reference = value

    @property
    def is_new_token(self):
        """
        | Indicates if a new token was created 
        |  * true - A new token was created 
        |  * false - A token with the same card number already exists and is returned. Please note that the existing token has not been updated. When you want to update other data then the card number, you need to update data stored in the token explicitly, as data is never updated during the creation of a token.

        Type: bool
        """
        return self.__is_new_token

    @is_new_token.setter
    def is_new_token(self, value):
        self.__is_new_token = value

    @property
    def token(self):
        """
        | ID of the token. This property is populated when the payment was done with a token or when the payment was tokenized.

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenization_succeeded(self):
        """
        | Indicates if tokenization was successful or not. If this value is false, then the token and isNewToken properties will not be set.

        Type: bool
        """
        return self.__tokenization_succeeded

    @tokenization_succeeded.setter
    def tokenization_succeeded(self, value):
        self.__tokenization_succeeded = value

    def to_dictionary(self):
        dictionary = super(PaymentCreationOutput, self).to_dictionary()
        if self.external_reference is not None:
            dictionary['externalReference'] = self.external_reference
        if self.is_new_token is not None:
            dictionary['isNewToken'] = self.is_new_token
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenization_succeeded is not None:
            dictionary['tokenizationSucceeded'] = self.tokenization_succeeded
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentCreationOutput, self).from_dictionary(dictionary)
        if 'externalReference' in dictionary:
            self.external_reference = dictionary['externalReference']
        if 'isNewToken' in dictionary:
            self.is_new_token = dictionary['isNewToken']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenizationSucceeded' in dictionary:
            self.tokenization_succeeded = dictionary['tokenizationSucceeded']
        return self
