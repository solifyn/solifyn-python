# UpdateCheckoutLinkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The friendly display title of this checkout link | [optional] 
**product_id** | **str** | Product database/Whop ID to sell | [optional] 
**collection_id** | **str** | Optional collection database ID to sell | [optional] 
**customer_name** | **str** | Prefilled customer name for checkout inputs | [optional] 
**customer_email** | **str** | Prefilled customer email for checkout inputs | [optional] 
**address_line1** | **str** | Prefilled customer billing address line 1 | [optional] 
**city** | **str** | Prefilled customer billing city | [optional] 
**state** | **str** | Prefilled customer billing state | [optional] 
**postal_code** | **str** | Prefilled customer billing zip/postal code | [optional] 
**country** | **str** | Prefilled customer billing country (2-letter ISO) | [optional] 
**quantity** | **object** | Override quantity for checkout session | [optional] 
**redirect_url** | **str** | The absolute URL to redirect to upon successful payment completion | [optional] 
**cancel_url** | **str** | The absolute URL to redirect to if a customer cancels the payment | [optional] 
**show_discounts** | **bool** | Whether to display discount input form fields on checkout screen | [optional] [default to True]

## Example

```python
from solifyn.models.update_checkout_link_dto import UpdateCheckoutLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCheckoutLinkDto from a JSON string
update_checkout_link_dto_instance = UpdateCheckoutLinkDto.from_json(json)
# print the JSON string representation of the object
print(UpdateCheckoutLinkDto.to_json())

# convert the object into a dict
update_checkout_link_dto_dict = update_checkout_link_dto_instance.to_dict()
# create an instance of UpdateCheckoutLinkDto from a dict
update_checkout_link_dto_from_dict = UpdateCheckoutLinkDto.from_dict(update_checkout_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


