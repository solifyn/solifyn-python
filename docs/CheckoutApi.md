# solifyn.CheckoutApi

All URIs are relative to *https://api.solifyn.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_create**](CheckoutApi.md#checkout_create) | **POST** /v1/checkout/create | Create Checkout Session
[**checkout_create_collection**](CheckoutApi.md#checkout_create_collection) | **POST** /v1/checkout/collection/create | Create Collection Checkout Session
[**checkout_create_setup**](CheckoutApi.md#checkout_create_setup) | **POST** /v1/checkout/setup-configuration | Create Setup Checkout Configuration
[**checkout_get_session**](CheckoutApi.md#checkout_get_session) | **GET** /v1/checkout/session/{id} | Get Checkout Session Details
[**checkout_price_preview**](CheckoutApi.md#checkout_price_preview) | **GET** /v1/checkout/price-preview | Get Converted Price Preview
[**checkout_supported_currencies**](CheckoutApi.md#checkout_supported_currencies) | **GET** /v1/checkout/supported-currencies | Get Supported Currencies


# **checkout_create**
> CheckoutResponseDto checkout_create(create_checkout_dto)

Create Checkout Session

Create a new payment configuration for a product. Returns redirect URLs pointing to the custom checkout layout.

### Example


```python
import solifyn
from solifyn.models.checkout_response_dto import CheckoutResponseDto
from solifyn.models.create_checkout_dto import CreateCheckoutDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)
    create_checkout_dto = solifyn.CreateCheckoutDto() # CreateCheckoutDto | 

    try:
        # Create Checkout Session
        api_response = api_instance.checkout_create(create_checkout_dto)
        print("The response of CheckoutApi->checkout_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_checkout_dto** | [**CreateCheckoutDto**](CreateCheckoutDto.md)|  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Checkout session configuration created successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_create_collection**
> CheckoutResponseDto checkout_create_collection(create_collection_checkout_dto)

Create Collection Checkout Session

Create a new payment configuration for a product bundle/collection.

### Example


```python
import solifyn
from solifyn.models.checkout_response_dto import CheckoutResponseDto
from solifyn.models.create_collection_checkout_dto import CreateCollectionCheckoutDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)
    create_collection_checkout_dto = solifyn.CreateCollectionCheckoutDto() # CreateCollectionCheckoutDto | 

    try:
        # Create Collection Checkout Session
        api_response = api_instance.checkout_create_collection(create_collection_checkout_dto)
        print("The response of CheckoutApi->checkout_create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collection_checkout_dto** | [**CreateCollectionCheckoutDto**](CreateCollectionCheckoutDto.md)|  | 

### Return type

[**CheckoutResponseDto**](CheckoutResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Collection checkout session created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_create_setup**
> checkout_create_setup(create_setup_checkout_dto)

Create Setup Checkout Configuration

Create a new checkout session in setup mode for collecting cards without immediate charge.

### Example


```python
import solifyn
from solifyn.models.create_setup_checkout_dto import CreateSetupCheckoutDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)
    create_setup_checkout_dto = solifyn.CreateSetupCheckoutDto() # CreateSetupCheckoutDto | 

    try:
        # Create Setup Checkout Configuration
        api_instance.checkout_create_setup(create_setup_checkout_dto)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_create_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_setup_checkout_dto** | [**CreateSetupCheckoutDto**](CreateSetupCheckoutDto.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Setup checkout configuration created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_get_session**
> CheckoutSessionDetailsDto checkout_get_session(id)

Get Checkout Session Details

Retrieve checkout details to mount the custom embedded checkout.

### Example


```python
import solifyn
from solifyn.models.checkout_session_details_dto import CheckoutSessionDetailsDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)
    id = 'ch_XXXXXXXXXXX' # str | Internal database checkout session ID

    try:
        # Get Checkout Session Details
        api_response = api_instance.checkout_get_session(id)
        print("The response of CheckoutApi->checkout_get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_get_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Internal database checkout session ID | 

### Return type

[**CheckoutSessionDetailsDto**](CheckoutSessionDetailsDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checkout session details resolved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_price_preview**
> PricePreviewResponseDto checkout_price_preview(product_id, addons, currency=currency, discount=discount, qty=qty, custom_price=custom_price)

Get Converted Price Preview

Pre-calculate target currencies, applied discounts, and PWYW values before mounting the checkout.

### Example


```python
import solifyn
from solifyn.models.price_preview_response_dto import PricePreviewResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)
    product_id = 'prod_z2o92kEl6cYYX' # str | Public product ID
    addons = 'addons_example' # str | 
    currency = 'vnd' # str | Target currency code (ISO) (optional)
    discount = '10' # str | Percentage discount rate (optional)
    qty = '1' # str | Number of product units (optional)
    custom_price = '15' # str | Override price for PWYW products (optional)

    try:
        # Get Converted Price Preview
        api_response = api_instance.checkout_price_preview(product_id, addons, currency=currency, discount=discount, qty=qty, custom_price=custom_price)
        print("The response of CheckoutApi->checkout_price_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_price_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Public product ID | 
 **addons** | **str**|  | 
 **currency** | **str**| Target currency code (ISO) | [optional] 
 **discount** | **str**| Percentage discount rate | [optional] 
 **qty** | **str**| Number of product units | [optional] 
 **custom_price** | **str**| Override price for PWYW products | [optional] 

### Return type

[**PricePreviewResponseDto**](PricePreviewResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Price preview calculations returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_supported_currencies**
> List[SupportedCurrenciesResponseDto] checkout_supported_currencies()

Get Supported Currencies

Retrieve all currencies supported for payouts and conversions.

### Example


```python
import solifyn
from solifyn.models.supported_currencies_response_dto import SupportedCurrenciesResponseDto
from solifyn.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.solifyn.com
# See configuration.py for a list of all supported configuration parameters.
configuration = solifyn.Configuration(
    host = "https://api.solifyn.com"
)


# Enter a context with an instance of the API client
with solifyn.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = solifyn.CheckoutApi(api_client)

    try:
        # Get Supported Currencies
        api_response = api_instance.checkout_supported_currencies()
        print("The response of CheckoutApi->checkout_supported_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutApi->checkout_supported_currencies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SupportedCurrenciesResponseDto]**](SupportedCurrenciesResponseDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported currencies resolved successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

