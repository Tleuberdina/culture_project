from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        email (str | Unset):
        id (int | Unset):
        username (str | Unset): Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.
    """

    email: str | Unset = UNSET
    id: int | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        id = self.id

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.email, Unset):
            files.append(("email", (None, str(self.email).encode(), "text/plain")))

        if not isinstance(self.id, Unset):
            files.append(("id", (None, str(self.id).encode(), "text/plain")))

        if not isinstance(self.username, Unset):
            files.append(("username", (None, str(self.username).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        user = cls(
            email=email,
            id=id,
            username=username,
        )

        user.additional_properties = d
        return user

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
