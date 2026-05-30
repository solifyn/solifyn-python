# solifyn.BusinessesApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**businesses_billing_history**](BusinessesApi.md#businesses_billing_history) | **GET** /v1/user/billing/history | Get Platform Billing History
[**merchants_generate_api_keys**](BusinessesApi.md#merchants_generate_api_keys) | **POST** /v1/user/whop-api-keys | Rotate Whop API Keys
[**merchants_update_page**](BusinessesApi.md#merchants_update_page) | **PATCH** /v1/user/page | Update Page configuration
[**merchants_update_settings**](BusinessesApi.md#merchants_update_settings) | **PATCH** /v1/user/settings | Update Merchant Settings
[**merchants_update_theme**](BusinessesApi.md#merchants_update_theme) | **PATCH** /v1/user/theme | Update Theme


# **businesses_billing_history**
> businesses_billing_history()

Get Platform Billing History

Retrieve history of SaaS subscription payments paid by this business to the platform.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
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
    api_instance = solifyn.BusinessesApi(api_client)

    try:
        # Get Platform Billing History
        api_instance.businesses_billing_history()
    except Exception as e:
        print("Exception when calling BusinessesApi->businesses_billing_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchants_generate_api_keys**
> WhopApiKeysRotation merchants_generate_api_keys()

Rotate Whop API Keys

Generate and sync a new Whop Child Company API key (restricted to business owners).

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.whop_api_keys_rotation import WhopApiKeysRotation
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
    api_instance = solifyn.BusinessesApi(api_client)

    try:
        # Rotate Whop API Keys
        api_response = api_instance.merchants_generate_api_keys()
        print("The response of BusinessesApi->merchants_generate_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessesApi->merchants_generate_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WhopApiKeysRotation**](WhopApiKeysRotation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Whop child API credentials successfully rotated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchants_update_page**
> UserPage merchants_update_page(user_theme_update)

Update Page configuration

Modify store page content configs, banner images, or avatar details.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_page import UserPage
from solifyn.models.user_theme_update import UserThemeUpdate
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
    api_instance = solifyn.BusinessesApi(api_client)
    user_theme_update = solifyn.UserThemeUpdate() # UserThemeUpdate | 

    try:
        # Update Page configuration
        api_response = api_instance.merchants_update_page(user_theme_update)
        print("The response of BusinessesApi->merchants_update_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessesApi->merchants_update_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_theme_update** | [**UserThemeUpdate**](UserThemeUpdate.md)|  | 

### Return type

[**UserPage**](UserPage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store page settings updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchants_update_settings**
> UserSettings merchants_update_settings(user_settings_update)

Update Merchant Settings

Update profile parameters, SEO, Google analytics, and email notification properties.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_settings import UserSettings
from solifyn.models.user_settings_update import UserSettingsUpdate
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
    api_instance = solifyn.BusinessesApi(api_client)
    user_settings_update = solifyn.UserSettingsUpdate() # UserSettingsUpdate | 

    try:
        # Update Merchant Settings
        api_response = api_instance.merchants_update_settings(user_settings_update)
        print("The response of BusinessesApi->merchants_update_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessesApi->merchants_update_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_settings_update** | [**UserSettingsUpdate**](UserSettingsUpdate.md)|  | 

### Return type

[**UserSettings**](UserSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User settings successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchants_update_theme**
> UserTheme merchants_update_theme(user_theme_update)

Update Theme

Update colors, fonts, avatar, or banner settings for the store.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.user_theme import UserTheme
from solifyn.models.user_theme_update import UserThemeUpdate
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
    api_instance = solifyn.BusinessesApi(api_client)
    user_theme_update = solifyn.UserThemeUpdate() # UserThemeUpdate | 

    try:
        # Update Theme
        api_response = api_instance.merchants_update_theme(user_theme_update)
        print("The response of BusinessesApi->merchants_update_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BusinessesApi->merchants_update_theme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_theme_update** | [**UserThemeUpdate**](UserThemeUpdate.md)|  | 

### Return type

[**UserTheme**](UserTheme.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme settings successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

