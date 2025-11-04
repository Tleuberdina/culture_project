from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_reviews_response_200 import ListReviewsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    product_id: str,
    *,
    page: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/products/{product_id}/reviews/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListReviewsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListReviewsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListReviewsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
) -> Response[ListReviewsResponse200]:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReviewsResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
) -> ListReviewsResponse200 | None:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReviewsResponse200
    """

    return sync_detailed(
        product_id=product_id,
        client=client,
        page=page,
    ).parsed


async def asyncio_detailed(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
) -> Response[ListReviewsResponse200]:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListReviewsResponse200]
    """

    kwargs = _get_kwargs(
        product_id=product_id,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    product_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
) -> ListReviewsResponse200 | None:
    """Обрабатывает операции CRUD для модели Review.

    Args:
        product_id (str):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListReviewsResponse200
    """

    return (
        await asyncio_detailed(
            product_id=product_id,
            client=client,
            page=page,
        )
    ).parsed
