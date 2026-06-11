# solifyn.EntitlementGrantsApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entitlement_grants_get**](EntitlementGrantsApi.md#entitlement_grants_get) | **GET** /v1/entitlement-grants/{id} | Retrieve Entitlement Grant
[**entitlement_grants_list**](EntitlementGrantsApi.md#entitlement_grants_list) | **GET** /v1/entitlement-grants | List Entitlement Grants
[**entitlement_grants_retry**](EntitlementGrantsApi.md#entitlement_grants_retry) | **POST** /v1/entitlement-grants/{id}/retry | Retry Entitlement Grant Delivery
[**entitlement_grants_revoke**](EntitlementGrantsApi.md#entitlement_grants_revoke) | **POST** /v1/entitlement-grants/{id}/revoke | Manually Revoke Entitlement Grant


# **entitlement_grants_get**
> EntitlementGrantResponseDto entitlement_grants_get(id)

Retrieve Entitlement Grant

Retrieve details of a specific entitlement grant.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.entitlement_grant_response_dto import EntitlementGrantResponseDto
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
    api_instance = solifyn.EntitlementGrantsApi(api_client)
    id = 'id_example' # str | The unique grant ID

    try:
        # Retrieve Entitlement Grant
        api_response = api_instance.entitlement_grants_get(id)
        print("The response of EntitlementGrantsApi->entitlement_grants_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementGrantsApi->entitlement_grants_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique grant ID | 

### Return type

[**EntitlementGrantResponseDto**](EntitlementGrantResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the grant. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_grants_list**
> List[EntitlementGrantResponseDto] entitlement_grants_list(status=status, entitlement_id=entitlement_id, product_id=product_id)

List Entitlement Grants

Retrieve all GitHub repository entitlement grants for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.entitlement_grant_response_dto import EntitlementGrantResponseDto
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
    api_instance = solifyn.EntitlementGrantsApi(api_client)
    status = 'status_example' # str | Filter by status (PENDING, DELIVERED, FAILED, REVOKED) (optional)
    entitlement_id = 'entitlement_id_example' # str | Filter by entitlement config ID (optional)
    product_id = 'product_id_example' # str | Filter by product ID (optional)

    try:
        # List Entitlement Grants
        api_response = api_instance.entitlement_grants_list(status=status, entitlement_id=entitlement_id, product_id=product_id)
        print("The response of EntitlementGrantsApi->entitlement_grants_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementGrantsApi->entitlement_grants_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by status (PENDING, DELIVERED, FAILED, REVOKED) | [optional] 
 **entitlement_id** | **str**| Filter by entitlement config ID | [optional] 
 **product_id** | **str**| Filter by product ID | [optional] 

### Return type

[**List[EntitlementGrantResponseDto]**](EntitlementGrantResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved list of grants. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_grants_retry**
> EntitlementGrantResponseDto entitlement_grants_retry(id)

Retry Entitlement Grant Delivery

Attempts to re-invite the collaborator if GitHub username is already connected, or resets the OAuth URL redirect.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.entitlement_grant_response_dto import EntitlementGrantResponseDto
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
    api_instance = solifyn.EntitlementGrantsApi(api_client)
    id = 'id_example' # str | The unique grant ID

    try:
        # Retry Entitlement Grant Delivery
        api_response = api_instance.entitlement_grants_retry(id)
        print("The response of EntitlementGrantsApi->entitlement_grants_retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementGrantsApi->entitlement_grants_retry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique grant ID | 

### Return type

[**EntitlementGrantResponseDto**](EntitlementGrantResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Grant delivery retried. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlement_grants_revoke**
> EntitlementGrantResponseDto entitlement_grants_revoke(id)

Manually Revoke Entitlement Grant

Manually remove the customer collaborator access from the repository and revoke the grant.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.entitlement_grant_response_dto import EntitlementGrantResponseDto
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
    api_instance = solifyn.EntitlementGrantsApi(api_client)
    id = 'id_example' # str | The unique grant ID

    try:
        # Manually Revoke Entitlement Grant
        api_response = api_instance.entitlement_grants_revoke(id)
        print("The response of EntitlementGrantsApi->entitlement_grants_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntitlementGrantsApi->entitlement_grants_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique grant ID | 

### Return type

[**EntitlementGrantResponseDto**](EntitlementGrantResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Grant successfully revoked. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

