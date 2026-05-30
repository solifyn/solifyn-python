# CheckoutResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the checkout session in database | 
**session_id** | **str** | The unique session ID format for external clients | 
**checkout_url** | **str** | The public redirect URL to the custom payment steps page | 

## Example

```python
from solifyn.models.checkout_response_dto import CheckoutResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutResponseDto from a JSON string
checkout_response_dto_instance = CheckoutResponseDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutResponseDto.to_json())

# convert the object into a dict
checkout_response_dto_dict = checkout_response_dto_instance.to_dict()
# create an instance of CheckoutResponseDto from a dict
checkout_response_dto_from_dict = CheckoutResponseDto.from_dict(checkout_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


