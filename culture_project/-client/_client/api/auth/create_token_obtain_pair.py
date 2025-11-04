from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token_obtain_pair import TokenObtainPair
from ...types import Response


def _get_kwargs(
    *,
    body: TokenObtainPair | TokenObtainPair | TokenObtainPair,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/jwt/create/",
    }

    if isinstance(body, TokenObtainPair):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TokenObtainPair):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, TokenObtainPair):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TokenObtainPair | None:
    if response.status_code == 201:
        response_201 = TokenObtainPair.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TokenObtainPair]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenObtainPair | TokenObtainPair | TokenObtainPair,
) -> Response[TokenObtainPair]:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.

    Args:
        body (TokenObtainPair):
        body (TokenObtainPair):
        body (TokenObtainPair):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenObtainPair]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TokenObtainPair | TokenObtainPair | TokenObtainPair,
) -> TokenObtainPair | None:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.

    Args:
        body (TokenObtainPair):
        body (TokenObtainPair):
        body (TokenObtainPair):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenObtainPair
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenObtainPair | TokenObtainPair | TokenObtainPair,
) -> Response[TokenObtainPair]:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.

    Args:
        body (TokenObtainPair):
        body (TokenObtainPair):
        body (TokenObtainPair):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TokenObtainPair]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TokenObtainPair | TokenObtainPair | TokenObtainPair,
) -> TokenObtainPair | None:
    """Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.

    Args:
        body (TokenObtainPair):
        body (TokenObtainPair):
        body (TokenObtainPair):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TokenObtainPair
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
