# solifyn.DisputesApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disputes_generate_report**](DisputesApi.md#disputes_generate_report) | **GET** /v1/transactions/disputes/report | Generate Dispute CSV Report
[**disputes_get**](DisputesApi.md#disputes_get) | **GET** /v1/transactions/disputes/{id} | Retrieve Dispute
[**disputes_list**](DisputesApi.md#disputes_list) | **GET** /v1/transactions/disputes | List Disputes
[**disputes_submit_evidence**](DisputesApi.md#disputes_submit_evidence) | **POST** /v1/transactions/disputes/{id}/submit | Submit Dispute Evidence
[**disputes_update_evidence**](DisputesApi.md#disputes_update_evidence) | **PATCH** /v1/transactions/disputes/{id}/evidence | Update Dispute Evidence
[**disputes_upload_evidence_file**](DisputesApi.md#disputes_upload_evidence_file) | **POST** /v1/transactions/disputes/upload | Upload Evidence File


# **disputes_generate_report**
> disputes_generate_report(created_at_gte=created_at_gte, created_at_lte=created_at_lte, status=status)

Generate Dispute CSV Report

Generates a downloadable CSV report of disputes matching the filters.

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
    api_instance = solifyn.DisputesApi(api_client)
    created_at_gte = 'created_at_gte_example' # str | Filter disputes created after this ISO date-time string (optional)
    created_at_lte = 'created_at_lte_example' # str | Filter disputes created before this ISO date-time string (optional)
    status = 'status_example' # str | Filter disputes by status (optional)

    try:
        # Generate Dispute CSV Report
        api_instance.disputes_generate_report(created_at_gte=created_at_gte, created_at_lte=created_at_lte, status=status)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_generate_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_at_gte** | **str**| Filter disputes created after this ISO date-time string | [optional] 
 **created_at_lte** | **str**| Filter disputes created before this ISO date-time string | [optional] 
 **status** | **str**| Filter disputes by status | [optional] 

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
**200** | CSV report file contents generated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disputes_get**
> Dispute disputes_get(id)

Retrieve Dispute

Retrieve details of a specific dispute by ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.dispute import Dispute
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
    api_instance = solifyn.DisputesApi(api_client)
    id = 'dsp_123' # str | The dispute ID

    try:
        # Retrieve Dispute
        api_response = api_instance.disputes_get(id)
        print("The response of DisputesApi->disputes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The dispute ID | 

### Return type

[**Dispute**](Dispute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disputes_list**
> DisputeList disputes_list(page=page, limit=limit, status=status, type=type)

List Disputes

Retrieve disputes associated with the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.dispute_list import DisputeList
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
    api_instance = solifyn.DisputesApi(api_client)
    page = '1' # str | Page number for pagination (optional)
    limit = '10' # str | Page size limit for pagination (optional)
    status = 'status_example' # str | Filter disputes by status (optional)
    type = 'type_example' # str | Filter by type: dispute or alert (optional)

    try:
        # List Disputes
        api_response = api_instance.disputes_list(page=page, limit=limit, status=status, type=type)
        print("The response of DisputesApi->disputes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Page number for pagination | [optional] 
 **limit** | **str**| Page size limit for pagination | [optional] 
 **status** | **str**| Filter disputes by status | [optional] 
 **type** | **str**| Filter by type: dispute or alert | [optional] 

### Return type

[**DisputeList**](DisputeList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute list retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disputes_submit_evidence**
> Dispute disputes_submit_evidence(id)

Submit Dispute Evidence

Finalize and submit the uploaded evidence for review.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.dispute import Dispute
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
    api_instance = solifyn.DisputesApi(api_client)
    id = 'dsp_123' # str | The dispute ID

    try:
        # Submit Dispute Evidence
        api_response = api_instance.disputes_submit_evidence(id)
        print("The response of DisputesApi->disputes_submit_evidence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_submit_evidence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The dispute ID | 

### Return type

[**Dispute**](Dispute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute evidence successfully submitted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disputes_update_evidence**
> Dispute disputes_update_evidence(id, dispute_evidence_update)

Update Dispute Evidence

Upload and update evidence attachments for a dispute.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.dispute import Dispute
from solifyn.models.dispute_evidence_update import DisputeEvidenceUpdate
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
    api_instance = solifyn.DisputesApi(api_client)
    id = 'dsp_123' # str | The dispute ID
    dispute_evidence_update = solifyn.DisputeEvidenceUpdate() # DisputeEvidenceUpdate | 

    try:
        # Update Dispute Evidence
        api_response = api_instance.disputes_update_evidence(id, dispute_evidence_update)
        print("The response of DisputesApi->disputes_update_evidence:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_update_evidence: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The dispute ID | 
 **dispute_evidence_update** | [**DisputeEvidenceUpdate**](DisputeEvidenceUpdate.md)|  | 

### Return type

[**Dispute**](Dispute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dispute evidence successfully updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disputes_upload_evidence_file**
> DisputeFileUpload disputes_upload_evidence_file(file)

Upload Evidence File

Upload a support file (image, PDF, video) to use as dispute evidence.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.dispute_file_upload import DisputeFileUpload
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
    api_instance = solifyn.DisputesApi(api_client)
    file = None # bytearray | The evidence file to upload (Max 25MB: JPEG, PNG, GIF, WEBP, PDF, MP4, WEBM, QuickTime)

    try:
        # Upload Evidence File
        api_response = api_instance.disputes_upload_evidence_file(file)
        print("The response of DisputesApi->disputes_upload_evidence_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DisputesApi->disputes_upload_evidence_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| The evidence file to upload (Max 25MB: JPEG, PNG, GIF, WEBP, PDF, MP4, WEBM, QuickTime) | 

### Return type

[**DisputeFileUpload**](DisputeFileUpload.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | File upload details successfully created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

