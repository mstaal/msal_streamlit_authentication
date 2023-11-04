# OpenID Connect (OIDC) authentication component for Streamlit

## About

This Streamlit component enables client-side authentication using [Azure AD](https://docs.microsoft.com/azure/active-directory/develop/v2-overview) work and school accounts (AAD), Microsoft personal accounts (MSA) and social identity providers like Facebook, Google, LinkedIn, Microsoft accounts, etc. through [Azure AD B2C](https://docs.microsoft.com/azure/active-directory-b2c/active-directory-b2c-overview#identity-providers) service.
The component is achieving this by applying the [Microsoft MSAL JS Library](https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-browser) inside of a React project. Since the component is based on MSAL, it can be configured to support any provider that supports the OpenID Connect Authorization Code Flow (PKCE).
For more information on MSAL, consult the [Github project](https://github.com/AzureAD/microsoft-authentication-library-for-js/tree/dev/lib/msal-browser) and its [offical documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview).

## Usage

Below is a sample Python snippet displaying how to apply the component. Visually, the component gives rise to a single button
in the Streamlit Dashboard with a text that depends on whether an active login session exists. The `auth` and `cache`
parameters are entirely equivalent to the properties mentioned in the [Github documentation](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/initialization.md).
The `login_request` and `logout_request` parameters are covered [here](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/login-user.md).
```python
import streamlit as st
from msal_streamlit_authentication import msal_authentication


login_token = msal_authentication(
    auth={
        "clientId": "aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "authority": "https://login.microsoftonline.com/aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    }, # Corresponds to the 'auth' configuration for an MSAL Instance
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    }, # Corresponds to the 'cache' configuration for an MSAL Instance
    login_request={
        "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    }, # Optional
    logout_request={}, # Optional
    login_button_text="Login", # Optional, defaults to "Login"
    logout_button_text="Logout", # Optional, defaults to "Logout"
    class_name="css_button_class_selector", # Optional, defaults to None. Corresponds to HTML class.
    html_id="html_id_for_button", # Optional, defaults to None. Corresponds to HTML id.
    key=1 # Optional if only a single instance is needed
)
st.write("Recevied login token:", login_token)
```
A minimal sample project using the library can be found [here](https://github.com/mstaal/streamlit_msal_sample). Note that it is Dockerized.

The component currently expects for the user to go through a popup based login flow.
Further flows may be supported at a later time. As discussed [here](https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/initialization.md#optional-configure-authority),
the `protocolMode` parameter in `auth` can be used to configure OIDC providers that differ from Azure AD.

## Inspiration
Inspired by [official Streamlit template](https://github.com/streamlit/component-template), [this tutorial](https://youtu.be/htXgwEXwmNs) ([Github](https://github.com/andfanilo/streamlit-plotly-component-tutorial)) and the official [Streamlit NPM component-lib](https://github.com/streamlit/streamlit/tree/develop/component-lib).

