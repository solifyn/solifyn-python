# solifyn.RefundsChargebacksApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**refunds_create**](RefundsChargebacksApi.md#refunds_create) | **POST** /v1/orders/{id}/refund | Create Refund
[**refunds_get**](RefundsChargebacksApi.md#refunds_get) | **GET** /v1/refunds/{id} | Retrieve Refund details
[**refunds_list**](RefundsChargebacksApi.md#refunds_list) | **GET** /v1/refunds | List Refunds


# **refunds_create**
> refunds_create(id, order_refund_create)

Create Refund

Initiate a full or partial refund for a specific payment/order.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.order_refund_create import OrderRefundCreate
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
    api_instance = solifyn.RefundsChargebacksApi(api_client)
    id = 'pay_123' # str | The unique order/payment ID.
    order_refund_create = solifyn.OrderRefundCreate() # OrderRefundCreate | 

    try:
        # Create Refund
        api_instance.refunds_create(id, order_refund_create)
    except Exception as e:
        print("Exception when calling RefundsChargebacksApi->refunds_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique order/payment ID. | 
 **order_refund_create** | [**OrderRefundCreate**](OrderRefundCreate.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Refund processed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refunds_get**
> Refund refunds_get(id)

Retrieve Refund details

Get parameters of a specific processed refund by database ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.refund import Refund
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
    api_instance = solifyn.RefundsChargebacksApi(api_client)
    id = 'ref_123' # str | Refund ID

    try:
        # Retrieve Refund details
        api_response = api_instance.refunds_get(id)
        print("The response of RefundsChargebacksApi->refunds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsChargebacksApi->refunds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Refund ID | 

### Return type

[**Refund**](Refund.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund resolved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refunds_list**
> List[Refund] refunds_list()

List Refunds

Retrieve a list of processed refunds and chargeback transactions.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.refund import Refund
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
    api_instance = solifyn.RefundsChargebacksApi(api_client)

    try:
        # List Refunds
        api_response = api_instance.refunds_list()
        print("The response of RefundsChargebacksApi->refunds_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RefundsChargebacksApi->refunds_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Refund]**](Refund.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refunds list retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

