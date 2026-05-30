# solifyn.DeveloperApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developer_controller_create_api_key**](DeveloperApi.md#developer_controller_create_api_key) | **POST** /v1/developer/api-keys | 
[**developer_controller_create_webhook_endpoint**](DeveloperApi.md#developer_controller_create_webhook_endpoint) | **POST** /v1/developer/webhooks | 
[**developer_controller_delete_api_key**](DeveloperApi.md#developer_controller_delete_api_key) | **DELETE** /v1/developer/api-keys/{id} | 
[**developer_controller_delete_webhook_endpoint**](DeveloperApi.md#developer_controller_delete_webhook_endpoint) | **DELETE** /v1/developer/webhooks/{id} | 
[**developer_controller_get_api_keys**](DeveloperApi.md#developer_controller_get_api_keys) | **GET** /v1/developer/api-keys | 
[**developer_controller_get_app_portal_url**](DeveloperApi.md#developer_controller_get_app_portal_url) | **GET** /v1/developer/webhooks/app-portal | 
[**developer_controller_get_webhook_deliveries**](DeveloperApi.md#developer_controller_get_webhook_deliveries) | **GET** /v1/developer/webhooks/{id}/deliveries | 
[**developer_controller_get_webhook_endpoints**](DeveloperApi.md#developer_controller_get_webhook_endpoints) | **GET** /v1/developer/webhooks | 
[**developer_controller_update_webhook_endpoint**](DeveloperApi.md#developer_controller_update_webhook_endpoint) | **PATCH** /v1/developer/webhooks/{id} | 


# **developer_controller_create_api_key**
> developer_controller_create_api_key()



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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        api_instance.developer_controller_create_api_key()
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_create_api_key: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_controller_create_webhook_endpoint**
> developer_controller_create_webhook_endpoint()



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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        api_instance.developer_controller_create_webhook_endpoint()
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_create_webhook_endpoint: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_controller_delete_api_key**
> developer_controller_delete_api_key(id)



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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.developer_controller_delete_api_key(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_delete_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **developer_controller_delete_webhook_endpoint**
> developer_controller_delete_webhook_endpoint(id)



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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.developer_controller_delete_webhook_endpoint(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_delete_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **developer_controller_get_api_keys**
> developer_controller_get_api_keys()



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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        api_instance.developer_controller_get_api_keys()
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_get_api_keys: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_controller_get_app_portal_url**
> developer_controller_get_app_portal_url()



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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        api_instance.developer_controller_get_app_portal_url()
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_get_app_portal_url: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_controller_get_webhook_deliveries**
> developer_controller_get_webhook_deliveries(id)



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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.developer_controller_get_webhook_deliveries(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_get_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **developer_controller_get_webhook_endpoints**
> developer_controller_get_webhook_endpoints()



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
    api_instance = solifyn.DeveloperApi(api_client)

    try:
        api_instance.developer_controller_get_webhook_endpoints()
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_get_webhook_endpoints: %s\n" % e)
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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **developer_controller_update_webhook_endpoint**
> developer_controller_update_webhook_endpoint(id)



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
    api_instance = solifyn.DeveloperApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.developer_controller_update_webhook_endpoint(id)
    except Exception as e:
        print("Exception when calling DeveloperApi->developer_controller_update_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

