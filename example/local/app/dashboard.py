import streamlit as st

from msal_streamlit_authentication import msal_authentication

st.title("Streamlit MSAL Anthentication 🔒")

value = msal_authentication(
    auth={
        "clientId": "{CLIENT_ID_HERE}",
        "authority": "https://login.microsoftonline.com/{TENANT_ID_HERE}",
        "redirectUri": "http://localhost:8501/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": ["https://graph.microsoft.com/.default"]
    },
    key=1)

st.write("Received", value)
