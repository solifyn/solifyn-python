# ProductMessageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.product_message_response_dto import ProductMessageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductMessageResponseDto from a JSON string
product_message_response_dto_instance = ProductMessageResponseDto.from_json(json)
# print the JSON string representation of the object
print(ProductMessageResponseDto.to_json())

# convert the object into a dict
product_message_response_dto_dict = product_message_response_dto_instance.to_dict()
# create an instance of ProductMessageResponseDto from a dict
product_message_response_dto_from_dict = ProductMessageResponseDto.from_dict(product_message_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


