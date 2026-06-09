# solifyn.DiscountsApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**discounts_create**](DiscountsApi.md#discounts_create) | **POST** /v1/discounts | Create Discount
[**discounts_delete**](DiscountsApi.md#discounts_delete) | **DELETE** /v1/discounts/{id} | Delete Discount
[**discounts_get**](DiscountsApi.md#discounts_get) | **GET** /v1/discounts/{id} | Retrieve Discount
[**discounts_list**](DiscountsApi.md#discounts_list) | **GET** /v1/discounts | List Discounts
[**discounts_update**](DiscountsApi.md#discounts_update) | **PATCH** /v1/discounts/{id} | Update Discount
[**discounts_validate**](DiscountsApi.md#discounts_validate) | **GET** /v1/discounts/validate | Validate Code


# **discounts_create**
> Discount discounts_create(discount_create)

Create Discount

Create a new discount code within your active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.discount import Discount
from solifyn.models.discount_create import DiscountCreate
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    discount_create = solifyn.DiscountCreate() # DiscountCreate | 

    try:
        # Create Discount
        api_response = api_instance.discounts_create(discount_create)
        print("The response of DiscountsApi->discounts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discount_create** | [**DiscountCreate**](DiscountCreate.md)|  | 

### Return type

[**Discount**](Discount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Discount created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_delete**
> LicensesDeactivate200Response discounts_delete(id)

Delete Discount

Delete a specific discount code by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.licenses_deactivate200_response import LicensesDeactivate200Response
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    id = 'disc_123' # str | The unique discount ID.

    try:
        # Delete Discount
        api_response = api_instance.discounts_delete(id)
        print("The response of DiscountsApi->discounts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique discount ID. | 

### Return type

[**LicensesDeactivate200Response**](LicensesDeactivate200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discount deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_get**
> Discount discounts_get(id)

Retrieve Discount

Retrieve details of a specific discount code using its ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.discount import Discount
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    id = 'disc_123' # str | The unique discount ID.

    try:
        # Retrieve Discount
        api_response = api_instance.discounts_get(id)
        print("The response of DiscountsApi->discounts_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique discount ID. | 

### Return type

[**Discount**](Discount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved discount details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_list**
> DiscountsList200Response discounts_list(sorting=sorting, limit=limit, page=page, query=query, id=id)

List Discounts

List and query discounts belonging to your active business with support for fuzzy search by code, pagination, and sorting.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.discounts_list200_response import DiscountsList200Response
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    sorting = 'sorting_example' # str | Sorting criterion. Add a minus sign - before the criteria name to sort by descending order. (optional)
    limit = 10 # float | Size of a page, defaults to 10. Maximum is 100. (optional) (default to 10)
    page = 1 # float | Page number, defaults to 1. (optional) (default to 1)
    query = 'query_example' # str | Filter by discount code (fuzzy, case-insensitive). (optional)
    id = 'id_example' # str | Filter by discount ID. (optional)

    try:
        # List Discounts
        api_response = api_instance.discounts_list(sorting=sorting, limit=limit, page=page, query=query, id=id)
        print("The response of DiscountsApi->discounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sorting** | **str**| Sorting criterion. Add a minus sign - before the criteria name to sort by descending order. | [optional] 
 **limit** | **float**| Size of a page, defaults to 10. Maximum is 100. | [optional] [default to 10]
 **page** | **float**| Page number, defaults to 1. | [optional] [default to 1]
 **query** | **str**| Filter by discount code (fuzzy, case-insensitive). | [optional] 
 **id** | **str**| Filter by discount ID. | [optional] 

### Return type

[**DiscountsList200Response**](DiscountsList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved discounts list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_update**
> Discount discounts_update(id, discount_update)

Update Discount

Update details of an existing discount code.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.discount import Discount
from solifyn.models.discount_update import DiscountUpdate
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    id = 'disc_123' # str | The unique discount ID.
    discount_update = solifyn.DiscountUpdate() # DiscountUpdate | 

    try:
        # Update Discount
        api_response = api_instance.discounts_update(id, discount_update)
        print("The response of DiscountsApi->discounts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique discount ID. | 
 **discount_update** | [**DiscountUpdate**](DiscountUpdate.md)|  | 

### Return type

[**Discount**](Discount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Discount updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discounts_validate**
> Discount discounts_validate(code, business_id)

Validate Code

Validate if a specific discount code is active and valid for purchase checkout.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.discount import Discount
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
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
    api_instance = solifyn.DiscountsApi(api_client)
    code = 'SAVE20' # str | The plain discount code string
    business_id = 'biz_123' # str | The business database ID context

    try:
        # Validate Code
        api_response = api_instance.discounts_validate(code, business_id)
        print("The response of DiscountsApi->discounts_validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscountsApi->discounts_validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The plain discount code string | 
 **business_id** | **str**| The business database ID context | 

### Return type

[**Discount**](Discount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation query results. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

