import operator
from functools import reduce


def convert_structured_attributes(data):
    """
    Receive dict object and lookup for structured fields.
    Returns dict with converted structured fields to dict.
    E.g.:

    From:
    {
    address.address_line1: "Some address"
    address.city: "Some city"
    address.state: "Some state"
    address.zip: "Some zip"
    }

    To:
    "address": {
    "address_line1": "Some address",
    "city": "Some city",
    "state": "Some state",
    "zip": "Some zip"
    }
    """

    converted = {}
    for k, v in data.items():
        structure = k.split('.')
        if len(structure) > 1:
            if not structure[0] in converted:
                converted[structure[0]] = {}
            set_in_dict(converted, structure, v)
        else:
            converted[k] = v
    return converted


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)
