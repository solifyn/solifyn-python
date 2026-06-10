# solifyn.WebhookApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_controller_handle_svix_webhook**](WebhookApi.md#webhook_controller_handle_svix_webhook) | **POST** /v1/webhook/svix | 
[**webhook_controller_handle_webhook**](WebhookApi.md#webhook_controller_handle_webhook) | **POST** /v1/webhook | 


# **webhook_controller_handle_svix_webhook**
> webhook_controller_handle_svix_webhook()



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
    api_instance = solifyn.WebhookApi(api_client)

    try:
        api_instance.webhook_controller_handle_svix_webhook()
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_controller_handle_svix_webhook: %s\n" % e)
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

# **webhook_controller_handle_webhook**
> webhook_controller_handle_webhook(business_id)



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
    api_instance = solifyn.WebhookApi(api_client)
    business_id = 'business_id_example' # str | 

    try:
        api_instance.webhook_controller_handle_webhook(business_id)
    except Exception as e:
        print("Exception when calling WebhookApi->webhook_controller_handle_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_id** | **str**|  | 

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

