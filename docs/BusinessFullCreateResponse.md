# BusinessFullCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Indicates if creation was successful | 
**business_id** | **str** | The newly created business ID | 

## Example

```python
from solifyn.models.business_full_create_response import BusinessFullCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessFullCreateResponse from a JSON string
business_full_create_response_instance = BusinessFullCreateResponse.from_json(json)
# print the JSON string representation of the object
print(BusinessFullCreateResponse.to_json())

# convert the object into a dict
business_full_create_response_dict = business_full_create_response_instance.to_dict()
# create an instance of BusinessFullCreateResponse from a dict
business_full_create_response_from_dict = BusinessFullCreateResponse.from_dict(business_full_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


