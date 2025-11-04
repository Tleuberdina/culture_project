from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types

T = TypeVar("T", bound="PasswordResetConfirm")


@_attrs_define
class PasswordResetConfirm:
    """
    Attributes:
        uid (str):
        token (str):
        new_password (str):
    """

    uid: str
    token: str
    new_password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uid = self.uid

        token = self.token

        new_password = self.new_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uid": uid,
                "token": token,
                "new_password": new_password,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("uid", (None, str(self.uid).encode(), "text/plain")))

        files.append(("token", (None, str(self.token).encode(), "text/plain")))

        files.append(("new_password", (None, str(self.new_password).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uid = d.pop("uid")

        token = d.pop("token")

        new_password = d.pop("new_password")

        password_reset_confirm = cls(
            uid=uid,
            token=token,
            new_password=new_password,
        )

        password_reset_confirm.additional_properties = d
        return password_reset_confirm

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
