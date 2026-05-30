# LicensesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**activation_limit** | **int** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from solifyn.models.licenses_update_request import LicensesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesUpdateRequest from a JSON string
licenses_update_request_instance = LicensesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesUpdateRequest.to_json())

# convert the object into a dict
licenses_update_request_dict = licenses_update_request_instance.to_dict()
# create an instance of LicensesUpdateRequest from a dict
licenses_update_request_from_dict = LicensesUpdateRequest.from_dict(licenses_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


