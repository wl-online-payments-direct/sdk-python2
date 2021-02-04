#
# This class was auto-generated from the API references found at
# https://support.direct.ingenico.com/documentation/api/reference/
#
from ingenico.direct.sdk.api_resource import ApiResource
from ingenico.direct.sdk.response_exception import ResponseException
from ingenico.direct.sdk.domain.created_token_response import CreatedTokenResponse
from ingenico.direct.sdk.domain.error_response import ErrorResponse
from ingenico.direct.sdk.domain.token_response import TokenResponse
from ingenico.direct.sdk.merchant.tokens.i_tokens_client import ITokensClient


class TokensClient(ApiResource, ITokensClient):
    """
    Tokens client. Thread-safe.
    """

    def __init__(self, parent, path_context):
        """
        :param parent:       :class:`ingenico.direct.sdk.api_resource.ApiResource`
        :param path_context: dict[str, str]
        """
        super(TokensClient, self).__init__(parent, path_context)

    def create_token(self, body, context=None):
        """
        Resource /v2/{merchantId}/tokens - Create token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/CreateTokenApi

        :param body: :class:`ingenico.direct.sdk.domain.create_token_request.CreateTokenRequest`
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.created_token_response.CreatedTokenResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        uri = self._instantiate_uri("/v2/{merchantId}/tokens", None)
        try:
            return self._communicator.post(
                    uri,
                    self._client_headers,
                    None,
                    body,
                    CreatedTokenResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def get_token(self, token_id, context=None):
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Get token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/GetTokenApi

        :param token_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: :class:`ingenico.direct.sdk.domain.token_response.TokenResponse`
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.get(
                    uri,
                    self._client_headers,
                    None,
                    TokenResponse,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)

    def delete_token(self, token_id, context=None):
        """
        Resource /v2/{merchantId}/tokens/{tokenId} - Delete token

        See also https://support.direct.ingenico.com/documentation/api/reference#operation/DeleteTokenApi

        :param token_id: str
        :param context: :class:`ingenico.direct.sdk.call_context.CallContext`
        :return: None
        :raise: ValidationException if the request was not correct and couldn't be processed (HTTP status code 400)
        :raise: AuthorizationException if the request was not allowed (HTTP status code 403)
        :raise: ReferenceException if an object was attempted to be referenced that doesn't exist or has been removed,
                   or there was a conflict (HTTP status code 404, 409 or 410)
        :raise: DirectException if something went wrong at the Ingenico ePayments platform,
                   the Ingenico ePayments platform was unable to process a message from a downstream partner/acquirer,
                   or the service that you're trying to reach is temporary unavailable (HTTP status code 500, 502 or 503)
        :raise: ApiException if the Ingenico ePayments platform returned any other error
        """
        path_context = {
            "tokenId": token_id,
        }
        uri = self._instantiate_uri("/v2/{merchantId}/tokens/{tokenId}", path_context)
        try:
            return self._communicator.delete(
                    uri,
                    self._client_headers,
                    None,
                    None,
                    context)

        except ResponseException as e:
            error_type = ErrorResponse
            error_object = self._communicator.marshaller.unmarshal(e.body, error_type)
            raise self._create_exception(e.status_code, e.body, error_object, context)
