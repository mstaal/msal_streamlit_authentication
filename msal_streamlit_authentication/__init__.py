import os
import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components
from dotenv import load_dotenv

load_dotenv()

_USE_WEB_DEV_SERVER = os.getenv("USE_WEB_DEV_SERVER", True)
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
        auto_login=False,
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
        auto_login=auto_login,
        class_name=class_name,
        html_id=html_id,
        default=None,
        key=key
    )
    return authenticated_user_profile

if __name__ == "__main__":
    def login():
        load_dotenv()

        # https://pypi.org/project/msal-streamlit-authentication/
        login_token = msal_authentication(
            auth={
                "clientId": os.getenv('APPLICATION_ID', 'ff3a2c7e-a88d-4e90-8201-b5cb84631bcd'),
                "authority": f"https://login.microsoftonline.com/{os.getenv('TENANT_ID', '6264083e-3421-458b-886b-69ca1fc46f5b')}",
                "redirectUri": os.getenv('REDIRECT_URI', "http://localhost:5173"),
                "postLogoutRedirectUri": "/"
            }, # Corresponds to the 'auth' configuration for an MSAL Instance
            cache={
                "cacheLocation": "sessionStorage",
                "storeAuthStateInCookie": False
            }, # Corresponds to the 'cache' configuration for an MSAL Instance
            login_request={
                "scopes": ["https://graph.microsoft.com/.default"]
            }, # Optional
            # logout_request={}, # Optional
            # login_button_text="Login", # Optional, defaults to "Login"
            # logout_button_text="Logout", # Optional, defaults to "Logout"
            auto_login=True,
            # class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
            # html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
            key=1 # Optional if only a single instance is needed
        )
        st.write("Recevied login token:", login_token)

        return login_token


    st.header("Hello World!")
    login_token = login()
    st.write("Recevied login token:", login_token)