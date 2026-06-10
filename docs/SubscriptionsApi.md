# solifyn.SubscriptionsApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_action**](SubscriptionsApi.md#subscriptions_action) | **POST** /v1/subscriptions/{subscriptionId}/{action} | Subscription Action
[**subscriptions_get**](SubscriptionsApi.md#subscriptions_get) | **GET** /v1/subscriptions/{id} | Retrieve Subscription Details
[**subscriptions_list**](SubscriptionsApi.md#subscriptions_list) | **GET** /v1/subscriptions | List Subscriptions


# **subscriptions_action**
> SubscriptionsAction201Response subscriptions_action(subscription_id, action, subscription_action)

Subscription Action

Cancel, pause, resume, or add free days to a customer subscription.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.subscription_action import SubscriptionAction
from solifyn.models.subscriptions_action201_response import SubscriptionsAction201Response
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
    api_instance = solifyn.SubscriptionsApi(api_client)
    subscription_id = 'mem_123' # str | The customer subscription ID
    action = 'action_example' # str | The subscription task to execute
    subscription_action = solifyn.SubscriptionAction() # SubscriptionAction | 

    try:
        # Subscription Action
        api_response = api_instance.subscriptions_action(subscription_id, action, subscription_action)
        print("The response of SubscriptionsApi->subscriptions_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The customer subscription ID | 
 **action** | **str**| The subscription task to execute | 
 **subscription_action** | [**SubscriptionAction**](SubscriptionAction.md)|  | 

### Return type

[**SubscriptionsAction201Response**](SubscriptionsAction201Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscription action processed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_get**
> SubscriptionDetail subscriptions_get(id)

Retrieve Subscription Details

Retrieve detailed information about a subscription and its billing history.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.subscription_detail import SubscriptionDetail
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
    api_instance = solifyn.SubscriptionsApi(api_client)
    id = 'mem_123' # str | The customer subscription ID

    try:
        # Retrieve Subscription Details
        api_response = api_instance.subscriptions_get(id)
        print("The response of SubscriptionsApi->subscriptions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The customer subscription ID | 

### Return type

[**SubscriptionDetail**](SubscriptionDetail.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscription details retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_list**
> SubscriptionList subscriptions_list(customer_id=customer_id)

List Subscriptions

Retrieve a list of customer subscriptions, optionally filtered by customer ID.

### Example

* Bearer (API Key) Authentication (ApiKeyAuth):

```python
import solifyn
from solifyn.models.subscription_list import SubscriptionList
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
    api_instance = solifyn.SubscriptionsApi(api_client)
    customer_id = 'customer_id_example' # str | Filter subscriptions by customer ID. (optional)

    try:
        # List Subscriptions
        api_response = api_instance.subscriptions_list(customer_id=customer_id)
        print("The response of SubscriptionsApi->subscriptions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->subscriptions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Filter subscriptions by customer ID. | [optional] 

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscriptions retrieved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

