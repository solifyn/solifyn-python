# CheckoutLinkResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The checkout link ID | 
**title** | **str** | The title of the checkout link | [optional] 
**product_id** | **str** | The linked Product ID | [optional] 
**collection_id** | **str** | The linked Collection ID | [optional] 
**customer_name** | **str** | Pre-filled customer name | [optional] 
**customer_email** | **str** | Pre-filled customer email | [optional] 
**address_line1** | **str** | Pre-filled address line 1 | [optional] 
**city** | **str** | Pre-filled city | [optional] 
**state** | **str** | Pre-filled state | [optional] 
**postal_code** | **str** | Pre-filled postal code | [optional] 
**country** | **str** | Pre-filled country | [optional] 
**quantity** | **float** | Quantity to purchase | 
**redirect_url** | **str** | URL to redirect to after successful payment | [optional] 
**cancel_url** | **str** | URL to redirect to if payment is cancelled | [optional] 
**show_discounts** | **bool** | Whether to show discounts on the checkout page | 
**created_at** | **datetime** | Timestamp when the link was created | 
**updated_at** | **datetime** | Timestamp when the link was last updated | 

## Example

```python
from solifyn.models.checkout_link_response_dto import CheckoutLinkResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutLinkResponseDto from a JSON string
checkout_link_response_dto_instance = CheckoutLinkResponseDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutLinkResponseDto.to_json())

# convert the object into a dict
checkout_link_response_dto_dict = checkout_link_response_dto_instance.to_dict()
# create an instance of CheckoutLinkResponseDto from a dict
checkout_link_response_dto_from_dict = CheckoutLinkResponseDto.from_dict(checkout_link_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


