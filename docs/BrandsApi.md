# solifyn.BrandsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**brands_create**](BrandsApi.md#brands_create) | **POST** /v1/user/brand | Create Brand
[**brands_get**](BrandsApi.md#brands_get) | **GET** /v1/user/brand/{id} | Retrieve Brand
[**brands_list**](BrandsApi.md#brands_list) | **GET** /v1/user/brands | List Brands
[**brands_update**](BrandsApi.md#brands_update) | **PATCH** /v1/user/brand/{id} | Update Brand


# **brands_create**
> Brand brands_create(brand_create)

Create Brand

Add a new brand identity under the current active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.brand import Brand
from solifyn.models.brand_create import BrandCreate
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
    api_instance = solifyn.BrandsApi(api_client)
    brand_create = solifyn.BrandCreate() # BrandCreate | 

    try:
        # Create Brand
        api_response = api_instance.brands_create(brand_create)
        print("The response of BrandsApi->brands_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->brands_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_create** | [**BrandCreate**](BrandCreate.md)|  | 

### Return type

[**Brand**](Brand.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Brand successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **brands_get**
> Brand brands_get(id)

Retrieve Brand

Retrieve details of a brand identity by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.brand import Brand
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
    api_instance = solifyn.BrandsApi(api_client)
    id = 'brd_123' # str | The brand ID to retrieve

    try:
        # Retrieve Brand
        api_response = api_instance.brands_get(id)
        print("The response of BrandsApi->brands_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->brands_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The brand ID to retrieve | 

### Return type

[**Brand**](Brand.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Brand details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **brands_list**
> List[Brand] brands_list()

List Brands

Retrieve all brands associated with the current business context.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.brand import Brand
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
    api_instance = solifyn.BrandsApi(api_client)

    try:
        # List Brands
        api_response = api_instance.brands_list()
        print("The response of BrandsApi->brands_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->brands_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Brand]**](Brand.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of brands successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **brands_update**
> Brand brands_update(id, brand_update)

Update Brand

Update website, logo, description, or statement descriptors of a brand.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.brand import Brand
from solifyn.models.brand_update import BrandUpdate
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
    api_instance = solifyn.BrandsApi(api_client)
    id = 'brd_123' # str | The brand ID to update
    brand_update = solifyn.BrandUpdate() # BrandUpdate | 

    try:
        # Update Brand
        api_response = api_instance.brands_update(id, brand_update)
        print("The response of BrandsApi->brands_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandsApi->brands_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The brand ID to update | 
 **brand_update** | [**BrandUpdate**](BrandUpdate.md)|  | 

### Return type

[**Brand**](Brand.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Brand settings updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

