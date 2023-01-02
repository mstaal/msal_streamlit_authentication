import { LogLevel, PublicClientApplication } from "@azure/msal-browser";

export const useMsalInstance = function (clientId: string, authority: string, cache: string) {
    return new PublicClientApplication({
        auth: {
            clientId: clientId,
            authority: authority, // This is a URL (e.g. https://login.microsoftonline.com/{your tenant ID})
            redirectUri: "/",
            postLogoutRedirectUri: "/"
        },
        cache: {
            cacheLocation: cache, // This configures where your cache will be stored
            storeAuthStateInCookie: false, // Set this to "true" if you are having issues on IE11 or Edge
        },
        system: {
            loggerOptions: {
                loggerCallback: (level: LogLevel, message: string, containsPii: any) => {
                    if (containsPii) {
                        return;
                    }
                    switch (level) {
                        case LogLevel.Error:
                            console.error(message);
                            return;
                        case LogLevel.Info:
                            return;
                        case LogLevel.Verbose:
                            console.debug(message);
                            return;
                        case LogLevel.Warning:
                            console.warn(message);
                            return;
                        default:
                            return;
                    }
                }
            }
        }
    })
}
