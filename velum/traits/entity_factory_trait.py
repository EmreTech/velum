import typing

from velum import models
from velum.internal import data_binding


class EntityFactory(typing.Protocol):

    __slots__: typing.Sequence[str] = ()

    def deserialize_message(self, payload: data_binding.JSONObject) -> models.Message:
        ...

    def deserialize_instance_info(self, payload: data_binding.JSONObject) -> models.InstanceInfo:
        ...
