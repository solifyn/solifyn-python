# solifyn.PayoutsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payouts_create_withdrawal**](PayoutsApi.md#payouts_create_withdrawal) | **POST** /v1/payouts/withdrawals | Create Withdrawal
[**payouts_get_account**](PayoutsApi.md#payouts_get_account) | **GET** /v1/payouts/account | Retrieve Payout Account
[**payouts_get_account_link**](PayoutsApi.md#payouts_get_account_link) | **GET** /v1/payouts/account-link | Create Account Link
[**payouts_get_token**](PayoutsApi.md#payouts_get_token) | **GET** /v1/payouts/token | Generate Portal Access Token
[**payouts_get_withdrawals**](PayoutsApi.md#payouts_get_withdrawals) | **GET** /v1/payouts/withdrawals | Get Withdrawals List
[**payouts_list_methods**](PayoutsApi.md#payouts_list_methods) | **GET** /v1/payouts/methods | List Payout Methods
[**payouts_list_verifications**](PayoutsApi.md#payouts_list_verifications) | **GET** /v1/payouts/verifications | List Verifications
[**payouts_list_withdrawals**](PayoutsApi.md#payouts_list_withdrawals) | **GET** /v1/payouts | List Withdrawals


# **payouts_create_withdrawal**
> Withdrawal payouts_create_withdrawal(withdrawal_create)

Create Withdrawal

Initiate a balance withdrawal transfer request.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.withdrawal import Withdrawal
from solifyn.models.withdrawal_create import WithdrawalCreate
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
    api_instance = solifyn.PayoutsApi(api_client)
    withdrawal_create = solifyn.WithdrawalCreate() # WithdrawalCreate | 

    try:
        # Create Withdrawal
        api_response = api_instance.payouts_create_withdrawal(withdrawal_create)
        print("The response of PayoutsApi->payouts_create_withdrawal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_create_withdrawal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdrawal_create** | [**WithdrawalCreate**](WithdrawalCreate.md)|  | 

### Return type

[**Withdrawal**](Withdrawal.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Withdrawal successfully initiated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_get_account**
> PayoutAccount payouts_get_account()

Retrieve Payout Account

Retrieve general status and information of onboarding payout accounts.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.payout_account import PayoutAccount
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
    api_instance = solifyn.PayoutsApi(api_client)

    try:
        # Retrieve Payout Account
        api_response = api_instance.payouts_get_account()
        print("The response of PayoutsApi->payouts_get_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_get_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayoutAccount**](PayoutAccount.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout account details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_get_account_link**
> PayoutAccountLink payouts_get_account_link(use_case=use_case)

Create Account Link

Generate temporary links for onboarding or viewing portals.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.payout_account_link import PayoutAccountLink
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
    api_instance = solifyn.PayoutsApi(api_client)
    use_case = 'use_case_example' # str | Onboarding link type context (optional)

    try:
        # Create Account Link
        api_response = api_instance.payouts_get_account_link(use_case=use_case)
        print("The response of PayoutsApi->payouts_get_account_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_get_account_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **use_case** | **str**| Onboarding link type context | [optional] 

### Return type

[**PayoutAccountLink**](PayoutAccountLink.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account connection link generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_get_token**
> PayoutAccessToken payouts_get_token()

Generate Portal Access Token

Generate temporary credentials to access the embed portal.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.payout_access_token import PayoutAccessToken
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
    api_instance = solifyn.PayoutsApi(api_client)

    try:
        # Generate Portal Access Token
        api_response = api_instance.payouts_get_token()
        print("The response of PayoutsApi->payouts_get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_get_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PayoutAccessToken**](PayoutAccessToken.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Portal access token successfully generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_get_withdrawals**
> WithdrawalList payouts_get_withdrawals(limit=limit, page=page)

Get Withdrawals List

Retrieve withdrawal records for the active business.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.withdrawal_list import WithdrawalList
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
    api_instance = solifyn.PayoutsApi(api_client)
    limit = 3.4 # float | Page size limit (optional)
    page = 3.4 # float | Page number (optional)

    try:
        # Get Withdrawals List
        api_response = api_instance.payouts_get_withdrawals(limit=limit, page=page)
        print("The response of PayoutsApi->payouts_get_withdrawals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_get_withdrawals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Page size limit | [optional] 
 **page** | **float**| Page number | [optional] 

### Return type

[**WithdrawalList**](WithdrawalList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Withdrawals list retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_list_methods**
> PayoutMethodList payouts_list_methods(limit=limit, page=page)

List Payout Methods

List saved payout destinations (bank accounts, cards).

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.payout_method_list import PayoutMethodList
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
    api_instance = solifyn.PayoutsApi(api_client)
    limit = 3.4 # float |  (optional)
    page = 3.4 # float |  (optional)

    try:
        # List Payout Methods
        api_response = api_instance.payouts_list_methods(limit=limit, page=page)
        print("The response of PayoutsApi->payouts_list_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_list_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] 
 **page** | **float**|  | [optional] 

### Return type

[**PayoutMethodList**](PayoutMethodList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payout methods retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_list_verifications**
> PayoutVerificationList payouts_list_verifications(limit=limit, page=page)

List Verifications

Retrieve pending or completed KYC verification checks.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.payout_verification_list import PayoutVerificationList
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
    api_instance = solifyn.PayoutsApi(api_client)
    limit = 3.4 # float |  (optional)
    page = 3.4 # float |  (optional)

    try:
        # List Verifications
        api_response = api_instance.payouts_list_verifications(limit=limit, page=page)
        print("The response of PayoutsApi->payouts_list_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_list_verifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] 
 **page** | **float**|  | [optional] 

### Return type

[**PayoutVerificationList**](PayoutVerificationList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | KYC verifications list retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payouts_list_withdrawals**
> WithdrawalList payouts_list_withdrawals(limit=limit, page=page)

List Withdrawals

Retrieve a list of past withdrawal history.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.withdrawal_list import WithdrawalList
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
    api_instance = solifyn.PayoutsApi(api_client)
    limit = 3.4 # float | Page size limit (optional)
    page = 3.4 # float | Page number (optional)

    try:
        # List Withdrawals
        api_response = api_instance.payouts_list_withdrawals(limit=limit, page=page)
        print("The response of PayoutsApi->payouts_list_withdrawals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayoutsApi->payouts_list_withdrawals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Page size limit | [optional] 
 **page** | **float**| Page number | [optional] 

### Return type

[**WithdrawalList**](WithdrawalList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Withdrawals list retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

