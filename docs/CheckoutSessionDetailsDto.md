# CheckoutSessionDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Checkout session identifier | 
**price** | **float** | Total purchase amount | 
**currency** | **str** | ISO currency code of the purchase | 
**store_name** | **str** | Title or name of the merchant/store selling the item | 
**status** | **str** | Current status of the checkout session | 
**billing_address** | **object** | Customer billing address details | [optional] 
**custom_fields** | **object** | Custom fields collected during purchase | [optional] 
**session_id** | **str** | The payment partner session ID | [optional] 
**payment_id** | **str** | Database payment transaction ID | [optional] 
**checkout_url** | **str** | Checkout session redirect URL if loaded in link mode | [optional] 
**product** | [**Product**](Product.md) | The details of the product being purchased | [optional] 
**entitlement_grants** | **List[object]** | List of entitlement grants (e.g. GitHub repo invites) associated with this checkout. | [optional] 

## Example

```python
from solifyn.models.checkout_session_details_dto import CheckoutSessionDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionDetailsDto from a JSON string
checkout_session_details_dto_instance = CheckoutSessionDetailsDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionDetailsDto.to_json())

# convert the object into a dict
checkout_session_details_dto_dict = checkout_session_details_dto_instance.to_dict()
# create an instance of CheckoutSessionDetailsDto from a dict
checkout_session_details_dto_from_dict = CheckoutSessionDetailsDto.from_dict(checkout_session_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


