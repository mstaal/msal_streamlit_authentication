# streamlit_msal_sample
Reference project for using [msal-streamlit-authentication](https://github.com/ploomber/msal_streamlit_authentication)

# Get Started

1. Configure the application
Edit [dashboard.py](./app/dashboard.py), by providing the `msal_authentication` with your Single Page Application config. Don't forget to set the callback url to `https://localhost:8501`

    ```python
    value = msal_authentication(
        auth={
            "clientId": "CLIENT_ID",
            "authority": "https://login.microsoftonline.com/TENANT_ID",
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
        key=1
    )
    ```

2. Build the Docker container
    ```sh
	docker build -t streamlit .
    ```

3. Run the container
    ```sh
	 docker run -p 8501:8501 streamlit
    ```

4. Naviguate to `https://localhost:8501` to see the demo
