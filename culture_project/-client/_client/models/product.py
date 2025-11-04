from __future__ import annotations

import datetime
from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        name (str):
        text (str):
        id (int | Unset):
        author (str | Unset):
        created (datetime.datetime | Unset):
        average_score (float | Unset):
        image (File | None | Unset):
    """

    name: str
    text: str
    id: int | Unset = UNSET
    author: str | Unset = UNSET
    created: datetime.datetime | Unset = UNSET
    average_score: float | Unset = UNSET
    image: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        text = self.text

        id = self.id

        author = self.author

        created: str | Unset = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        average_score = self.average_score

        image: FileTypes | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        elif isinstance(self.image, File):
            image = self.image.to_tuple()

        else:
            image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "text": text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if author is not UNSET:
            field_dict["author"] = author
        if created is not UNSET:
            field_dict["created"] = created
        if average_score is not UNSET:
            field_dict["average_score"] = average_score
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("text", (None, str(self.text).encode(), "text/plain")))

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.author, Unset):
            files.append(("author", (None, str(self.author).encode(), "text/plain")))

        if not isinstance(self.created, Unset):
            files.append(("created", (None, self.created.isoformat().encode(), "text/plain")))

        if not isinstance(self.average_score, Unset):
            files.append(("average_score", (None, str(self.average_score).encode(), "text/plain")))

        if not isinstance(self.image, Unset):
            if isinstance(self.image, File):
                files.append(("image", self.image.to_tuple()))
            else:
                files.append(("image", (None, str(self.image).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        text = d.pop("text")

        id = d.pop("id", UNSET)

        author = d.pop("author", UNSET)

        _created = d.pop("created", UNSET)
        created: datetime.datetime | Unset
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        average_score = d.pop("average_score", UNSET)

        def _parse_image(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                image_type_0 = File(payload=BytesIO(data))

                return image_type_0
            except:  # noqa: E722
                pass
            return cast(File | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))

        product = cls(
            name=name,
            text=text,
            id=id,
            author=author,
            created=created,
            average_score=average_score,
            image=image,
        )

        product.additional_properties = d
        return product

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
