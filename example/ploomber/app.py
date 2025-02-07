import streamlit as st
import os

from msal_streamlit_authentication import msal_authentication

st.title("Streamlit MSAL Anthentication 🔒")

value = msal_authentication(
    auth={
        "clientId": os.getenv("ENTRA_CLIENT_ID"),
        "authority": f"https://login.microsoftonline.com/{os.getenv('ENTRA_TENANT_ID')}",
        "redirectUri": os.getenv("ENTRA_REDIRECT_URI"),
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": ["https://graph.microsoft.com/.default"]
    },
    key="1")

st.write("Received", value)
