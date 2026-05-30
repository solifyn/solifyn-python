# BusinessCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title/name of the business | 

## Example

```python
from solifyn.models.business_create import BusinessCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessCreate from a JSON string
business_create_instance = BusinessCreate.from_json(json)
# print the JSON string representation of the object
print(BusinessCreate.to_json())

# convert the object into a dict
business_create_dict = business_create_instance.to_dict()
# create an instance of BusinessCreate from a dict
business_create_from_dict = BusinessCreate.from_dict(business_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


