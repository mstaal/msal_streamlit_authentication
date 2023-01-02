import os
from pathlib import Path
import streamlit.components.v1 as components


_USE_WEB_DEV_SERVER = os.getenv("USE_WEB_DEV_SERVER", True)

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(
        "msal_authentication", url="http://localhost:5173"
    )
else:
    build_dir = str(Path(__file__).parent / "frontend" / "dist")
    _component_func = components.declare_component("msal_authentication", path=build_dir)


def msal_authentication(client_id, authority, cache, login_request, key=None):
    authenticated_user_profile = _component_func(
        client_id=client_id,
        authority=authority,
        cache=cache,
        login_request=login_request,
        default=None,
        key=key
    )
    return authenticated_user_profile
