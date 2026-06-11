# solifyn.EntitlementsApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitlements_create**](EntitlementsApi.md#entitlements_create) | **POST** /v1/entitlements | Create Entitlement
[**entitlements_delete**](EntitlementsApi.md#entitlements_delete) | **DELETE** /v1/entitlements/{id} | Delete Entitlement
[**entitlements_get**](EntitlementsApi.md#entitlements_get) | **GET** /v1/entitlements/{id} | Retrieve Entitlement
[**entitlements_list**](EntitlementsApi.md#entitlements_list) | **GET** /v1/entitlements | List Entitlements
[**entitlements_update**](EntitlementsApi.md#entitlements_update) | **PATCH** /v1/entitlements/{id} | Update Entitlement


# **entitlements_create**
> EntitlementDetailResponseDto entitlements_create(create_entitlement_dto)

Create Entitlement

Create a new independent access entitlement.

### Example


```python
import solifyn
from solifyn.models.create_entitlement_dto import CreateEntitlementDto
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto
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
    api_instance = solifyn.EntitlementsApi(api_client)
    create_entitlement_dto = solifyn.CreateEntitlementDto() # CreateEntitlementDto | 

    try:
        # Create Entitlement
        api_response = api_instance.entitlements_create(create_entitlement_dto)
        print("The response of EntitlementsApi->entitlements_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_entitlement_dto** | [**CreateEntitlementDto**](CreateEntitlementDto.md)|  | 

### Return type

[**EntitlementDetailResponseDto**](EntitlementDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Entitlement created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_delete**
> EntitlementDetailResponseDto entitlements_delete(id)

Delete Entitlement

Delete an independent entitlement and unlink all mapped products.

### Example


```python
import solifyn
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto
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
    api_instance = solifyn.EntitlementsApi(api_client)
    id = 'ent_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique entitlement ID.

    try:
        # Delete Entitlement
        api_response = api_instance.entitlements_delete(id)
        print("The response of EntitlementsApi->entitlements_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique entitlement ID. | 

### Return type

[**EntitlementDetailResponseDto**](EntitlementDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entitlement deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_get**
> EntitlementDetailResponseDto entitlements_get(id)

Retrieve Entitlement

Retrieve a specific entitlement definition by ID.

### Example


```python
import solifyn
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto
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
    api_instance = solifyn.EntitlementsApi(api_client)
    id = 'ent_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique entitlement ID.

    try:
        # Retrieve Entitlement
        api_response = api_instance.entitlements_get(id)
        print("The response of EntitlementsApi->entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique entitlement ID. | 

### Return type

[**EntitlementDetailResponseDto**](EntitlementDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entitlement retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_list**
> List[EntitlementDetailResponseDto] entitlements_list()

List Entitlements

List all independent entitlements for the active business.

### Example


```python
import solifyn
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto
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
    api_instance = solifyn.EntitlementsApi(api_client)

    try:
        # List Entitlements
        api_response = api_instance.entitlements_list()
        print("The response of EntitlementsApi->entitlements_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EntitlementDetailResponseDto]**](EntitlementDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entitlements retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_update**
> EntitlementDetailResponseDto entitlements_update(id, update_entitlement_dto)

Update Entitlement

Update details of an existing independent entitlement.

### Example


```python
import solifyn
from solifyn.models.entitlement_detail_response_dto import EntitlementDetailResponseDto
from solifyn.models.update_entitlement_dto import UpdateEntitlementDto
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
    api_instance = solifyn.EntitlementsApi(api_client)
    id = 'ent_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique entitlement ID.
    update_entitlement_dto = solifyn.UpdateEntitlementDto() # UpdateEntitlementDto | 

    try:
        # Update Entitlement
        api_response = api_instance.entitlements_update(id, update_entitlement_dto)
        print("The response of EntitlementsApi->entitlements_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementsApi->entitlements_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique entitlement ID. | 
 **update_entitlement_dto** | [**UpdateEntitlementDto**](UpdateEntitlementDto.md)|  | 

### Return type

[**EntitlementDetailResponseDto**](EntitlementDetailResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entitlement updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

