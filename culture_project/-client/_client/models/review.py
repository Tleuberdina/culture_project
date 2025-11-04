from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="Review")


@_attrs_define
class Review:
    """
    Attributes:
        text (str):
        id (int | Unset):
        estimation (int | Unset):
        author (str | Unset):
        created (datetime.datetime | Unset):
        product (str | Unset):
    """

    text: str
    id: int | Unset = UNSET
    estimation: int | Unset = UNSET
    author: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    product: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        id = self.id

        estimation = self.estimation

        author = self.author

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        product = self.product

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if estimation is not UNSET:
            field_dict["estimation"] = estimation
        if author is not UNSET:
            field_dict["author"] = author
        if created is not UNSET:
            field_dict["created"] = created
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("text", (None, str(self.text).encode(), "text/plain")))

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.estimation, Unset):
            files.append(("estimation", (None, str(self.estimation).encode(), "text/plain")))

        if not isinstance(self.author, Unset):
            files.append(("author", (None, str(self.author).encode(), "text/plain")))

        if not isinstance(self.created, Unset):
            files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))

        if not isinstance(self.product, Unset):
            files.append(("product", (None, str(self.product).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        id = d.pop("id", UNSET)

        estimation = d.pop("estimation", UNSET)

        author = d.pop("author", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        product = d.pop("product", UNSET)

        review = cls(
            text=text,
            id=id,
            estimation=estimation,
            author=author,
            created=created,
            product=product,
        )

        review.additional_properties = d
        return review

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
