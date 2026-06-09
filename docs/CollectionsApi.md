# solifyn.CollectionsApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_add_products**](CollectionsApi.md#collections_add_products) | **POST** /v1/collections/{id}/products | Add Products to Collection
[**collections_archive**](CollectionsApi.md#collections_archive) | **DELETE** /v1/collections/{id} | Archive Collection
[**collections_create**](CollectionsApi.md#collections_create) | **POST** /v1/collections | Create Collection
[**collections_delete_product**](CollectionsApi.md#collections_delete_product) | **DELETE** /v1/collections/{id}/products/{productId} | Remove Product from Collection
[**collections_get**](CollectionsApi.md#collections_get) | **GET** /v1/collections/{id} | Retrieve Collection
[**collections_list**](CollectionsApi.md#collections_list) | **GET** /v1/collections | List Collections
[**collections_list_archived**](CollectionsApi.md#collections_list_archived) | **GET** /v1/collections/archived | List Archived Collections
[**collections_unarchive**](CollectionsApi.md#collections_unarchive) | **POST** /v1/collections/{id}/unarchive | Unarchive Collection
[**collections_update**](CollectionsApi.md#collections_update) | **PATCH** /v1/collections/{id} | Update Collection
[**collections_update_product**](CollectionsApi.md#collections_update_product) | **PATCH** /v1/collections/{id}/products/{productId} | Update Collection Product


# **collections_add_products**
> CollectionResponseDto collections_add_products(id, add_collection_products_dto)

Add Products to Collection

Add one or more products to a collection. If a product already exists, its quantity is updated.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.add_collection_products_dto import AddCollectionProductsDto
from solifyn.models.collection_response_dto import CollectionResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID
    add_collection_products_dto = solifyn.AddCollectionProductsDto() # AddCollectionProductsDto | 

    try:
        # Add Products to Collection
        api_response = api_instance.collections_add_products(id, add_collection_products_dto)
        print("The response of CollectionsApi->collections_add_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_add_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **add_collection_products_dto** | [**AddCollectionProductsDto**](AddCollectionProductsDto.md)|  | 

### Return type

[**CollectionResponseDto**](CollectionResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products added/updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_archive**
> CollectionArchivedResponseDto collections_archive(id)

Archive Collection

Deactivate and move a collection to archives.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_archived_response_dto import CollectionArchivedResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID

    try:
        # Archive Collection
        api_response = api_instance.collections_archive(id)
        print("The response of CollectionsApi->collections_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**CollectionArchivedResponseDto**](CollectionArchivedResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection archived successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_create**
> CollectionResponseDto collections_create(create_collection_dto)

Create Collection

Generate a new product collection for checkout packaging.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_response_dto import CollectionResponseDto
from solifyn.models.create_collection_dto import CreateCollectionDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    create_collection_dto = solifyn.CreateCollectionDto() # CreateCollectionDto | 

    try:
        # Create Collection
        api_response = api_instance.collections_create(create_collection_dto)
        print("The response of CollectionsApi->collections_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_dto** | [**CreateCollectionDto**](CreateCollectionDto.md)|  | 

### Return type

[**CollectionResponseDto**](CollectionResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Collection created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_delete_product**
> CollectionProductDeletedResponseDto collections_delete_product(id, product_id)

Remove Product from Collection

Remove a product from a collection.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_product_deleted_response_dto import CollectionProductDeletedResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID
    product_id = 'prod_123' # str | Product ID

    try:
        # Remove Product from Collection
        api_response = api_instance.collections_delete_product(id, product_id)
        print("The response of CollectionsApi->collections_delete_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_delete_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **product_id** | **str**| Product ID | 

### Return type

[**CollectionProductDeletedResponseDto**](CollectionProductDeletedResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product removed from collection successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get**
> CollectionDetailResponseDto collections_get(id)

Retrieve Collection

Get properties of a product collection by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_detail_response_dto import CollectionDetailResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID

    try:
        # Retrieve Collection
        api_response = api_instance.collections_get(id)
        print("The response of CollectionsApi->collections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**CollectionDetailResponseDto**](CollectionDetailResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_list**
> List[CollectionResponseDto] collections_list()

List Collections

Get all active product collections linked to the current active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_response_dto import CollectionResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)

    try:
        # List Collections
        api_response = api_instance.collections_list()
        print("The response of CollectionsApi->collections_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionResponseDto]**](CollectionResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collections retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_list_archived**
> List[CollectionResponseDto] collections_list_archived()

List Archived Collections

Get all archived/deactivated product collections.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_response_dto import CollectionResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)

    try:
        # List Archived Collections
        api_response = api_instance.collections_list_archived()
        print("The response of CollectionsApi->collections_list_archived:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_list_archived: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionResponseDto]**](CollectionResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Archived collections list retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_unarchive**
> CollectionUnarchivedResponseDto collections_unarchive(id)

Unarchive Collection

Restore an archived collection back to active status.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_unarchived_response_dto import CollectionUnarchivedResponseDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID

    try:
        # Unarchive Collection
        api_response = api_instance.collections_unarchive(id)
        print("The response of CollectionsApi->collections_unarchive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_unarchive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 

### Return type

[**CollectionUnarchivedResponseDto**](CollectionUnarchivedResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Collection unarchived successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_update**
> CollectionUpdatedResponseDto collections_update(id, update_collection_dto)

Update Collection

Update products, friendly name, status, or description of a collection.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_updated_response_dto import CollectionUpdatedResponseDto
from solifyn.models.update_collection_dto import UpdateCollectionDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID
    update_collection_dto = solifyn.UpdateCollectionDto() # UpdateCollectionDto | 

    try:
        # Update Collection
        api_response = api_instance.collections_update(id, update_collection_dto)
        print("The response of CollectionsApi->collections_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **update_collection_dto** | [**UpdateCollectionDto**](UpdateCollectionDto.md)|  | 

### Return type

[**CollectionUpdatedResponseDto**](CollectionUpdatedResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_update_product**
> CollectionProductUpdatedResponseDto collections_update_product(id, product_id, update_collection_product_dto)

Update Collection Product

Update quantity of a specific product inside a collection.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.collection_product_updated_response_dto import CollectionProductUpdatedResponseDto
from solifyn.models.update_collection_product_dto import UpdateCollectionProductDto
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
    api_instance = solifyn.CollectionsApi(api_client)
    id = 'col_123' # str | Collection ID
    product_id = 'prod_123' # str | Product ID
    update_collection_product_dto = solifyn.UpdateCollectionProductDto() # UpdateCollectionProductDto | 

    try:
        # Update Collection Product
        api_response = api_instance.collections_update_product(id, product_id, update_collection_product_dto)
        print("The response of CollectionsApi->collections_update_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_update_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Collection ID | 
 **product_id** | **str**| Product ID | 
 **update_collection_product_dto** | [**UpdateCollectionProductDto**](UpdateCollectionProductDto.md)|  | 

### Return type

[**CollectionProductUpdatedResponseDto**](CollectionProductUpdatedResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection product quantity updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

