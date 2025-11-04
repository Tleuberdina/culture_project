from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.password_reset_confirm import PasswordResetConfirm
from ...types import Response


def _get_kwargs(
    *,
    body: PasswordResetConfirm | PasswordResetConfirm | PasswordResetConfirm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/users/reset_password_confirm/",
    }

    if isinstance(body, PasswordResetConfirm):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PasswordResetConfirm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, PasswordResetConfirm):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PasswordResetConfirm | None:
    if response.status_code == 201:
        response_201 = PasswordResetConfirm.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PasswordResetConfirm]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordResetConfirm | PasswordResetConfirm | PasswordResetConfirm,
) -> Response[PasswordResetConfirm]:
    """
    Args:
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasswordResetConfirm]
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
    body: PasswordResetConfirm | PasswordResetConfirm | PasswordResetConfirm,
) -> PasswordResetConfirm | None:
    """
    Args:
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasswordResetConfirm
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordResetConfirm | PasswordResetConfirm | PasswordResetConfirm,
) -> Response[PasswordResetConfirm]:
    """
    Args:
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PasswordResetConfirm]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PasswordResetConfirm | PasswordResetConfirm | PasswordResetConfirm,
) -> PasswordResetConfirm | None:
    """
    Args:
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):
        body (PasswordResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PasswordResetConfirm
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
