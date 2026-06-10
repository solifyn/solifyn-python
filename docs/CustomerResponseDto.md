# CustomerResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The customer ID | 
**member_id** | **str** | The Membership ID associated with this customer | [optional] 
**email** | **str** | The email address of the customer | 
**name** | **str** | The name of the customer | [optional] 
**username** | **str** | The username of the customer | [optional] 
**phone** | **str** | The phone number of the customer | [optional] 
**phone_number** | **str** | The phone number of the customer | [optional] 
**metadata** | **object** | Additional metadata associated with the customer | [optional] 
**created_at** | **datetime** | Timestamp when the customer was created | 
**updated_at** | **datetime** | Timestamp when the customer was last updated | 
**business_id** | **str** | The business ID associated with the customer | 

## Example

```python
from solifyn.models.customer_response_dto import CustomerResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseDto from a JSON string
customer_response_dto_instance = CustomerResponseDto.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseDto.to_json())

# convert the object into a dict
customer_response_dto_dict = customer_response_dto_instance.to_dict()
# create an instance of CustomerResponseDto from a dict
customer_response_dto_from_dict = CustomerResponseDto.from_dict(customer_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


