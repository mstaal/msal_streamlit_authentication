import streamlit as st
import os
from dotenv import load_dotenv
import streamlit as st
import requests
import msal
# from msal_streamlit_authentication import msal_authentication
import urllib

def login():
    load_dotenv()

    # https://pypi.org/project/msal-streamlit-authentication/
    login_token = msal_authentication(
        auth={
            "clientId": os.getenv('APPLICATION_ID', '7be9e197-f235-4b03-a465-513db8c467db'),
            "authority": f"https://login.microsoftonline.com/{os.getenv('TENANT_ID', '6264083e-3421-458b-886b-69ca1fc46f5b')}",
            "redirectUri": os.getenv('REDIRECT_URI', "https://aisearch.azurewebsites.net/"),
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
        # class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
        # html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
        key=1 # Optional if only a single instance is needed
    )
    st.write("Recevied login token:", login_token)

    return login_token


st.header("Hello World! This is a test of the MSAL Streamlit Authentication package.")
login_token = login()
st.write("Recevied login token:", login_token)