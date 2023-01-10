import typing

from magicgui import type_map

def get_default_widget(field_name: str, field_value: typing.Any, field_type: typing.Any):
    new_widget_cls, ops = type_map.get_widget_class(
        None,
        field_type,
        dict(name=field_name, value=field_value, annotation=field_type),
        raise_on_unknown=False,
    )
    return new_widget_cls, ops
