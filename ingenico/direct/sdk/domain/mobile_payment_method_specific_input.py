# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/index.html/
#
from ingenico.direct.sdk.data_object import DataObject
from ingenico.direct.sdk.domain.decrypted_payment_data import DecryptedPaymentData


class MobilePaymentMethodSpecificInput(DataObject):
    """
    | Object containing the specific input details for mobile payments
    """

    __authorization_mode = None
    __decrypted_payment_data = None
    __encrypted_payment_data = None
    __ephemeral_key = None
    __payment_product_id = None
    __public_key_hash = None
    __requires_approval = None

    @property
    def authorization_mode(self):
        """
        | Determines the type of the authorization that will be used. Allowed values: 
        |   * FINAL_AUTHORIZATION - The payment creation results in an authorization that is ready for capture. Final authorizations can't be reversed and need to be captured for the full amount within 7 days. 
        |   * PRE_AUTHORIZATION - The payment creation results in a pre-authorization that is ready for capture. Pre-authortizations can be reversed and can be captured within 30 days. The capture amount can be lower than the authorized amount. 
        |   * SALE - The payment creation results in an authorization that is already captured at the moment of approval. 
        
        |   Only used with some acquirers, ignored for acquirers that don't support this. In case the acquirer doesn't allow this to be specified the authorizationMode is 'unspecified', which behaves similar to a final authorization.

        Type: str
        """
        return self.__authorization_mode

    @authorization_mode.setter
    def authorization_mode(self, value):
        self.__authorization_mode = value

    @property
    def decrypted_payment_data(self):
        """
        | The payment data if you do the decryption of the encrypted payment data yourself.

        Type: :class:`ingenico.direct.sdk.domain.decrypted_payment_data.DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value):
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self):
        """
        | The payment data if we will do the decryption of the encrypted payment data. Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the encrypted payment data instead.
        | * For Apple Pay, the encrypted payment data can be found in property data of the PKPayment.token.paymentData property.

        Type: str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value):
        self.__encrypted_payment_data = value

    @property
    def ephemeral_key(self):
        """
        | Ephemeral Key
        | A unique generated key used by Apple to encrypt data.

        Type: str
        """
        return self.__ephemeral_key

    @ephemeral_key.setter
    def ephemeral_key(self, value):
        self.__ephemeral_key = value

    @property
    def payment_product_id(self):
        """
        | Payment product identifier - Please see [payment products](https://support.direct.ingenico.com/documentation/api/reference/index.html#tag/Products) for a full overview of possible values.

        Type: int
        """
        return self.__payment_product_id

    @payment_product_id.setter
    def payment_product_id(self, value):
        self.__payment_product_id = value

    @property
    def public_key_hash(self):
        """
        | Public Key Hash
        | A unique identifier to retrieve key used by Apple to encrypt information.

        Type: str
        """
        return self.__public_key_hash

    @public_key_hash.setter
    def public_key_hash(self, value):
        self.__public_key_hash = value

    @property
    def requires_approval(self):
        """
        | * true = the payment requires approval before the funds will be captured using the Approve payment or Capture payment API
        | * false = the payment does not require approval, and the funds will be captured automatically

        Type: bool
        """
        return self.__requires_approval

    @requires_approval.setter
    def requires_approval(self, value):
        self.__requires_approval = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificInput, self).to_dictionary()
        if self.authorization_mode is not None:
            dictionary['authorizationMode'] = self.authorization_mode
        if self.decrypted_payment_data is not None:
            dictionary['decryptedPaymentData'] = self.decrypted_payment_data.to_dictionary()
        if self.encrypted_payment_data is not None:
            dictionary['encryptedPaymentData'] = self.encrypted_payment_data
        if self.ephemeral_key is not None:
            dictionary['ephemeralKey'] = self.ephemeral_key
        if self.payment_product_id is not None:
            dictionary['paymentProductId'] = self.payment_product_id
        if self.public_key_hash is not None:
            dictionary['publicKeyHash'] = self.public_key_hash
        if self.requires_approval is not None:
            dictionary['requiresApproval'] = self.requires_approval
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'authorizationMode' in dictionary:
            self.authorization_mode = dictionary['authorizationMode']
        if 'decryptedPaymentData' in dictionary:
            if not isinstance(dictionary['decryptedPaymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['decryptedPaymentData']))
            value = DecryptedPaymentData()
            self.decrypted_payment_data = value.from_dictionary(dictionary['decryptedPaymentData'])
        if 'encryptedPaymentData' in dictionary:
            self.encrypted_payment_data = dictionary['encryptedPaymentData']
        if 'ephemeralKey' in dictionary:
            self.ephemeral_key = dictionary['ephemeralKey']
        if 'paymentProductId' in dictionary:
            self.payment_product_id = dictionary['paymentProductId']
        if 'publicKeyHash' in dictionary:
            self.public_key_hash = dictionary['publicKeyHash']
        if 'requiresApproval' in dictionary:
            self.requires_approval = dictionary['requiresApproval']
        return self
