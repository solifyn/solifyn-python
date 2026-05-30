# solifyn.LicenseKeysClientApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**licenses_activate**](LicenseKeysClientApi.md#licenses_activate) | **POST** /v1/licenses/activate | Activate License Key
[**licenses_deactivate**](LicenseKeysClientApi.md#licenses_deactivate) | **POST** /v1/licenses/deactivate/{instanceId} | Deactivate Instance
[**licenses_instances**](LicenseKeysClientApi.md#licenses_instances) | **GET** /v1/licenses/instances/{licenseId} | Get Active Instances
[**licenses_verify**](LicenseKeysClientApi.md#licenses_verify) | **POST** /v1/licenses/verify | Validate License Key


# **licenses_activate**
> Instance licenses_activate(licenses_activate_request)

Activate License Key

Register and activate a device or instance for a specific license key.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.instance import Instance
from solifyn.models.licenses_activate_request import LicensesActivateRequest
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
    api_instance = solifyn.LicenseKeysClientApi(api_client)
    licenses_activate_request = solifyn.LicensesActivateRequest() # LicensesActivateRequest | 

    try:
        # Activate License Key
        api_response = api_instance.licenses_activate(licenses_activate_request)
        print("The response of LicenseKeysClientApi->licenses_activate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysClientApi->licenses_activate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licenses_activate_request** | [**LicensesActivateRequest**](LicensesActivateRequest.md)|  | 

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
**200** | Activation successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_deactivate**
> LicensesDeactivate200Response licenses_deactivate(instance_id, licenses_deactivate_request)

Deactivate Instance

Deactivate or unregister an active device instance from a license key.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.licenses_deactivate200_response import LicensesDeactivate200Response
from solifyn.models.licenses_deactivate_request import LicensesDeactivateRequest
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
    api_instance = solifyn.LicenseKeysClientApi(api_client)
    instance_id = 'instance_id_example' # str | The unique device instance ID.
    licenses_deactivate_request = solifyn.LicensesDeactivateRequest() # LicensesDeactivateRequest | 

    try:
        # Deactivate Instance
        api_response = api_instance.licenses_deactivate(instance_id, licenses_deactivate_request)
        print("The response of LicenseKeysClientApi->licenses_deactivate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysClientApi->licenses_deactivate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| The unique device instance ID. | 
 **licenses_deactivate_request** | [**LicensesDeactivateRequest**](LicensesDeactivateRequest.md)|  | 

### Return type

[**LicensesDeactivate200Response**](LicensesDeactivate200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Instance deactivated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_instances**
> List[Instance] licenses_instances(license_id)

Get Active Instances

List all active devices or server instances linked to a specific license key.

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
    api_instance = solifyn.LicenseKeysClientApi(api_client)
    license_id = 'license_id_example' # str | The unique license key ID.

    try:
        # Get Active Instances
        api_response = api_instance.licenses_instances(license_id)
        print("The response of LicenseKeysClientApi->licenses_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysClientApi->licenses_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_id** | **str**| The unique license key ID. | 

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
**200** | Successfully retrieved active instances. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **licenses_verify**
> LicenseValidationResponse licenses_verify(licenses_verify_request)

Validate License Key

Verify if a software license key is valid, active, and has not exceeded its limits.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.license_validation_response import LicenseValidationResponse
from solifyn.models.licenses_verify_request import LicensesVerifyRequest
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
    api_instance = solifyn.LicenseKeysClientApi(api_client)
    licenses_verify_request = solifyn.LicensesVerifyRequest() # LicensesVerifyRequest | 

    try:
        # Validate License Key
        api_response = api_instance.licenses_verify(licenses_verify_request)
        print("The response of LicenseKeysClientApi->licenses_verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LicenseKeysClientApi->licenses_verify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licenses_verify_request** | [**LicensesVerifyRequest**](LicensesVerifyRequest.md)|  | 

### Return type

[**LicenseValidationResponse**](LicenseValidationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | License is valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

