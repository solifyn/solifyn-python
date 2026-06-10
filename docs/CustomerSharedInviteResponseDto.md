# CustomerSharedInviteResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The generated invite token | 
**expires_at** | **datetime** | The expiration timestamp of the token | 
**url** | **str** | The self-service shared portal URL | [optional] 

## Example

```python
from solifyn.models.customer_shared_invite_response_dto import CustomerSharedInviteResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSharedInviteResponseDto from a JSON string
customer_shared_invite_response_dto_instance = CustomerSharedInviteResponseDto.from_json(json)
# print the JSON string representation of the object
print(CustomerSharedInviteResponseDto.to_json())

# convert the object into a dict
customer_shared_invite_response_dto_dict = customer_shared_invite_response_dto_instance.to_dict()
# create an instance of CustomerSharedInviteResponseDto from a dict
customer_shared_invite_response_dto_from_dict = CustomerSharedInviteResponseDto.from_dict(customer_shared_invite_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


