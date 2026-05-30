# CustomerMessageResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Response message indicating the outcome of the action. | 

## Example

```python
from solifyn.models.customer_message_response_dto import CustomerMessageResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerMessageResponseDto from a JSON string
customer_message_response_dto_instance = CustomerMessageResponseDto.from_json(json)
# print the JSON string representation of the object
print(CustomerMessageResponseDto.to_json())

# convert the object into a dict
customer_message_response_dto_dict = customer_message_response_dto_instance.to_dict()
# create an instance of CustomerMessageResponseDto from a dict
customer_message_response_dto_from_dict = CustomerMessageResponseDto.from_dict(customer_message_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


