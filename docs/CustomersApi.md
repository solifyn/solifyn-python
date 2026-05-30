# solifyn.CustomersApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_create**](CustomersApi.md#customers_create) | **POST** /v1/customers | Create Customer
[**customers_generate_invite**](CustomersApi.md#customers_generate_invite) | **POST** /v1/customers/{id}/share | Generate Shared Invite
[**customers_get**](CustomersApi.md#customers_get) | **GET** /v1/customers/{id} | Retrieve Customer
[**customers_list**](CustomersApi.md#customers_list) | **GET** /v1/customers | List Customers
[**customers_update**](CustomersApi.md#customers_update) | **PATCH** /v1/customers/{id} | Update Customer


# **customers_create**
> CustomerResponseDto customers_create(create_customer_dto)

Create Customer

Add/upsert a new customer profile under the current business context.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.create_customer_dto import CreateCustomerDto
from solifyn.models.customer_response_dto import CustomerResponseDto
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
    api_instance = solifyn.CustomersApi(api_client)
    create_customer_dto = solifyn.CreateCustomerDto() # CreateCustomerDto | 

    try:
        # Create Customer
        api_response = api_instance.customers_create(create_customer_dto)
        print("The response of CustomersApi->customers_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_customer_dto** | [**CreateCustomerDto**](CreateCustomerDto.md)|  | 

### Return type

[**CustomerResponseDto**](CustomerResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Customer created/updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_generate_invite**
> CustomerSharedInviteResponseDto customers_generate_invite(id)

Generate Shared Invite

Generate a short-lived token granting temporary customer self-service billing page access.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.customer_shared_invite_response_dto import CustomerSharedInviteResponseDto
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
    api_instance = solifyn.CustomersApi(api_client)
    id = 'user_123' # str | Customer ID

    try:
        # Generate Shared Invite
        api_response = api_instance.customers_generate_invite(id)
        print("The response of CustomersApi->customers_generate_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_generate_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

[**CustomerSharedInviteResponseDto**](CustomerSharedInviteResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Self-service billing portal invite token created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_get**
> CustomerResponseDto customers_get(id)

Retrieve Customer

Retrieve details of a customer profile by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.customer_response_dto import CustomerResponseDto
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
    api_instance = solifyn.CustomersApi(api_client)
    id = 'user_123' # str | Customer ID

    try:
        # Retrieve Customer
        api_response = api_instance.customers_get(id)
        print("The response of CustomersApi->customers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 

### Return type

[**CustomerResponseDto**](CustomerResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_list**
> CustomerListResponseDto customers_list()

List Customers

Retrieve all customers associated with the current active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.customer_list_response_dto import CustomerListResponseDto
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
    api_instance = solifyn.CustomersApi(api_client)

    try:
        # List Customers
        api_response = api_instance.customers_list()
        print("The response of CustomersApi->customers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomerListResponseDto**](CustomerListResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of customers retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_update**
> CustomerMessageResponseDto customers_update(id, update_customer_dto)

Update Customer

Update name, phone, or metadata of an existing customer profile.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.customer_message_response_dto import CustomerMessageResponseDto
from solifyn.models.update_customer_dto import UpdateCustomerDto
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
    api_instance = solifyn.CustomersApi(api_client)
    id = 'user_123' # str | Customer ID
    update_customer_dto = solifyn.UpdateCustomerDto() # UpdateCustomerDto | 

    try:
        # Update Customer
        api_response = api_instance.customers_update(id, update_customer_dto)
        print("The response of CustomersApi->customers_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomersApi->customers_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Customer ID | 
 **update_customer_dto** | [**UpdateCustomerDto**](UpdateCustomerDto.md)|  | 

### Return type

[**CustomerMessageResponseDto**](CustomerMessageResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Customer updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

