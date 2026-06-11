# solifyn.FramerIntegrationApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**framer_create_template**](FramerIntegrationApi.md#framer_create_template) | **POST** /v1/framer/templates | Create Framer Template
[**framer_delete_template**](FramerIntegrationApi.md#framer_delete_template) | **DELETE** /v1/framer/templates/{id} | Delete Framer Template
[**framer_get_template**](FramerIntegrationApi.md#framer_get_template) | **GET** /v1/framer/templates/{id} | Retrieve Framer Template
[**framer_list_templates**](FramerIntegrationApi.md#framer_list_templates) | **GET** /v1/framer/templates | List Framer Templates
[**framer_update_template**](FramerIntegrationApi.md#framer_update_template) | **PUT** /v1/framer/templates/{id} | Update Framer Template


# **framer_create_template**
> FramerTemplateResponseDto framer_create_template(create_framer_template_dto)

Create Framer Template

Registers a new Framer template with its public remix link for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.create_framer_template_dto import CreateFramerTemplateDto
from solifyn.models.framer_template_response_dto import FramerTemplateResponseDto
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
    api_instance = solifyn.FramerIntegrationApi(api_client)
    create_framer_template_dto = solifyn.CreateFramerTemplateDto() # CreateFramerTemplateDto | 

    try:
        # Create Framer Template
        api_response = api_instance.framer_create_template(create_framer_template_dto)
        print("The response of FramerIntegrationApi->framer_create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FramerIntegrationApi->framer_create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_framer_template_dto** | [**CreateFramerTemplateDto**](CreateFramerTemplateDto.md)|  | 

### Return type

[**FramerTemplateResponseDto**](FramerTemplateResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Template created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **framer_delete_template**
> framer_delete_template(id)

Delete Framer Template

Deletes a registered Framer template for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
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
    api_instance = solifyn.FramerIntegrationApi(api_client)
    id = 'id_example' # str | The Framer template ID

    try:
        # Delete Framer Template
        api_instance.framer_delete_template(id)
    except Exception as e:
        print("Exception when calling FramerIntegrationApi->framer_delete_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Framer template ID | 

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
**204** | Template deleted successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **framer_get_template**
> FramerTemplateResponseDto framer_get_template(id)

Retrieve Framer Template

Retrieves details of a specific registered Framer template.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.framer_template_response_dto import FramerTemplateResponseDto
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
    api_instance = solifyn.FramerIntegrationApi(api_client)
    id = 'id_example' # str | The Framer template ID

    try:
        # Retrieve Framer Template
        api_response = api_instance.framer_get_template(id)
        print("The response of FramerIntegrationApi->framer_get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FramerIntegrationApi->framer_get_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Framer template ID | 

### Return type

[**FramerTemplateResponseDto**](FramerTemplateResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of the Framer template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **framer_list_templates**
> List[FramerTemplateResponseDto] framer_list_templates()

List Framer Templates

Retrieves all registered Framer templates for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.framer_template_response_dto import FramerTemplateResponseDto
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
    api_instance = solifyn.FramerIntegrationApi(api_client)

    try:
        # List Framer Templates
        api_response = api_instance.framer_list_templates()
        print("The response of FramerIntegrationApi->framer_list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FramerIntegrationApi->framer_list_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FramerTemplateResponseDto]**](FramerTemplateResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Framer templates. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **framer_update_template**
> FramerTemplateResponseDto framer_update_template(id, update_framer_template_dto)

Update Framer Template

Updates a registered Framer template for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.framer_template_response_dto import FramerTemplateResponseDto
from solifyn.models.update_framer_template_dto import UpdateFramerTemplateDto
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
    api_instance = solifyn.FramerIntegrationApi(api_client)
    id = 'id_example' # str | The Framer template ID
    update_framer_template_dto = solifyn.UpdateFramerTemplateDto() # UpdateFramerTemplateDto | 

    try:
        # Update Framer Template
        api_response = api_instance.framer_update_template(id, update_framer_template_dto)
        print("The response of FramerIntegrationApi->framer_update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FramerIntegrationApi->framer_update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Framer template ID | 
 **update_framer_template_dto** | [**UpdateFramerTemplateDto**](UpdateFramerTemplateDto.md)|  | 

### Return type

[**FramerTemplateResponseDto**](FramerTemplateResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Template updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

