# UpdateCustomerDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The customer friendly full name | [optional] 
**phone** | **str** | The customer telephone/phone number | [optional] 
**username** | **str** | The username of the customer (e.g. Discord, Whop) | [optional] 
**metadata** | **object** | Custom key-value metadata associated with the customer | [optional] 

## Example

```python
from solifyn.models.update_customer_dto import UpdateCustomerDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerDto from a JSON string
update_customer_dto_instance = UpdateCustomerDto.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerDto.to_json())

# convert the object into a dict
update_customer_dto_dict = update_customer_dto_instance.to_dict()
# create an instance of UpdateCustomerDto from a dict
update_customer_dto_from_dict = UpdateCustomerDto.from_dict(update_customer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


