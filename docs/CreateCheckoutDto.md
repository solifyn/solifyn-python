# CreateCheckoutDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The public product identifier (product ID) | 
**currency** | **str** | Three-letter ISO currency code (lowercase) | [optional] 
**quantity** | **float** | The quantity of items to buy | [optional] [default to 1]
**discount_code** | **str** | Discount code to apply | [optional] 
**custom_price** | **float** | Custom price paid by customer (for Pay What You Want products) | [optional] 
**customer_email** | **str** | Email address of the customer | [optional] 
**checkout_data** | **object** | JSON metadata or checkout custom information | [optional] 
**custom_fields** | **object** | Custom text fields required for the purchase | [optional] 
**aff** | **str** | Affiliate partner tracking code | [optional] 
**checkout_id** | **str** | The existing checkout database ID to validate / update | [optional] 

## Example

```python
from solifyn.models.create_checkout_dto import CreateCheckoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutDto from a JSON string
create_checkout_dto_instance = CreateCheckoutDto.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutDto.to_json())

# convert the object into a dict
create_checkout_dto_dict = create_checkout_dto_instance.to_dict()
# create an instance of CreateCheckoutDto from a dict
create_checkout_dto_from_dict = CreateCheckoutDto.from_dict(create_checkout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


