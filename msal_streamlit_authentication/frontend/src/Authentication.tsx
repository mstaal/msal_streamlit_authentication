import React, { useCallback, useEffect, useState } from "react"
import {
    withStreamlitConnection,
    Streamlit,
    ComponentProps,
} from "streamlit-component-lib"
import { useMsalInstance } from "./auth/msal-auth";
import "./Authentication.css"

const Authentication = ({ args }: ComponentProps) => {
    const msalInstance = useMsalInstance(args["auth"], args["cache"])
    const loginRequest = args["login_request"] ?? undefined
    const logoutRequest = args["logout_request"] ?? undefined
    const loginButtonText = args["login_button_text"] ?? ""
    const logoutButtonText = args["logout_button_text"] ?? ""

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
            <button onClick={isAuthenticated() ? logoutPopup : loginPopup}>
                {isAuthenticated() ? logoutButtonText : loginButtonText}
            </button>
        </div>
    )

}

export default withStreamlitConnection(Authentication)
