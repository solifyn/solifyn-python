# solifyn.GitHubIntegrationApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**github_disconnect**](GitHubIntegrationApi.md#github_disconnect) | **POST** /v1/github/disconnect | Disconnect GitHub Integration
[**github_get_install_url**](GitHubIntegrationApi.md#github_get_install_url) | **GET** /v1/github/install | Get GitHub App Installation URL
[**github_list_repos**](GitHubIntegrationApi.md#github_list_repos) | **GET** /v1/github/repos | List Available GitHub Repositories


# **github_disconnect**
> github_disconnect()

Disconnect GitHub Integration

Disconnects the GitHub App integration by removing the installation ID from the business profile.

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
    api_instance = solifyn.GitHubIntegrationApi(api_client)

    try:
        # Disconnect GitHub Integration
        api_instance.github_disconnect()
    except Exception as e:
        print("Exception when calling GitHubIntegrationApi->github_disconnect: %s\n" % e)
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
**200** | Successfully disconnected. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **github_get_install_url**
> github_get_install_url(product_id=product_id)

Get GitHub App Installation URL

Generates the URL to install the system-wide GitHub App onto the merchant's GitHub account/org.

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
    api_instance = solifyn.GitHubIntegrationApi(api_client)
    product_id = 'product_id_example' # str | Optional Product ID to redirect back to after installation (optional)

    try:
        # Get GitHub App Installation URL
        api_instance.github_get_install_url(product_id=product_id)
    except Exception as e:
        print("Exception when calling GitHubIntegrationApi->github_get_install_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Optional Product ID to redirect back to after installation | [optional] 

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
**200** | Returns the generated installation URL. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **github_list_repos**
> List[GithubReposResponseDto] github_list_repos()

List Available GitHub Repositories

Retrieves all repositories accessible by the merchant's installed GitHub App.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.github_repos_response_dto import GithubReposResponseDto
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
    api_instance = solifyn.GitHubIntegrationApi(api_client)

    try:
        # List Available GitHub Repositories
        api_response = api_instance.github_list_repos()
        print("The response of GitHubIntegrationApi->github_list_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitHubIntegrationApi->github_list_repos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[GithubReposResponseDto]**](GithubReposResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of repositories. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

