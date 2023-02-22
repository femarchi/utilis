"""
Sqlalchemy association proxy getset factories

https://docs.sqlalchemy.org/en/20/orm/extensions/associationproxy.html#sqlalchemy.ext.associationproxy.association_proxy.params.getset_factory
"""

def get_or_update(collection_type, proxy):
    def getter(obj):
        if obj is None:
            return None
        return getattr(obj, proxy.value_attr)

    def setter(obj, value):
        if value is None:
            return
        setattr(obj, proxy.value_attr, value)

    return getter, setter


def get_or_update_first(collection_type, proxy):
    def getter(obj):
        if obj is None:
            return None
        value = getattr(obj, proxy.value_attr)
        if value is None:
            return None
        return value[0]

    def setter(obj, value):
        if value is None:
            return
        values = getattr(obj, proxy.value_attr)
        if len(values) == 0:
            return
        values[0] = value

    return getter, setter


def get_or_set_first(collection_type, proxy):
    def getter(obj):
        if obj is None:
            return None
        value = getattr(obj, proxy.value_attr)
        if value is None:
            return None
        return value[0] if len(value) > 0 else []

    def setter(obj, value):
        values = getattr(obj, proxy.value_attr)
        if value is None:
            setattr(obj, proxy.value_attr, value)
        if len(values) == 0:
            setattr(obj, proxy.value_attr, [value])
        else:
            values[0] = value

    return getter, setter
