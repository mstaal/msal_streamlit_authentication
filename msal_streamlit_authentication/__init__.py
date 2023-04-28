import os
from pathlib import Path
import streamlit.components.v1 as components


_USE_WEB_DEV_SERVER = os.getenv("USE_WEB_DEV_SERVER", False)
_WEB_DEV_SERVER_URL = os.getenv("WEB_DEV_SERVER_URL", "http://localhost:5173")
COMPONENT_NAME = "msal_authentication"

if _USE_WEB_DEV_SERVER:
    _component_func = components.declare_component(name=COMPONENT_NAME, url=_WEB_DEV_SERVER_URL)
else:
    build_dir = str(Path(__file__).parent / "frontend" / "dist")
    _component_func = components.declare_component(name=COMPONENT_NAME, path=build_dir)


def msal_authentication(
        auth,
        cache,
        login_request=None,
        logout_request=None,
        login_button_text="Login",
        logout_button_text="Logout",
        class_name=None,
        html_id=None,
        key=None
):
    authenticated_user_profile = _component_func(
        auth=auth,
        cache=cache,
        login_request=login_request,
        logout_request=logout_request,
        login_button_text=login_button_text,
        logout_button_text=logout_button_text,
        class_name=class_name,
        html_id=html_id,
        default=None,
        key=key
    )
    return authenticated_user_profile
