# solifyn.ProductsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_archive**](ProductsApi.md#products_archive) | **DELETE** /v1/products/{id} | Archive Product
[**products_create**](ProductsApi.md#products_create) | **POST** /v1/products | Create Product
[**products_get**](ProductsApi.md#products_get) | **GET** /v1/products/{id} | Retrieve Product
[**products_list**](ProductsApi.md#products_list) | **GET** /v1/products | List Products
[**products_unarchive**](ProductsApi.md#products_unarchive) | **POST** /v1/products/{id}/unarchive | Unarchive Product
[**products_update**](ProductsApi.md#products_update) | **PATCH** /v1/products/{id} | Update Product


# **products_archive**
> ProductsArchive200Response products_archive(id)

Archive Product

Archive a specific product to hide it from checkout pages and search results. Products are soft-deleted (archived) and can be restored using the unarchive endpoint.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.products_archive200_response import ProductsArchive200Response
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
    api_instance = solifyn.ProductsApi(api_client)
    id = 'prod_123' # str | The unique product ID to archive.

    try:
        # Archive Product
        api_response = api_instance.products_archive(id)
        print("The response of ProductsApi->products_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique product ID to archive. | 

### Return type

[**ProductsArchive200Response**](ProductsArchive200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product archived successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_create**
> Product products_create(product_create)

Create Product

Create a new product within your active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.product import Product
from solifyn.models.product_create import ProductCreate
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
    api_instance = solifyn.ProductsApi(api_client)
    product_create = solifyn.ProductCreate() # ProductCreate | 

    try:
        # Create Product
        api_response = api_instance.products_create(product_create)
        print("The response of ProductsApi->products_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_create** | [**ProductCreate**](ProductCreate.md)|  | 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Product created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get**
> Product products_get(id)

Retrieve Product

Retrieve details of a specific product using its ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.product import Product
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
    api_instance = solifyn.ProductsApi(api_client)
    id = 'prod_123' # str | The unique product ID.

    try:
        # Retrieve Product
        api_response = api_instance.products_get(id)
        print("The response of ProductsApi->products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique product ID. | 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved product details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_list**
> ProductsList200Response products_list(pricing_type=pricing_type, sorting=sorting, limit=limit, page=page, is_recurring=is_recurring, is_archived=is_archived, query=query, id=id)

List Products

List and query products belonging to your active business with support for fuzzy search, filters, pagination, and sorting.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.products_list200_response import ProductsList200Response
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
    api_instance = solifyn.ProductsApi(api_client)
    pricing_type = 'pricing_type_example' # str | Filter by pricing type. (optional)
    sorting = 'sorting_example' # str | Sorting criterion. Add a minus sign - before the criteria name to sort by descending order. (optional)
    limit = 10 # float | Size of a page, defaults to 10. Maximum is 100. (optional) (default to 10)
    page = 1 # float | Page number, defaults to 1. (optional) (default to 1)
    is_recurring = True # bool | Filter on recurring products (subscriptions). If true, only subscription tiers are returned. If false, only one-time purchase products are returned. (optional)
    is_archived = True # bool | Filter by archived status. (optional)
    query = 'query_example' # str | Filter by product name (fuzzy, case-insensitive). (optional)
    id = 'id_example' # str | Filter by product ID. (optional)

    try:
        # List Products
        api_response = api_instance.products_list(pricing_type=pricing_type, sorting=sorting, limit=limit, page=page, is_recurring=is_recurring, is_archived=is_archived, query=query, id=id)
        print("The response of ProductsApi->products_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pricing_type** | **str**| Filter by pricing type. | [optional] 
 **sorting** | **str**| Sorting criterion. Add a minus sign - before the criteria name to sort by descending order. | [optional] 
 **limit** | **float**| Size of a page, defaults to 10. Maximum is 100. | [optional] [default to 10]
 **page** | **float**| Page number, defaults to 1. | [optional] [default to 1]
 **is_recurring** | **bool**| Filter on recurring products (subscriptions). If true, only subscription tiers are returned. If false, only one-time purchase products are returned. | [optional] 
 **is_archived** | **bool**| Filter by archived status. | [optional] 
 **query** | **str**| Filter by product name (fuzzy, case-insensitive). | [optional] 
 **id** | **str**| Filter by product ID. | [optional] 

### Return type

[**ProductsList200Response**](ProductsList200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved products list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_unarchive**
> ProductsUnarchive200Response products_unarchive(id)

Unarchive Product

Restore an archived product back to active status, making it visible again.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.products_unarchive200_response import ProductsUnarchive200Response
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
    api_instance = solifyn.ProductsApi(api_client)
    id = 'prod_123' # str | The unique product ID to unarchive.

    try:
        # Unarchive Product
        api_response = api_instance.products_unarchive(id)
        print("The response of ProductsApi->products_unarchive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_unarchive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique product ID to unarchive. | 

### Return type

[**ProductsUnarchive200Response**](ProductsUnarchive200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product unarchived successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update**
> ProductMessageResponseDto products_update(id, product_update)

Update Product

Update details of an existing product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.product_message_response_dto import ProductMessageResponseDto
from solifyn.models.product_update import ProductUpdate
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
    api_instance = solifyn.ProductsApi(api_client)
    id = 'prod_123' # str | The unique product ID.
    product_update = solifyn.ProductUpdate() # ProductUpdate | 

    try:
        # Update Product
        api_response = api_instance.products_update(id, product_update)
        print("The response of ProductsApi->products_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique product ID. | 
 **product_update** | [**ProductUpdate**](ProductUpdate.md)|  | 

### Return type

[**ProductMessageResponseDto**](ProductMessageResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

