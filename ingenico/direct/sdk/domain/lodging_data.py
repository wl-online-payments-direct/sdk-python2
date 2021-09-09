# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.data_object import DataObject


class LodgingData(DataObject):
    """
    | Object that holds lodging specific data
    """

    __check_in_date = None

    @property
    def check_in_date(self):
        """
        | The date the guest checks into (or plans to check in to) the facility.
        | Format YYYYMMDD

        Type: str
        """
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        self.__check_in_date = value

    def to_dictionary(self):
        dictionary = super(LodgingData, self).to_dictionary()
        if self.check_in_date is not None:
            dictionary['checkInDate'] = self.check_in_date
        return dictionary

    def from_dictionary(self, dictionary):
        super(LodgingData, self).from_dictionary(dictionary)
        if 'checkInDate' in dictionary:
            self.check_in_date = dictionary['checkInDate']
        return self
