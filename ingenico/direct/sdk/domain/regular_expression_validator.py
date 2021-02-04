# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class RegularExpressionValidator(DataObject):

    __regular_expression = None

    @property
    def regular_expression(self):
        """
        Type: str
        """
        return self.__regular_expression

    @regular_expression.setter
    def regular_expression(self, value):
        self.__regular_expression = value

    def to_dictionary(self):
        dictionary = super(RegularExpressionValidator, self).to_dictionary()
        if self.regular_expression is not None:
            dictionary['regularExpression'] = self.regular_expression
        return dictionary

    def from_dictionary(self, dictionary):
        super(RegularExpressionValidator, self).from_dictionary(dictionary)
        if 'regularExpression' in dictionary:
            self.regular_expression = dictionary['regularExpression']
        return self
