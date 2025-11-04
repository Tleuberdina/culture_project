from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.username_reset_confirm import UsernameResetConfirm
from ...types import Response


def _get_kwargs(
    *,
    body: UsernameResetConfirm | UsernameResetConfirm | UsernameResetConfirm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/auth/users/reset_username_confirm/",
    }

    if isinstance(body, UsernameResetConfirm):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UsernameResetConfirm):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, UsernameResetConfirm):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UsernameResetConfirm | None:
    if response.status_code == 201:
        response_201 = UsernameResetConfirm.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[UsernameResetConfirm]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UsernameResetConfirm | UsernameResetConfirm | UsernameResetConfirm,
) -> Response[UsernameResetConfirm]:
    """
    Args:
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsernameResetConfirm]
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
    body: UsernameResetConfirm | UsernameResetConfirm | UsernameResetConfirm,
) -> UsernameResetConfirm | None:
    """
    Args:
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsernameResetConfirm
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UsernameResetConfirm | UsernameResetConfirm | UsernameResetConfirm,
) -> Response[UsernameResetConfirm]:
    """
    Args:
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsernameResetConfirm]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UsernameResetConfirm | UsernameResetConfirm | UsernameResetConfirm,
) -> UsernameResetConfirm | None:
    """
    Args:
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):
        body (UsernameResetConfirm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UsernameResetConfirm
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
