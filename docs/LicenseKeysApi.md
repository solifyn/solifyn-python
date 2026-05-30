# solifyn.LicenseKeysApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_create**](LicenseKeysApi.md#licenses_create) | **POST** /v1/licenses | Create License Key
[**licenses_delete_instance**](LicenseKeysApi.md#licenses_delete_instance) | **DELETE** /v1/licenses/instances/{instanceId} | Force Delete Instance
[**licenses_get**](LicenseKeysApi.md#licenses_get) | **GET** /v1/licenses/{id} | Get License Key
[**licenses_get_instance**](LicenseKeysApi.md#licenses_get_instance) | **GET** /v1/licenses/{id}/instances/{instanceId} | Get License Key Instance
[**licenses_get_instances**](LicenseKeysApi.md#licenses_get_instances) | **GET** /v1/licenses/{id}/instances | Get License Key Instances
[**licenses_list**](LicenseKeysApi.md#licenses_list) | **GET** /v1/licenses | List License Keys
[**licenses_toggle**](LicenseKeysApi.md#licenses_toggle) | **POST** /v1/licenses/{id}/toggle | Toggle License Status
[**licenses_update**](LicenseKeysApi.md#licenses_update) | **PATCH** /v1/licenses/{id} | Update License Key
[**licenses_update_instance**](LicenseKeysApi.md#licenses_update_instance) | **PATCH** /v1/licenses/{id}/instances/{instanceId} | Update License Key Instance
[**licenses_update_instance_post**](LicenseKeysApi.md#licenses_update_instance_post) | **POST** /v1/licenses/{id}/instances/{instanceId} | Update License Key Instance (POST)


# **licenses_create**
> License licenses_create(licenses_create_request)

Create License Key

Manually issue a new license key for a specific product.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license import License
from solifyn.models.licenses_create_request import LicensesCreateRequest
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    licenses_create_request = solifyn.LicensesCreateRequest() # LicensesCreateRequest | 

    try:
        # Create License Key
        api_response = api_instance.licenses_create(licenses_create_request)
        print("The response of LicenseKeysApi->licenses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licenses_create_request** | [**LicensesCreateRequest**](LicensesCreateRequest.md)|  | 

### Return type

[**License**](License.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created license. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_delete_instance**
> Instance licenses_delete_instance(instance_id)

Force Delete Instance

Administrative endpoint to force-delete an instance globally by its database ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    instance_id = 'inc_123' # str | The unique hardware activation instance ID.

    try:
        # Force Delete Instance
        api_response = api_instance.licenses_delete_instance(instance_id)
        print("The response of LicenseKeysApi->licenses_delete_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_delete_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The unique hardware activation instance ID. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance deactivated/deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_get**
> License licenses_get(id)

Get License Key

Retrieve complete administrative details of a specific license key.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license import License
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    id = 'id_example' # str | The unique license key ID.

    try:
        # Get License Key
        api_response = api_instance.licenses_get(id)
        print("The response of LicenseKeysApi->licenses_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique license key ID. | 

### Return type

[**License**](License.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved license details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_get_instance**
> Instance licenses_get_instance(id, instance_id)

Get License Key Instance

Retrieve administrative details of a specific software license instance.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    id = 'id_example' # str | The unique administrative identifier (ID) of the parent license key.
    instance_id = 'inc_123' # str | The client-generated instance ID (hardware hash) or the internal database ID of the instance.

    try:
        # Get License Key Instance
        api_response = api_instance.licenses_get_instance(id, instance_id)
        print("The response of LicenseKeysApi->licenses_get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique administrative identifier (ID) of the parent license key. | 
 **instance_id** | **str**| The client-generated instance ID (hardware hash) or the internal database ID of the instance. | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved instance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_get_instances**
> List[Instance] licenses_get_instances(id)

Get License Key Instances

Retrieve all active devices/instances for a specific administrative license key.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    id = 'lic_123' # str | The unique administrative identifier (ID) of the parent license key.

    try:
        # Get License Key Instances
        api_response = api_instance.licenses_get_instances(id)
        print("The response of LicenseKeysApi->licenses_get_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_get_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique administrative identifier (ID) of the parent license key. | 

### Return type

[**List[Instance]**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved instances. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_list**
> List[License] licenses_list()

List License Keys

List all administrative license keys belonging to products under your active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license import License
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
    api_instance = solifyn.LicenseKeysApi(api_client)

    try:
        # List License Keys
        api_response = api_instance.licenses_list()
        print("The response of LicenseKeysApi->licenses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[License]**](License.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved licenses list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_toggle**
> License licenses_toggle(id)

Toggle License Status

Toggle the status of a specific license key between ACTIVE and DISABLED.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license import License
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    id = 'lic_123' # str | The unique license key ID.

    try:
        # Toggle License Status
        api_response = api_instance.licenses_toggle(id)
        print("The response of LicenseKeysApi->licenses_toggle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_toggle: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique license key ID. | 

### Return type

[**License**](License.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status toggled successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_update**
> License licenses_update(id, licenses_update_request)

Update License Key

Update limits or status of an existing license key.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license import License
from solifyn.models.licenses_update_request import LicensesUpdateRequest
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    id = 'id_example' # str | The unique license key ID.
    licenses_update_request = solifyn.LicensesUpdateRequest() # LicensesUpdateRequest | 

    try:
        # Update License Key
        api_response = api_instance.licenses_update(id, licenses_update_request)
        print("The response of LicenseKeysApi->licenses_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique license key ID. | 
 **licenses_update_request** | [**LicensesUpdateRequest**](LicensesUpdateRequest.md)|  | 

### Return type

[**License**](License.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated license. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_update_instance**
> Instance licenses_update_instance(instance_id, id, licenses_update_instance_post_request)

Update License Key Instance

Update administrative details (like friendly display name or custom IP) of an active license device instance.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
from solifyn.models.licenses_update_instance_post_request import LicensesUpdateInstancePostRequest
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    instance_id = 'inc_123' # str | The client-generated instance ID (hardware hash) or the internal database ID of the instance.
    id = 'id_example' # str | The unique administrative identifier (ID) of the parent license key.
    licenses_update_instance_post_request = solifyn.LicensesUpdateInstancePostRequest() # LicensesUpdateInstancePostRequest | 

    try:
        # Update License Key Instance
        api_response = api_instance.licenses_update_instance(instance_id, id, licenses_update_instance_post_request)
        print("The response of LicenseKeysApi->licenses_update_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_update_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The client-generated instance ID (hardware hash) or the internal database ID of the instance. | 
 **id** | **str**| The unique administrative identifier (ID) of the parent license key. | 
 **licenses_update_instance_post_request** | [**LicensesUpdateInstancePostRequest**](LicensesUpdateInstancePostRequest.md)|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated instance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_update_instance_post**
> Instance licenses_update_instance_post(instance_id, id, licenses_update_instance_post_request)

Update License Key Instance (POST)

Alternative POST endpoint to update administrative details (like friendly display name or custom IP) of an active license device instance.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
from solifyn.models.licenses_update_instance_post_request import LicensesUpdateInstancePostRequest
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
    api_instance = solifyn.LicenseKeysApi(api_client)
    instance_id = 'inc_123' # str | The client-generated instance ID (hardware hash) or the internal database ID of the instance.
    id = 'id_example' # str | The unique administrative identifier (ID) of the parent license key.
    licenses_update_instance_post_request = solifyn.LicensesUpdateInstancePostRequest() # LicensesUpdateInstancePostRequest | 

    try:
        # Update License Key Instance (POST)
        api_response = api_instance.licenses_update_instance_post(instance_id, id, licenses_update_instance_post_request)
        print("The response of LicenseKeysApi->licenses_update_instance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysApi->licenses_update_instance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The client-generated instance ID (hardware hash) or the internal database ID of the instance. | 
 **id** | **str**| The unique administrative identifier (ID) of the parent license key. | 
 **licenses_update_instance_post_request** | [**LicensesUpdateInstancePostRequest**](LicensesUpdateInstancePostRequest.md)|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated instance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

