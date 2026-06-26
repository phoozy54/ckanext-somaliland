import ckan.plugins.toolkit as tk


def somaliland_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "somaliland_required": somaliland_required,
    }
