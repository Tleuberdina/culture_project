from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.review import Review
from ...types import Response


def _get_kwargs(
    product_id: str,
    id: str,
    *,
    body: Review | Review | Review,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/products/{product_id}/reviews/{id}/",
    }

    if isinstance(body, Review):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, Review):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, Review):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Review | None:
    if response.status_code == 200:
        response_200 = Review.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Review]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Review | Review | Review,
) -> Response[Review]:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        id (str):
        body (Review):
        body (Review):
        body (Review):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Review]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Review | Review | Review,
) -> Review | None:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        id (str):
        body (Review):
        body (Review):
        body (Review):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Review
    """

    return sync_detailed(
        product_id=product_id,
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Review | Review | Review,
) -> Response[Review]:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        id (str):
        body (Review):
        body (Review):
        body (Review):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Review]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Review | Review | Review,
) -> Review | None:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        id (str):
        body (Review):
        body (Review):
        body (Review):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Review
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            id=id,
            client=client,
            body=body,
        )
    ).parsed
