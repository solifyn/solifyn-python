# solifyn.WebhookEndpointApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operational_webhook_controller_create**](WebhookEndpointApi.md#operational_webhook_controller_create) | **POST** /v1/operational-webhook/endpoint | Create Operational Webhook Endpoint
[**operational_webhook_controller_delete**](WebhookEndpointApi.md#operational_webhook_controller_delete) | **DELETE** /v1/operational-webhook/endpoint/{id} | Delete Operational Webhook Endpoint
[**operational_webhook_controller_get**](WebhookEndpointApi.md#operational_webhook_controller_get) | **GET** /v1/operational-webhook/endpoint/{id} | Get Operational Webhook Endpoint
[**operational_webhook_controller_get_headers**](WebhookEndpointApi.md#operational_webhook_controller_get_headers) | **GET** /v1/operational-webhook/endpoint/{id}/headers | Get Operational Webhook Endpoint Headers
[**operational_webhook_controller_get_secret**](WebhookEndpointApi.md#operational_webhook_controller_get_secret) | **GET** /v1/operational-webhook/endpoint/{id}/secret | Get Operational Webhook Endpoint Secret
[**operational_webhook_controller_list**](WebhookEndpointApi.md#operational_webhook_controller_list) | **GET** /v1/operational-webhook/endpoint | List Operational Webhook Endpoints
[**operational_webhook_controller_rotate_secret**](WebhookEndpointApi.md#operational_webhook_controller_rotate_secret) | **POST** /v1/operational-webhook/endpoint/{id}/secret/rotate | Rotate Operational Webhook Endpoint Secret
[**operational_webhook_controller_update**](WebhookEndpointApi.md#operational_webhook_controller_update) | **PUT** /v1/operational-webhook/endpoint/{id} | Update Operational Webhook Endpoint
[**operational_webhook_controller_update_headers**](WebhookEndpointApi.md#operational_webhook_controller_update_headers) | **PUT** /v1/operational-webhook/endpoint/{id}/headers | Set Operational Webhook Endpoint Headers


# **operational_webhook_controller_create**
> OperationalWebhookEndpointResponseDto operational_webhook_controller_create(operational_webhook_endpoint_in_dto)

Create Operational Webhook Endpoint

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_in_dto import OperationalWebhookEndpointInDto
from solifyn.models.operational_webhook_endpoint_response_dto import OperationalWebhookEndpointResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    operational_webhook_endpoint_in_dto = solifyn.OperationalWebhookEndpointInDto() # OperationalWebhookEndpointInDto | 

    try:
        # Create Operational Webhook Endpoint
        api_response = api_instance.operational_webhook_controller_create(operational_webhook_endpoint_in_dto)
        print("The response of WebhookEndpointApi->operational_webhook_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operational_webhook_endpoint_in_dto** | [**OperationalWebhookEndpointInDto**](OperationalWebhookEndpointInDto.md)|  | 

### Return type

[**OperationalWebhookEndpointResponseDto**](OperationalWebhookEndpointResponseDto.md)

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

# **operational_webhook_controller_delete**
> operational_webhook_controller_delete(id)

Delete Operational Webhook Endpoint

### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID

    try:
        # Delete Operational Webhook Endpoint
        api_instance.operational_webhook_controller_delete(id)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 

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
**204** | Deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operational_webhook_controller_get**
> OperationalWebhookEndpointResponseDto operational_webhook_controller_get(id)

Get Operational Webhook Endpoint

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_response_dto import OperationalWebhookEndpointResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID

    try:
        # Get Operational Webhook Endpoint
        api_response = api_instance.operational_webhook_controller_get(id)
        print("The response of WebhookEndpointApi->operational_webhook_controller_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 

### Return type

[**OperationalWebhookEndpointResponseDto**](OperationalWebhookEndpointResponseDto.md)

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

# **operational_webhook_controller_get_headers**
> OperationalWebhookEndpointHeadersResponseDto operational_webhook_controller_get_headers(id)

Get Operational Webhook Endpoint Headers

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_headers_response_dto import OperationalWebhookEndpointHeadersResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID

    try:
        # Get Operational Webhook Endpoint Headers
        api_response = api_instance.operational_webhook_controller_get_headers(id)
        print("The response of WebhookEndpointApi->operational_webhook_controller_get_headers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_get_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 

### Return type

[**OperationalWebhookEndpointHeadersResponseDto**](OperationalWebhookEndpointHeadersResponseDto.md)

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

# **operational_webhook_controller_get_secret**
> OperationalWebhookEndpointSecretResponseDto operational_webhook_controller_get_secret(id)

Get Operational Webhook Endpoint Secret

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_secret_response_dto import OperationalWebhookEndpointSecretResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID

    try:
        # Get Operational Webhook Endpoint Secret
        api_response = api_instance.operational_webhook_controller_get_secret(id)
        print("The response of WebhookEndpointApi->operational_webhook_controller_get_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_get_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 

### Return type

[**OperationalWebhookEndpointSecretResponseDto**](OperationalWebhookEndpointSecretResponseDto.md)

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

# **operational_webhook_controller_list**
> OperationalWebhookEndpointListResponseDto operational_webhook_controller_list()

List Operational Webhook Endpoints

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_list_response_dto import OperationalWebhookEndpointListResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)

    try:
        # List Operational Webhook Endpoints
        api_response = api_instance.operational_webhook_controller_list()
        print("The response of WebhookEndpointApi->operational_webhook_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OperationalWebhookEndpointListResponseDto**](OperationalWebhookEndpointListResponseDto.md)

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

# **operational_webhook_controller_rotate_secret**
> operational_webhook_controller_rotate_secret(id, operational_webhook_endpoint_secret_in_dto)

Rotate Operational Webhook Endpoint Secret

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_secret_in_dto import OperationalWebhookEndpointSecretInDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID
    operational_webhook_endpoint_secret_in_dto = solifyn.OperationalWebhookEndpointSecretInDto() # OperationalWebhookEndpointSecretInDto | 

    try:
        # Rotate Operational Webhook Endpoint Secret
        api_instance.operational_webhook_controller_rotate_secret(id, operational_webhook_endpoint_secret_in_dto)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_rotate_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 
 **operational_webhook_endpoint_secret_in_dto** | [**OperationalWebhookEndpointSecretInDto**](OperationalWebhookEndpointSecretInDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Secret rotated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operational_webhook_controller_update**
> OperationalWebhookEndpointResponseDto operational_webhook_controller_update(id, operational_webhook_endpoint_update_dto)

Update Operational Webhook Endpoint

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_response_dto import OperationalWebhookEndpointResponseDto
from solifyn.models.operational_webhook_endpoint_update_dto import OperationalWebhookEndpointUpdateDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID
    operational_webhook_endpoint_update_dto = solifyn.OperationalWebhookEndpointUpdateDto() # OperationalWebhookEndpointUpdateDto | 

    try:
        # Update Operational Webhook Endpoint
        api_response = api_instance.operational_webhook_controller_update(id, operational_webhook_endpoint_update_dto)
        print("The response of WebhookEndpointApi->operational_webhook_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 
 **operational_webhook_endpoint_update_dto** | [**OperationalWebhookEndpointUpdateDto**](OperationalWebhookEndpointUpdateDto.md)|  | 

### Return type

[**OperationalWebhookEndpointResponseDto**](OperationalWebhookEndpointResponseDto.md)

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

# **operational_webhook_controller_update_headers**
> operational_webhook_controller_update_headers(id, operational_webhook_endpoint_headers_in_dto)

Set Operational Webhook Endpoint Headers

### Example


```python
import solifyn
from solifyn.models.operational_webhook_endpoint_headers_in_dto import OperationalWebhookEndpointHeadersInDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.WebhookEndpointApi(api_client)
    id = 'id_example' # str | The endpoint ID or UID
    operational_webhook_endpoint_headers_in_dto = solifyn.OperationalWebhookEndpointHeadersInDto() # OperationalWebhookEndpointHeadersInDto | 

    try:
        # Set Operational Webhook Endpoint Headers
        api_instance.operational_webhook_controller_update_headers(id, operational_webhook_endpoint_headers_in_dto)
    except Exception as e:
        print("Exception when calling WebhookEndpointApi->operational_webhook_controller_update_headers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The endpoint ID or UID | 
 **operational_webhook_endpoint_headers_in_dto** | [**OperationalWebhookEndpointHeadersInDto**](OperationalWebhookEndpointHeadersInDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Headers set |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

