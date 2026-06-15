# solifyn.DiscordIntegrationApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discord_disconnect**](DiscordIntegrationApi.md#discord_disconnect) | **POST** /v1/discord/disconnect | Disconnect Discord Integration
[**discord_get_install_url**](DiscordIntegrationApi.md#discord_get_install_url) | **GET** /v1/discord/install | Get Discord Bot Installation URL
[**discord_list_roles**](DiscordIntegrationApi.md#discord_list_roles) | **GET** /v1/discord/roles | List Guild Discord Roles


# **discord_disconnect**
> discord_disconnect()

Disconnect Discord Integration

Disconnects the Discord Bot integration by removing the guild ID from the business profile.

### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.DiscordIntegrationApi(api_client)

    try:
        # Disconnect Discord Integration
        api_instance.discord_disconnect()
    except Exception as e:
        print("Exception when calling DiscordIntegrationApi->discord_disconnect: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully disconnected. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discord_get_install_url**
> discord_get_install_url(product_id=product_id)

Get Discord Bot Installation URL

Generates the URL to invite the system-wide Discord Bot onto the merchant's Discord server.

### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.DiscordIntegrationApi(api_client)
    product_id = 'product_id_example' # str | Optional Product ID to redirect back to after installation (optional)

    try:
        # Get Discord Bot Installation URL
        api_instance.discord_get_install_url(product_id=product_id)
    except Exception as e:
        print("Exception when calling DiscordIntegrationApi->discord_get_install_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Optional Product ID to redirect back to after installation | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the generated installation URL. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discord_list_roles**
> List[DiscordRolesResponseDto] discord_list_roles()

List Guild Discord Roles

Retrieves all roles available in the connected merchant's Discord server/guild.

### Example


```python
import solifyn
from solifyn.models.discord_roles_response_dto import DiscordRolesResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.DiscordIntegrationApi(api_client)

    try:
        # List Guild Discord Roles
        api_response = api_instance.discord_list_roles()
        print("The response of DiscordIntegrationApi->discord_list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscordIntegrationApi->discord_list_roles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DiscordRolesResponseDto]**](DiscordRolesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of server roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

