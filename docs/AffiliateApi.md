# solifyn.AffiliateApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**affiliate_controller_approve_connection**](AffiliateApi.md#affiliate_controller_approve_connection) | **POST** /v1/affiliate/program/connections/{id}/approve | 
[**affiliate_controller_archive_connection**](AffiliateApi.md#affiliate_controller_archive_connection) | **POST** /v1/affiliate/program/connections/{id}/archive | 
[**affiliate_controller_delete_override**](AffiliateApi.md#affiliate_controller_delete_override) | **DELETE** /v1/affiliate/program/override/{id} | 
[**affiliate_controller_get_earnings_connections**](AffiliateApi.md#affiliate_controller_get_earnings_connections) | **GET** /v1/affiliate/earnings/connections | 
[**affiliate_controller_get_earnings_ledger**](AffiliateApi.md#affiliate_controller_get_earnings_ledger) | **GET** /v1/affiliate/earnings/ledger | 
[**affiliate_controller_get_earnings_stats**](AffiliateApi.md#affiliate_controller_get_earnings_stats) | **GET** /v1/affiliate/earnings/stats | 
[**affiliate_controller_get_marketplace**](AffiliateApi.md#affiliate_controller_get_marketplace) | **GET** /v1/affiliate/marketplace | 
[**affiliate_controller_get_program_connections**](AffiliateApi.md#affiliate_controller_get_program_connections) | **GET** /v1/affiliate/program/connections | 
[**affiliate_controller_get_program_ledger**](AffiliateApi.md#affiliate_controller_get_program_ledger) | **GET** /v1/affiliate/program/ledger | 
[**affiliate_controller_get_program_settings**](AffiliateApi.md#affiliate_controller_get_program_settings) | **GET** /v1/affiliate/program/settings | 
[**affiliate_controller_join_program**](AffiliateApi.md#affiliate_controller_join_program) | **POST** /v1/affiliate/marketplace/join | 
[**affiliate_controller_reject_connection**](AffiliateApi.md#affiliate_controller_reject_connection) | **POST** /v1/affiliate/program/connections/{id}/reject | 
[**affiliate_controller_save_override**](AffiliateApi.md#affiliate_controller_save_override) | **POST** /v1/affiliate/program/override | 
[**affiliate_controller_save_program_settings**](AffiliateApi.md#affiliate_controller_save_program_settings) | **POST** /v1/affiliate/program/settings | 


# **affiliate_controller_approve_connection**
> affiliate_controller_approve_connection(id)



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.affiliate_controller_approve_connection(id)
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_approve_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_archive_connection**
> affiliate_controller_archive_connection(id)



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.affiliate_controller_archive_connection(id)
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_archive_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_delete_override**
> affiliate_controller_delete_override(id)



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.affiliate_controller_delete_override(id)
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_delete_override: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_earnings_connections**
> affiliate_controller_get_earnings_connections()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_earnings_connections()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_earnings_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_earnings_ledger**
> affiliate_controller_get_earnings_ledger()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_earnings_ledger()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_earnings_ledger: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_earnings_stats**
> affiliate_controller_get_earnings_stats()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_earnings_stats()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_earnings_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_marketplace**
> affiliate_controller_get_marketplace()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_marketplace()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_marketplace: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_program_connections**
> affiliate_controller_get_program_connections()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_program_connections()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_program_connections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_program_ledger**
> affiliate_controller_get_program_ledger()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_program_ledger()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_program_ledger: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_get_program_settings**
> affiliate_controller_get_program_settings()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_get_program_settings()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_get_program_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_join_program**
> affiliate_controller_join_program()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_join_program()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_join_program: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_reject_connection**
> affiliate_controller_reject_connection(id)



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.affiliate_controller_reject_connection(id)
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_reject_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_save_override**
> affiliate_controller_save_override()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_save_override()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_save_override: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **affiliate_controller_save_program_settings**
> affiliate_controller_save_program_settings()



### Example


```python
import solifyn
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.AffiliateApi(api_client)

    try:
        api_instance.affiliate_controller_save_program_settings()
    except Exception as e:
        print("Exception when calling AffiliateApi->affiliate_controller_save_program_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

