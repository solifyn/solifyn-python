# solifyn.ProductAddOnsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_create_addon**](ProductAddOnsApi.md#products_create_addon) | **POST** /v1/products/{id}/addons | Create Product Add-on
[**products_delete_addon**](ProductAddOnsApi.md#products_delete_addon) | **DELETE** /v1/products/{id}/addons/{addonId} | Delete Product Add-on
[**products_get_addon**](ProductAddOnsApi.md#products_get_addon) | **GET** /v1/products/{id}/addons/{addonId} | Retrieve Product Add-on
[**products_list_addons**](ProductAddOnsApi.md#products_list_addons) | **GET** /v1/products/{id}/addons | List Product Add-ons
[**products_list_all_addons**](ProductAddOnsApi.md#products_list_all_addons) | **GET** /v1/products/all-addons/list | List All Add-ons
[**products_update_addon**](ProductAddOnsApi.md#products_update_addon) | **PATCH** /v1/products/{id}/addons/{addonId} | Update Product Add-on


# **products_create_addon**
> Addon products_create_addon(id, addon_create)

Create Product Add-on

Attach a new add-on configuration to a product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.addon import Addon
from solifyn.models.addon_create import AddonCreate
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
    api_instance = solifyn.ProductAddOnsApi(api_client)
    id = 'prod_parent_123' # str | The parent product ID.
    addon_create = solifyn.AddonCreate() # AddonCreate | 

    try:
        # Create Product Add-on
        api_response = api_instance.products_create_addon(id, addon_create)
        print("The response of ProductAddOnsApi->products_create_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_create_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The parent product ID. | 
 **addon_create** | [**AddonCreate**](AddonCreate.md)|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add-on attached successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_delete_addon**
> ProductMessageResponseDto products_delete_addon(id, addon_id)

Delete Product Add-on

Remove an add-on configuration from a product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.product_message_response_dto import ProductMessageResponseDto
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
    api_instance = solifyn.ProductAddOnsApi(api_client)
    id = 'prod_parent_123' # str | The parent product ID.
    addon_id = 'prod_addon_123' # str | The add-on product ID to remove.

    try:
        # Delete Product Add-on
        api_response = api_instance.products_delete_addon(id, addon_id)
        print("The response of ProductAddOnsApi->products_delete_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_delete_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The parent product ID. | 
 **addon_id** | **str**| The add-on product ID to remove. | 

### Return type

[**ProductMessageResponseDto**](ProductMessageResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add-on configuration removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get_addon**
> Addon products_get_addon(id, addon_id)

Retrieve Product Add-on

Retrieve a specific add-on configuration of a product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.addon import Addon
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
    api_instance = solifyn.ProductAddOnsApi(api_client)
    id = 'prod_parent_123' # str | The parent product ID.
    addon_id = 'prod_addon_123' # str | The add-on product ID.

    try:
        # Retrieve Product Add-on
        api_response = api_instance.products_get_addon(id, addon_id)
        print("The response of ProductAddOnsApi->products_get_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_get_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The parent product ID. | 
 **addon_id** | **str**| The add-on product ID. | 

### Return type

[**Addon**](Addon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved add-on configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_list_addons**
> List[Addon] products_list_addons(id)

List Product Add-ons

Retrieve all add-on configurations attached to a product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.addon import Addon
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
    api_instance = solifyn.ProductAddOnsApi(api_client)
    id = 'prod_parent_123' # str | The parent product ID.

    try:
        # List Product Add-ons
        api_response = api_instance.products_list_addons(id)
        print("The response of ProductAddOnsApi->products_list_addons:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_list_addons: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The parent product ID. | 

### Return type

[**List[Addon]**](Addon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product add-on configurations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_list_all_addons**
> products_list_all_addons()

List All Add-ons

Retrieve all configured add-on configurations for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
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
    api_instance = solifyn.ProductAddOnsApi(api_client)

    try:
        # List All Add-ons
        api_instance.products_list_all_addons()
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_list_all_addons: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of all addons. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_update_addon**
> Addon products_update_addon(id, addon_id, addon_update)

Update Product Add-on

Update an existing add-on configuration for a product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.addon import Addon
from solifyn.models.addon_update import AddonUpdate
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
    api_instance = solifyn.ProductAddOnsApi(api_client)
    id = 'prod_parent_123' # str | The parent product ID.
    addon_id = 'prod_addon_123' # str | The add-on product ID.
    addon_update = solifyn.AddonUpdate() # AddonUpdate | 

    try:
        # Update Product Add-on
        api_response = api_instance.products_update_addon(id, addon_id, addon_update)
        print("The response of ProductAddOnsApi->products_update_addon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductAddOnsApi->products_update_addon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The parent product ID. | 
 **addon_id** | **str**| The add-on product ID. | 
 **addon_update** | [**AddonUpdate**](AddonUpdate.md)|  | 

### Return type

[**Addon**](Addon.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add-on configuration updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

