# -*- coding: utf-8 -*-
#
# This class was auto-generated.
#
from onlinepayments.sdk.data_object import DataObject
from onlinepayments.sdk.domain.address import Address
from onlinepayments.sdk.domain.company_information import CompanyInformation
from onlinepayments.sdk.domain.contact_details import ContactDetails
from onlinepayments.sdk.domain.customer_account import CustomerAccount
from onlinepayments.sdk.domain.customer_device import CustomerDevice
from onlinepayments.sdk.domain.personal_information import PersonalInformation


class Customer(DataObject):
    """
    | Object containing the details of the customer
    """

    __account = None
    __account_type = None
    __billing_address = None
    __company_information = None
    __contact_details = None
    __device = None
    __fiscal_number = None
    __locale = None
    __merchant_customer_id = None
    __personal_information = None

    @property
    def account(self):
        """
        | Object containing data related to the account the customer has with you

        Type: :class:`onlinepayments.sdk.domain.customer_account.CustomerAccount`
        """
        return self.__account

    @account.setter
    def account(self, value):
        self.__account = value

    @property
    def account_type(self):
        """
        | Type of the customer account that is used to place this order. Can have one of the following values:
        |  * none - The account that was used to place the order with is a guest account or no account was used at all
        |  * created - The customer account was created during this transaction
        |  * existing - The customer account was an already existing account prior to this transaction

        Type: str
        """
        return self.__account_type

    @account_type.setter
    def account_type(self, value):
        self.__account_type = value

    @property
    def billing_address(self):
        """
        | Object containing billing address details

        Type: :class:`onlinepayments.sdk.domain.address.Address`
        """
        return self.__billing_address

    @billing_address.setter
    def billing_address(self, value):
        self.__billing_address = value

    @property
    def company_information(self):
        """
        | Object containing company information

        Type: :class:`onlinepayments.sdk.domain.company_information.CompanyInformation`
        """
        return self.__company_information

    @company_information.setter
    def company_information(self, value):
        self.__company_information = value

    @property
    def contact_details(self):
        """
        | Object containing contact details like email address and phone number

        Type: :class:`onlinepayments.sdk.domain.contact_details.ContactDetails`
        """
        return self.__contact_details

    @contact_details.setter
    def contact_details(self, value):
        self.__contact_details = value

    @property
    def device(self):
        """
        | Object containing information on the device and browser of the customer

        Type: :class:`onlinepayments.sdk.domain.customer_device.CustomerDevice`
        """
        return self.__device

    @device.setter
    def device(self, value):
        self.__device = value

    @property
    def fiscal_number(self):
        """
        | Fiscal registration number of the customer or the tax registration number of the company for a business customer. Please find below specifics per country:
        |  * Brazil - Consumer (CPF) with a length of 11 digits
        |  * Brazil - Company (CNPJ) with a length of 14 digits
        |  * Denmark - Consumer (CPR-nummer or personnummer) with a length of 10 digits
        |  * Finland - Consumer (Finnish: henkilötunnus (abbreviated as HETU), Swedish: personbeteckning) with a length of 11 characters
        |  * Norway - Consumer (fødselsnummer) with a length of 11 digits
        |  * Sweden - Consumer (personnummer) with a length of 10 or 12 digits

        Type: str
        """
        return self.__fiscal_number

    @fiscal_number.setter
    def fiscal_number(self, value):
        self.__fiscal_number = value

    @property
    def locale(self):
        """
        | The locale that the customer should be addressed in (for 3rd parties). Note that some 3rd party providers only support the languageCode part of the locale, in those cases we will only use part of the locale provided.

        Type: str
        """
        return self.__locale

    @locale.setter
    def locale(self, value):
        self.__locale = value

    @property
    def merchant_customer_id(self):
        """
        | Your identifier for the customer. It is used in the fraud-screening process for payments on the payment platform.

        Type: str
        """
        return self.__merchant_customer_id

    @merchant_customer_id.setter
    def merchant_customer_id(self, value):
        self.__merchant_customer_id = value

    @property
    def personal_information(self):
        """
        | Object containing personal information like name, date of birth and gender.

        Type: :class:`onlinepayments.sdk.domain.personal_information.PersonalInformation`
        """
        return self.__personal_information

    @personal_information.setter
    def personal_information(self, value):
        self.__personal_information = value

    def to_dictionary(self):
        dictionary = super(Customer, self).to_dictionary()
        if self.account is not None:
            dictionary['account'] = self.account.to_dictionary()
        if self.account_type is not None:
            dictionary['accountType'] = self.account_type
        if self.billing_address is not None:
            dictionary['billingAddress'] = self.billing_address.to_dictionary()
        if self.company_information is not None:
            dictionary['companyInformation'] = self.company_information.to_dictionary()
        if self.contact_details is not None:
            dictionary['contactDetails'] = self.contact_details.to_dictionary()
        if self.device is not None:
            dictionary['device'] = self.device.to_dictionary()
        if self.fiscal_number is not None:
            dictionary['fiscalNumber'] = self.fiscal_number
        if self.locale is not None:
            dictionary['locale'] = self.locale
        if self.merchant_customer_id is not None:
            dictionary['merchantCustomerId'] = self.merchant_customer_id
        if self.personal_information is not None:
            dictionary['personalInformation'] = self.personal_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(Customer, self).from_dictionary(dictionary)
        if 'account' in dictionary:
            if not isinstance(dictionary['account'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['account']))
            value = CustomerAccount()
            self.account = value.from_dictionary(dictionary['account'])
        if 'accountType' in dictionary:
            self.account_type = dictionary['accountType']
        if 'billingAddress' in dictionary:
            if not isinstance(dictionary['billingAddress'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['billingAddress']))
            value = Address()
            self.billing_address = value.from_dictionary(dictionary['billingAddress'])
        if 'companyInformation' in dictionary:
            if not isinstance(dictionary['companyInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['companyInformation']))
            value = CompanyInformation()
            self.company_information = value.from_dictionary(dictionary['companyInformation'])
        if 'contactDetails' in dictionary:
            if not isinstance(dictionary['contactDetails'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['contactDetails']))
            value = ContactDetails()
            self.contact_details = value.from_dictionary(dictionary['contactDetails'])
        if 'device' in dictionary:
            if not isinstance(dictionary['device'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['device']))
            value = CustomerDevice()
            self.device = value.from_dictionary(dictionary['device'])
        if 'fiscalNumber' in dictionary:
            self.fiscal_number = dictionary['fiscalNumber']
        if 'locale' in dictionary:
            self.locale = dictionary['locale']
        if 'merchantCustomerId' in dictionary:
            self.merchant_customer_id = dictionary['merchantCustomerId']
        if 'personalInformation' in dictionary:
            if not isinstance(dictionary['personalInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['personalInformation']))
            value = PersonalInformation()
            self.personal_information = value.from_dictionary(dictionary['personalInformation'])
        return self
