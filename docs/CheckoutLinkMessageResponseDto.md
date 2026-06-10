# CheckoutLinkMessageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.checkout_link_message_response_dto import CheckoutLinkMessageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutLinkMessageResponseDto from a JSON string
checkout_link_message_response_dto_instance = CheckoutLinkMessageResponseDto.from_json(json)
# print the JSON string representation of the object
print(CheckoutLinkMessageResponseDto.to_json())

# convert the object into a dict
checkout_link_message_response_dto_dict = checkout_link_message_response_dto_instance.to_dict()
# create an instance of CheckoutLinkMessageResponseDto from a dict
checkout_link_message_response_dto_from_dict = CheckoutLinkMessageResponseDto.from_dict(checkout_link_message_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


