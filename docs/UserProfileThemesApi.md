# solifyn.UserProfileThemesApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get_my_page**](UserProfileThemesApi.md#users_get_my_page) | **GET** /v1/user/my-page | Get My Page details
[**users_get_my_theme**](UserProfileThemesApi.md#users_get_my_theme) | **GET** /v1/user/my-theme | Get My Theme
[**users_get_settings**](UserProfileThemesApi.md#users_get_settings) | **GET** /v1/user/settings | Retrieve User Settings
[**users_get_stats**](UserProfileThemesApi.md#users_get_stats) | **GET** /v1/user/dashboard-stats | Get Dashboard Statistics
[**users_get_theme_by_subdomain**](UserProfileThemesApi.md#users_get_theme_by_subdomain) | **GET** /v1/user/theme/{subdomain} | Get Theme by Subdomain


# **users_get_my_page**
> UserPage users_get_my_page()

Get My Page details

Retrieve page settings and custom content configured for the store.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_page import UserPage
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): ApiKeyAuth
configuration = solifyn.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.UserProfileThemesApi(api_client)

    try:
        # Get My Page details
        api_response = api_instance.users_get_my_page()
        print("The response of UserProfileThemesApi->users_get_my_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserProfileThemesApi->users_get_my_page: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserPage**](UserPage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store page configuration data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_my_theme**
> UserTheme users_get_my_theme()

Get My Theme

Retrieve theme configurations for the active business context.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_theme import UserTheme
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): ApiKeyAuth
configuration = solifyn.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.UserProfileThemesApi(api_client)

    try:
        # Get My Theme
        api_response = api_instance.users_get_my_theme()
        print("The response of UserProfileThemesApi->users_get_my_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserProfileThemesApi->users_get_my_theme: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserTheme**](UserTheme.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Active theme settings details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_settings**
> UserSettings users_get_settings()

Retrieve User Settings

Retrieve profile settings and notification preferences for the user.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_settings import UserSettings
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): ApiKeyAuth
configuration = solifyn.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.UserProfileThemesApi(api_client)

    try:
        # Retrieve User Settings
        api_response = api_instance.users_get_settings()
        print("The response of UserProfileThemesApi->users_get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserProfileThemesApi->users_get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserSettings**](UserSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User settings profile details retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_stats**
> UserStats users_get_stats()

Get Dashboard Statistics

Retrieve general analytics stats (revenue, order counts, etc.) for dashboard graphs.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_stats import UserStats
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): ApiKeyAuth
configuration = solifyn.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.UserProfileThemesApi(api_client)

    try:
        # Get Dashboard Statistics
        api_response = api_instance.users_get_stats()
        print("The response of UserProfileThemesApi->users_get_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserProfileThemesApi->users_get_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserStats**](UserStats.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dashboard analytics statistics data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_theme_by_subdomain**
> UserTheme users_get_theme_by_subdomain(subdomain)

Get Theme by Subdomain

Retrieve public theme configuration details by store subdomain.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_theme import UserTheme
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (API Key): ApiKeyAuth
configuration = solifyn.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.UserProfileThemesApi(api_client)
    subdomain = 'acme' # str | The subdomain of the store

    try:
        # Get Theme by Subdomain
        api_response = api_instance.users_get_theme_by_subdomain(subdomain)
        print("The response of UserProfileThemesApi->users_get_theme_by_subdomain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserProfileThemesApi->users_get_theme_by_subdomain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**| The subdomain of the store | 

### Return type

[**UserTheme**](UserTheme.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme configurations retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

