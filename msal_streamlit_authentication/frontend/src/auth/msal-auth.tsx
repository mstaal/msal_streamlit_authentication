import {BrowserAuthOptions, CacheOptions, LogLevel, PublicClientApplication} from "@azure/msal-browser";

export const useMsalInstance = function (auth_config: BrowserAuthOptions, cache_config: CacheOptions) {
    return new PublicClientApplication({
        auth: auth_config,
        cache: cache_config,
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
