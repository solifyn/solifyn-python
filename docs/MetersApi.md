# solifyn.MetersApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_ingest**](MetersApi.md#events_ingest) | **POST** /v1/meters/ingest | Ingest Events
[**meters_create**](MetersApi.md#meters_create) | **POST** /v1/meters | Create Meter
[**meters_get**](MetersApi.md#meters_get) | **GET** /v1/meters/{id} | Retrieve Meter
[**meters_get_events**](MetersApi.md#meters_get_events) | **GET** /v1/meters/{id}/events | List Meter Events
[**meters_get_quantities**](MetersApi.md#meters_get_quantities) | **GET** /v1/meters/{id}/quantities | Get Meter Quantities
[**meters_list**](MetersApi.md#meters_list) | **GET** /v1/meters | List Meters
[**meters_update**](MetersApi.md#meters_update) | **PATCH** /v1/meters/{id} | Update Meter


# **events_ingest**
> MeterIngestResponseDto events_ingest(meter_ingest_request_dto)

Ingest Events

Ingest usage events for meters.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_ingest_request_dto import MeterIngestRequestDto
from solifyn.models.meter_ingest_response_dto import MeterIngestResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    meter_ingest_request_dto = solifyn.MeterIngestRequestDto() # MeterIngestRequestDto | 

    try:
        # Ingest Events
        api_response = api_instance.events_ingest(meter_ingest_request_dto)
        print("The response of MetersApi->events_ingest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->events_ingest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meter_ingest_request_dto** | [**MeterIngestRequestDto**](MeterIngestRequestDto.md)|  | 

### Return type

[**MeterIngestResponseDto**](MeterIngestResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Events ingested successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_create**
> MeterResponseDto meters_create(create_meter_dto)

Create Meter

Create a new usage meter for event-based billing and usage tracking.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.create_meter_dto import CreateMeterDto
from solifyn.models.meter_response_dto import MeterResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    create_meter_dto = solifyn.CreateMeterDto() # CreateMeterDto | 

    try:
        # Create Meter
        api_response = api_instance.meters_create(create_meter_dto)
        print("The response of MetersApi->meters_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_meter_dto** | [**CreateMeterDto**](CreateMeterDto.md)|  | 

### Return type

[**MeterResponseDto**](MeterResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Meter created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_get**
> MeterDetailResponseDto meters_get(id, start_date, end_date)

Retrieve Meter

Retrieve a meter and its most recent usage events.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_detail_response_dto import MeterDetailResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    id = 'mtr_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique meter ID.
    start_date = 'start_date_example' # str | 
    end_date = 'end_date_example' # str | 

    try:
        # Retrieve Meter
        api_response = api_instance.meters_get(id, start_date, end_date)
        print("The response of MetersApi->meters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique meter ID. | 
 **start_date** | **str**|  | 
 **end_date** | **str**|  | 

### Return type

[**MeterDetailResponseDto**](MeterDetailResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meter retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_get_events**
> MeterEventsResponseDto meters_get_events(id, limit=limit)

List Meter Events

List recent usage events recorded for a meter.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_events_response_dto import MeterEventsResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    id = 'mtr_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique meter ID.
    limit = 100 # float | Maximum number of usage events to return. (optional) (default to 100)

    try:
        # List Meter Events
        api_response = api_instance.meters_get_events(id, limit=limit)
        print("The response of MetersApi->meters_get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_get_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique meter ID. | 
 **limit** | **float**| Maximum number of usage events to return. | [optional] [default to 100]

### Return type

[**MeterEventsResponseDto**](MeterEventsResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meter events retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_get_quantities**
> MeterQuantitiesResponseDto meters_get_quantities(id, start_date=start_date, end_date=end_date)

Get Meter Quantities

Get aggregated usage quantities for a meter within an optional date range.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_quantities_response_dto import MeterQuantitiesResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    id = 'mtr_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique meter ID.
    start_date = 'start_date_example' # str | Inclusive start date in ISO 8601 format. (optional)
    end_date = 'end_date_example' # str | Inclusive end date in ISO 8601 format. (optional)

    try:
        # Get Meter Quantities
        api_response = api_instance.meters_get_quantities(id, start_date=start_date, end_date=end_date)
        print("The response of MetersApi->meters_get_quantities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_get_quantities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique meter ID. | 
 **start_date** | **str**| Inclusive start date in ISO 8601 format. | [optional] 
 **end_date** | **str**| Inclusive end date in ISO 8601 format. | [optional] 

### Return type

[**MeterQuantitiesResponseDto**](MeterQuantitiesResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meter quantities retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_list**
> List[MeterResponseDto] meters_list(status=status)

List Meters

List meters belonging to your active business. You can filter by archived status.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_response_dto import MeterResponseDto
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
    api_instance = solifyn.MetersApi(api_client)
    status = 'status_example' # str | Filter by meter status. (optional)

    try:
        # List Meters
        api_response = api_instance.meters_list(status=status)
        print("The response of MetersApi->meters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter by meter status. | [optional] 

### Return type

[**List[MeterResponseDto]**](MeterResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meters retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meters_update**
> MeterResponseDto meters_update(id, update_meter_dto)

Update Meter

Update an existing meter definition.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.meter_response_dto import MeterResponseDto
from solifyn.models.update_meter_dto import UpdateMeterDto
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
    api_instance = solifyn.MetersApi(api_client)
    id = 'mtr_8Z1aB2cD3eF4gH5iJ6kL7m' # str | The unique meter ID.
    update_meter_dto = solifyn.UpdateMeterDto() # UpdateMeterDto | 

    try:
        # Update Meter
        api_response = api_instance.meters_update(id, update_meter_dto)
        print("The response of MetersApi->meters_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetersApi->meters_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique meter ID. | 
 **update_meter_dto** | [**UpdateMeterDto**](UpdateMeterDto.md)|  | 

### Return type

[**MeterResponseDto**](MeterResponseDto.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Meter updated successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

