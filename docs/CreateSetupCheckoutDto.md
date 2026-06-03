# CreateSetupCheckoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **str** | The Whop/Stripe company ID context | 
**currency** | **str** | Currency for setup mode | [optional] [default to 'usd']
**retry_payment_id** | **str** | Internal or Whop failed payment ID to retry | [optional] 
**membership_id** | **str** | Membership ID to link setup checkout to for card updating | [optional] 
**plan_id** | **str** | Plan ID to retry or renew | [optional] 

## Example

```python
from solifyn.models.create_setup_checkout_dto import CreateSetupCheckoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSetupCheckoutDto from a JSON string
create_setup_checkout_dto_instance = CreateSetupCheckoutDto.from_json(json)
# print the JSON string representation of the object
print(CreateSetupCheckoutDto.to_json())

# convert the object into a dict
create_setup_checkout_dto_dict = create_setup_checkout_dto_instance.to_dict()
# create an instance of CreateSetupCheckoutDto from a dict
create_setup_checkout_dto_from_dict = CreateSetupCheckoutDto.from_dict(create_setup_checkout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


