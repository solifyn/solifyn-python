# solifyn.RefundRequestsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refund_requests_list**](RefundRequestsApi.md#refund_requests_list) | **GET** /v1/refund-requests | List Refund Requests (Merchant)
[**refund_requests_list_messages**](RefundRequestsApi.md#refund_requests_list_messages) | **GET** /v1/refund-requests/{id}/messages | List Messages for Refund Request (Merchant)
[**refund_requests_send_message**](RefundRequestsApi.md#refund_requests_send_message) | **POST** /v1/refund-requests/{id}/messages | Send Refund Request Message (Merchant)
[**refund_requests_update_status**](RefundRequestsApi.md#refund_requests_update_status) | **PATCH** /v1/refund-requests/{id}/status | Update Refund Request Status (Merchant)
[**refund_requests_upload_evidence**](RefundRequestsApi.md#refund_requests_upload_evidence) | **POST** /v1/refund-requests/upload-evidence | Upload Dispute Evidence File (Merchant)


# **refund_requests_list**
> refund_requests_list()

List Refund Requests (Merchant)

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
    api_instance = solifyn.RefundRequestsApi(api_client)

    try:
        # List Refund Requests (Merchant)
        api_instance.refund_requests_list()
    except Exception as e:
        print("Exception when calling RefundRequestsApi->refund_requests_list: %s\n" % e)
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

# **refund_requests_list_messages**
> refund_requests_list_messages(id)

List Messages for Refund Request (Merchant)

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
    api_instance = solifyn.RefundRequestsApi(api_client)
    id = 'id_example' # str | 

    try:
        # List Messages for Refund Request (Merchant)
        api_instance.refund_requests_list_messages(id)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->refund_requests_list_messages: %s\n" % e)
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

# **refund_requests_send_message**
> refund_requests_send_message(id)

Send Refund Request Message (Merchant)

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
    api_instance = solifyn.RefundRequestsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Send Refund Request Message (Merchant)
        api_instance.refund_requests_send_message(id)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->refund_requests_send_message: %s\n" % e)
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_requests_update_status**
> refund_requests_update_status(id)

Update Refund Request Status (Merchant)

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
    api_instance = solifyn.RefundRequestsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Update Refund Request Status (Merchant)
        api_instance.refund_requests_update_status(id)
    except Exception as e:
        print("Exception when calling RefundRequestsApi->refund_requests_update_status: %s\n" % e)
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

# **refund_requests_upload_evidence**
> refund_requests_upload_evidence()

Upload Dispute Evidence File (Merchant)

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
    api_instance = solifyn.RefundRequestsApi(api_client)

    try:
        # Upload Dispute Evidence File (Merchant)
        api_instance.refund_requests_upload_evidence()
    except Exception as e:
        print("Exception when calling RefundRequestsApi->refund_requests_upload_evidence: %s\n" % e)
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

