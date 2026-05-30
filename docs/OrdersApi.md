# solifyn.OrdersApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_get**](OrdersApi.md#orders_get) | **GET** /v1/orders/{id} | Retrieve Order
[**orders_get_invoice**](OrdersApi.md#orders_get_invoice) | **GET** /v1/orders/{id}/invoice | Get Order Invoice
[**orders_list**](OrdersApi.md#orders_list) | **GET** /v1/orders | List Orders
[**orders_update**](OrdersApi.md#orders_update) | **PATCH** /v1/orders/{id} | Update Order Billing Address
[**refunds_create**](OrdersApi.md#refunds_create) | **POST** /v1/orders/{id}/refund | Create Refund


# **orders_get**
> Order orders_get(id)

Retrieve Order

Retrieve details of a specific order/payment by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.order import Order
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
    api_instance = solifyn.OrdersApi(api_client)
    id = 'pay_123' # str | The unique order/payment ID.

    try:
        # Retrieve Order
        api_response = api_instance.orders_get(id)
        print("The response of OrdersApi->orders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique order/payment ID. | 

### Return type

[**Order**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order resolved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get_invoice**
> Invoice orders_get_invoice(id)

Get Order Invoice

Retrieve the generated invoice details for the specified order.

### Example


```python
import solifyn
from solifyn.models.invoice import Invoice
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
    api_instance = solifyn.OrdersApi(api_client)
    id = 'pay_123' # str | The unique order/payment ID.

    try:
        # Get Order Invoice
        api_response = api_instance.orders_get_invoice(id)
        print("The response of OrdersApi->orders_get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique order/payment ID. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invoice retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_list**
> OrderList orders_list(created_at_lte=created_at_lte, created_at_gte=created_at_gte, product_id=product_id, customer_id=customer_id, status=status, page_size=page_size, page_number=page_number)

List Orders

List and query orders/payments belonging to your active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.order_list import OrderList
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
    api_instance = solifyn.OrdersApi(api_client)
    created_at_lte = 'created_at_lte_example' # str | Filter by creation date less than or equal to. (optional)
    created_at_gte = 'created_at_gte_example' # str | Filter by creation date greater than or equal to. (optional)
    product_id = 'product_id_example' # str | Filter by product identifier. (optional)
    customer_id = 'customer_id_example' # str | Filter by customer identifier. (optional)
    status = 'status_example' # str | Filter by order/payment status. (optional)
    page_size = 10 # float | Size of a page, defaults to 10. Maximum is 100. (optional) (default to 10)
    page_number = 1 # float | Page number, defaults to 1. (optional) (default to 1)

    try:
        # List Orders
        api_response = api_instance.orders_list(created_at_lte=created_at_lte, created_at_gte=created_at_gte, product_id=product_id, customer_id=customer_id, status=status, page_size=page_size, page_number=page_number)
        print("The response of OrdersApi->orders_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_lte** | **str**| Filter by creation date less than or equal to. | [optional] 
 **created_at_gte** | **str**| Filter by creation date greater than or equal to. | [optional] 
 **product_id** | **str**| Filter by product identifier. | [optional] 
 **customer_id** | **str**| Filter by customer identifier. | [optional] 
 **status** | **str**| Filter by order/payment status. | [optional] 
 **page_size** | **float**| Size of a page, defaults to 10. Maximum is 100. | [optional] [default to 10]
 **page_number** | **float**| Page number, defaults to 1. | [optional] [default to 1]

### Return type

[**OrderList**](OrderList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of orders/payments retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_update**
> Order orders_update(id, order_update)

Update Order Billing Address

Update the billing details of an existing order.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.order import Order
from solifyn.models.order_update import OrderUpdate
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
    api_instance = solifyn.OrdersApi(api_client)
    id = 'pay_123' # str | The unique order/payment ID.
    order_update = solifyn.OrderUpdate() # OrderUpdate | 

    try:
        # Update Order Billing Address
        api_response = api_instance.orders_update(id, order_update)
        print("The response of OrdersApi->orders_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->orders_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique order/payment ID. | 
 **order_update** | [**OrderUpdate**](OrderUpdate.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order billing address updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = solifyn.OrdersApi(api_client)
    id = 'pay_123' # str | The unique order/payment ID.
    order_refund_create = solifyn.OrderRefundCreate() # OrderRefundCreate | 

    try:
        # Create Refund
        api_instance.refunds_create(id, order_refund_create)
    except Exception as e:
        print("Exception when calling OrdersApi->refunds_create: %s\n" % e)
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

