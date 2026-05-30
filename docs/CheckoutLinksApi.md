# solifyn.CheckoutLinksApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_links_create**](CheckoutLinksApi.md#checkout_links_create) | **POST** /v1/checkout-links | Create Checkout Link
[**checkout_links_delete**](CheckoutLinksApi.md#checkout_links_delete) | **DELETE** /v1/checkout-links/{id} | Delete Checkout Link
[**checkout_links_get**](CheckoutLinksApi.md#checkout_links_get) | **GET** /v1/checkout-links/{id} | Retrieve Checkout Link Details
[**checkout_links_list**](CheckoutLinksApi.md#checkout_links_list) | **GET** /v1/checkout-links | List Checkout Links
[**checkout_links_update**](CheckoutLinksApi.md#checkout_links_update) | **PATCH** /v1/checkout-links/{id} | Update Checkout Link


# **checkout_links_create**
> CheckoutLinkResponseDto checkout_links_create(create_checkout_link_dto)

Create Checkout Link

Generate a new checkout session link.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.checkout_link_response_dto import CheckoutLinkResponseDto
from solifyn.models.create_checkout_link_dto import CreateCheckoutLinkDto
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
    api_instance = solifyn.CheckoutLinksApi(api_client)
    create_checkout_link_dto = solifyn.CreateCheckoutLinkDto() # CreateCheckoutLinkDto | 

    try:
        # Create Checkout Link
        api_response = api_instance.checkout_links_create(create_checkout_link_dto)
        print("The response of CheckoutLinksApi->checkout_links_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutLinksApi->checkout_links_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_checkout_link_dto** | [**CreateCheckoutLinkDto**](CreateCheckoutLinkDto.md)|  | 

### Return type

[**CheckoutLinkResponseDto**](CheckoutLinkResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Checkout link created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_links_delete**
> CheckoutLinkMessageResponseDto checkout_links_delete(id)

Delete Checkout Link

Permanently remove a checkout link.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.checkout_link_message_response_dto import CheckoutLinkMessageResponseDto
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
    api_instance = solifyn.CheckoutLinksApi(api_client)
    id = 'chk_123' # str | Checkout Link ID

    try:
        # Delete Checkout Link
        api_response = api_instance.checkout_links_delete(id)
        print("The response of CheckoutLinksApi->checkout_links_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutLinksApi->checkout_links_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Checkout Link ID | 

### Return type

[**CheckoutLinkMessageResponseDto**](CheckoutLinkMessageResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout link deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_links_get**
> CheckoutLinkResponseDto checkout_links_get(id)

Retrieve Checkout Link Details

Get details of a specific checkout link by ID (public access).

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.checkout_link_response_dto import CheckoutLinkResponseDto
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
    api_instance = solifyn.CheckoutLinksApi(api_client)
    id = 'chk_123' # str | Checkout Link ID

    try:
        # Retrieve Checkout Link Details
        api_response = api_instance.checkout_links_get(id)
        print("The response of CheckoutLinksApi->checkout_links_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutLinksApi->checkout_links_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Checkout Link ID | 

### Return type

[**CheckoutLinkResponseDto**](CheckoutLinkResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout link resolved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_links_list**
> List[CheckoutLinkResponseDto] checkout_links_list()

List Checkout Links

Retrieve all active checkout session links for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.checkout_link_response_dto import CheckoutLinkResponseDto
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
    api_instance = solifyn.CheckoutLinksApi(api_client)

    try:
        # List Checkout Links
        api_response = api_instance.checkout_links_list()
        print("The response of CheckoutLinksApi->checkout_links_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutLinksApi->checkout_links_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CheckoutLinkResponseDto]**](CheckoutLinkResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout links retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_links_update**
> CheckoutLinkMessageResponseDto checkout_links_update(id, update_checkout_link_dto)

Update Checkout Link

Update title, custom pricing, redirection URLs, or friendly inputs for a checkout link.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.checkout_link_message_response_dto import CheckoutLinkMessageResponseDto
from solifyn.models.update_checkout_link_dto import UpdateCheckoutLinkDto
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
    api_instance = solifyn.CheckoutLinksApi(api_client)
    id = 'chk_123' # str | Checkout Link ID
    update_checkout_link_dto = solifyn.UpdateCheckoutLinkDto() # UpdateCheckoutLinkDto | 

    try:
        # Update Checkout Link
        api_response = api_instance.checkout_links_update(id, update_checkout_link_dto)
        print("The response of CheckoutLinksApi->checkout_links_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutLinksApi->checkout_links_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Checkout Link ID | 
 **update_checkout_link_dto** | [**UpdateCheckoutLinkDto**](UpdateCheckoutLinkDto.md)|  | 

### Return type

[**CheckoutLinkMessageResponseDto**](CheckoutLinkMessageResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout link updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

