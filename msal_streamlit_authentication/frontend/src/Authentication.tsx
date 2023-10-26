import React, { useCallback, useEffect, useState } from "react"
import {
    withStreamlitConnection,
    Streamlit,
    ComponentProps,
} from "streamlit-component-lib"
import { useMsalInstance } from "./auth/msal-auth";

const Authentication = ({ args }: ComponentProps) => {
    const msalInstance = useMsalInstance(args["auth"], args["cache"])
    const loginRequest = args["login_request"] ?? undefined
    const logoutRequest = args["logout_request"] ?? undefined
    const loginButtonText = args["login_button_text"] ?? ""
    const logoutButtonText = args["logout_button_text"] ?? ""
    const auto_login = args["auto_login"] ?? false
    const buttonClass = args["class_name"] ?? ""
    const buttonId = args["html_id"] ?? ""

    const [loginToken, setLoginToken] = useState(null)
    const isAuthenticated = useCallback(() => {
        return msalInstance.getAllAccounts().length > 0
    }, [])

    useEffect(() => {
        if (msalInstance.getAllAccounts().length > 0) {
            msalInstance.acquireTokenSilent({
                ...loginRequest,
                account: msalInstance.getAllAccounts()[0]
            }).then(function (response) {
                // @ts-ignore
                setLoginToken(response)
            })
        } else {
            setLoginToken(null)

            console.log("loginPopup...")
            loginPopup();
        }
    }, [])

    useEffect(() => {
        Streamlit.setComponentValue(loginToken)
        Streamlit.setFrameHeight()
        Streamlit.setComponentReady()
    }, [loginToken])

    const loginPopup = useCallback(() => {
        msalInstance.loginPopup(loginRequest).then(function (response) {
            // @ts-ignore
            setLoginToken(response)
        }).catch(console.error)
    }, [])

    const logoutPopup = useCallback(() => {
        // @ts-ignore
        msalInstance.logoutPopup(logoutRequest).then(function (response) {
            setLoginToken(null)
        }).catch(console.error)
    }, [])

    return (
        <div className="card">
        {
            auto_login === false ? (
                <button onClick={isAuthenticated() ? logoutPopup : loginPopup} className={buttonClass} id={buttonId}>
                {isAuthenticated() ? logoutButtonText : loginButtonText}
                </button>
            ) : null
        }
        </div>
    )

}

export default withStreamlitConnection(Authentication)
