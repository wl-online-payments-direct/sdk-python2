from abc import ABCMeta, abstractmethod


class SecretKeyStore(object):
    """
    A store of secret keys. Implementations could store secret keys in a database, on disk, etc.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_secret_key(self, key_id):
        """
        :return: The secret key for the given key ID. Never None.
        :raise: SecretKeyNotAvailableException: If the secret key for the given
         key ID is not available.
        """
