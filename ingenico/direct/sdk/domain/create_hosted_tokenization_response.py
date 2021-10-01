# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class CreateHostedTokenizationResponse(DataObject):

    __hosted_tokenization_id = None
    __invalid_tokens = None
    __partial_redirect_url = None

    @property
    def hosted_tokenization_id(self):
        """
        | The ID of the Hosted Tokenization Session

        Type: str
        """
        return self.__hosted_tokenization_id

    @hosted_tokenization_id.setter
    def hosted_tokenization_id(self, value):
        self.__hosted_tokenization_id = value

    @property
    def invalid_tokens(self):
        """
        | Tokens that are submitted in the request are validated. Tokens that cannot be used in the current session are returned in this array. 
        | These tokens might not be valid anymore. The validity of tokens can be verified using the [Get token](#operation/GetTokenApi) endpoint.

        Type: list[str]
        """
        return self.__invalid_tokens

    @invalid_tokens.setter
    def invalid_tokens(self, value):
        self.__invalid_tokens = value

    @property
    def partial_redirect_url(self):
        """
        | The partial URL as generated by our system. You will need to add the protocol and the relevant subdomain to this URL, before redirecting your customer to this URL. A special 'payment' subdomain will always work so you can always add 'https://payment.' at the beginning of this response value to view your hosted pages.

        Type: str
        """
        return self.__partial_redirect_url

    @partial_redirect_url.setter
    def partial_redirect_url(self, value):
        self.__partial_redirect_url = value

    def to_dictionary(self):
        dictionary = super(CreateHostedTokenizationResponse, self).to_dictionary()
        if self.hosted_tokenization_id is not None:
            dictionary['hostedTokenizationId'] = self.hosted_tokenization_id
        if self.invalid_tokens is not None:
            dictionary['invalidTokens'] = []
            for element in self.invalid_tokens:
                if element is not None:
                    dictionary['invalidTokens'].append(element)
        if self.partial_redirect_url is not None:
            dictionary['partialRedirectUrl'] = self.partial_redirect_url
        return dictionary

    def from_dictionary(self, dictionary):
        super(CreateHostedTokenizationResponse, self).from_dictionary(dictionary)
        if 'hostedTokenizationId' in dictionary:
            self.hosted_tokenization_id = dictionary['hostedTokenizationId']
        if 'invalidTokens' in dictionary:
            if not isinstance(dictionary['invalidTokens'], list):
                raise TypeError('value \'{}\' is not a list'.format(dictionary['invalidTokens']))
            self.invalid_tokens = []
            for element in dictionary['invalidTokens']:
                self.invalid_tokens.append(element)
        if 'partialRedirectUrl' in dictionary:
            self.partial_redirect_url = dictionary['partialRedirectUrl']
        return self