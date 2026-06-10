# CustomerListResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CustomerResponseDto]**](CustomerResponseDto.md) | List of customers | 
**total_count** | **float** | Total count of customers matching the filters | 

## Example

```python
from solifyn.models.customer_list_response_dto import CustomerListResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerListResponseDto from a JSON string
customer_list_response_dto_instance = CustomerListResponseDto.from_json(json)
# print the JSON string representation of the object
print(CustomerListResponseDto.to_json())

# convert the object into a dict
customer_list_response_dto_dict = customer_list_response_dto_instance.to_dict()
# create an instance of CustomerListResponseDto from a dict
customer_list_response_dto_from_dict = CustomerListResponseDto.from_dict(customer_list_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


