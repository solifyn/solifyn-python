# CreateCustomerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The unique email of the customer | 
**name** | **str** | The customer friendly full name | 
**phone** | **str** | The customer telephone/phone number | [optional] 
**username** | **str** | The username of the customer (e.g. Discord, Whop) | [optional] 
**metadata** | **object** | Custom key-value metadata associated with the customer | [optional] 

## Example

```python
from solifyn.models.create_customer_dto import CreateCustomerDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerDto from a JSON string
create_customer_dto_instance = CreateCustomerDto.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerDto.to_json())

# convert the object into a dict
create_customer_dto_dict = create_customer_dto_instance.to_dict()
# create an instance of CreateCustomerDto from a dict
create_customer_dto_from_dict = CreateCustomerDto.from_dict(create_customer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


