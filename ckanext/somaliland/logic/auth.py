import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def somaliland_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "somaliland_get_sum": somaliland_get_sum,
    }
