# solifyn.DeveloperApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_create_api_key**](DeveloperApi.md#developer_create_api_key) | **POST** /v1/developer/api-keys | Create Developer API Key
[**developer_create_webhook**](DeveloperApi.md#developer_create_webhook) | **POST** /v1/developer/webhooks | Create Webhook Endpoint
[**developer_delete_webhook**](DeveloperApi.md#developer_delete_webhook) | **DELETE** /v1/developer/webhooks/{id} | Delete Webhook Endpoint
[**developer_get_app_portal**](DeveloperApi.md#developer_get_app_portal) | **GET** /v1/developer/webhooks/app-portal | Retrieve Hosted Webhooks Portal URL
[**developer_get_webhook**](DeveloperApi.md#developer_get_webhook) | **GET** /v1/developer/webhooks/{id} | Retrieve Webhook Endpoint Details
[**developer_list_api_keys**](DeveloperApi.md#developer_list_api_keys) | **GET** /v1/developer/api-keys | List Developer API Keys
[**developer_list_webhook_deliveries**](DeveloperApi.md#developer_list_webhook_deliveries) | **GET** /v1/developer/webhooks/{id}/deliveries | Retrieve Webhook Delivery Logs
[**developer_list_webhooks**](DeveloperApi.md#developer_list_webhooks) | **GET** /v1/developer/webhooks | List Webhook Endpoints
[**developer_revoke_api_key**](DeveloperApi.md#developer_revoke_api_key) | **DELETE** /v1/developer/api-keys/{id} | Revoke API Key
[**developer_update_webhook**](DeveloperApi.md#developer_update_webhook) | **PATCH** /v1/developer/webhooks/{id} | Update Webhook Endpoint


# **developer_create_api_key**
> ApiKeyResponseDto developer_create_api_key(create_api_key_dto)

Create Developer API Key

### Example


```python
import solifyn
from solifyn.models.api_key_response_dto import ApiKeyResponseDto
from solifyn.models.create_api_key_dto import CreateApiKeyDto
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
    api_instance = solifyn.DeveloperApi(api_client)
    create_api_key_dto = solifyn.CreateApiKeyDto() # CreateApiKeyDto | 

    try:
        # Create Developer API Key
        api_response = api_instance.developer_create_api_key(create_api_key_dto)
        print("The response of DeveloperApi->developer_create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_create_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key_dto** | [**CreateApiKeyDto**](CreateApiKeyDto.md)|  | 

### Return type

[**ApiKeyResponseDto**](ApiKeyResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_create_webhook**
> WebhookEndpointResponseDto developer_create_webhook(create_webhook_endpoint_dto)

Create Webhook Endpoint

### Example


```python
import solifyn
from solifyn.models.create_webhook_endpoint_dto import CreateWebhookEndpointDto
from solifyn.models.webhook_endpoint_response_dto import WebhookEndpointResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)
    create_webhook_endpoint_dto = solifyn.CreateWebhookEndpointDto() # CreateWebhookEndpointDto | 

    try:
        # Create Webhook Endpoint
        api_response = api_instance.developer_create_webhook(create_webhook_endpoint_dto)
        print("The response of DeveloperApi->developer_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_endpoint_dto** | [**CreateWebhookEndpointDto**](CreateWebhookEndpointDto.md)|  | 

### Return type

[**WebhookEndpointResponseDto**](WebhookEndpointResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_delete_webhook**
> developer_delete_webhook(id)

Delete Webhook Endpoint

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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | The webhook endpoint ID

    try:
        # Delete Webhook Endpoint
        api_instance.developer_delete_webhook(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The webhook endpoint ID | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_get_app_portal**
> AppPortalUrlResponseDto developer_get_app_portal()

Retrieve Hosted Webhooks Portal URL

### Example


```python
import solifyn
from solifyn.models.app_portal_url_response_dto import AppPortalUrlResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        # Retrieve Hosted Webhooks Portal URL
        api_response = api_instance.developer_get_app_portal()
        print("The response of DeveloperApi->developer_get_app_portal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_get_app_portal: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppPortalUrlResponseDto**](AppPortalUrlResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_get_webhook**
> WebhookEndpointResponseDto developer_get_webhook(id)

Retrieve Webhook Endpoint Details

### Example


```python
import solifyn
from solifyn.models.webhook_endpoint_response_dto import WebhookEndpointResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | The webhook endpoint ID

    try:
        # Retrieve Webhook Endpoint Details
        api_response = api_instance.developer_get_webhook(id)
        print("The response of DeveloperApi->developer_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The webhook endpoint ID | 

### Return type

[**WebhookEndpointResponseDto**](WebhookEndpointResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_list_api_keys**
> List[ApiKeyResponseDto] developer_list_api_keys()

List Developer API Keys

### Example


```python
import solifyn
from solifyn.models.api_key_response_dto import ApiKeyResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        # List Developer API Keys
        api_response = api_instance.developer_list_api_keys()
        print("The response of DeveloperApi->developer_list_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_list_api_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKeyResponseDto]**](ApiKeyResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_list_webhook_deliveries**
> List[WebhookDeliveryResponseDto] developer_list_webhook_deliveries(id)

Retrieve Webhook Delivery Logs

### Example


```python
import solifyn
from solifyn.models.webhook_delivery_response_dto import WebhookDeliveryResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | The webhook endpoint ID

    try:
        # Retrieve Webhook Delivery Logs
        api_response = api_instance.developer_list_webhook_deliveries(id)
        print("The response of DeveloperApi->developer_list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The webhook endpoint ID | 

### Return type

[**List[WebhookDeliveryResponseDto]**](WebhookDeliveryResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_list_webhooks**
> List[WebhookEndpointResponseDto] developer_list_webhooks()

List Webhook Endpoints

### Example


```python
import solifyn
from solifyn.models.webhook_endpoint_response_dto import WebhookEndpointResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        # List Webhook Endpoints
        api_response = api_instance.developer_list_webhooks()
        print("The response of DeveloperApi->developer_list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_list_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[WebhookEndpointResponseDto]**](WebhookEndpointResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_revoke_api_key**
> developer_revoke_api_key(id)

Revoke API Key

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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | The API key ID

    try:
        # Revoke API Key
        api_instance.developer_revoke_api_key(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_revoke_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The API key ID | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_update_webhook**
> WebhookEndpointResponseDto developer_update_webhook(id, update_webhook_endpoint_dto)

Update Webhook Endpoint

### Example


```python
import solifyn
from solifyn.models.update_webhook_endpoint_dto import UpdateWebhookEndpointDto
from solifyn.models.webhook_endpoint_response_dto import WebhookEndpointResponseDto
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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | The webhook endpoint ID
    update_webhook_endpoint_dto = solifyn.UpdateWebhookEndpointDto() # UpdateWebhookEndpointDto | 

    try:
        # Update Webhook Endpoint
        api_response = api_instance.developer_update_webhook(id, update_webhook_endpoint_dto)
        print("The response of DeveloperApi->developer_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The webhook endpoint ID | 
 **update_webhook_endpoint_dto** | [**UpdateWebhookEndpointDto**](UpdateWebhookEndpointDto.md)|  | 

### Return type

[**WebhookEndpointResponseDto**](WebhookEndpointResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

