# LicensesDeactivateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The license key. | 

## Example

```python
from solifyn.models.licenses_deactivate_request import LicensesDeactivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesDeactivateRequest from a JSON string
licenses_deactivate_request_instance = LicensesDeactivateRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesDeactivateRequest.to_json())

# convert the object into a dict
licenses_deactivate_request_dict = licenses_deactivate_request_instance.to_dict()
# create an instance of LicensesDeactivateRequest from a dict
licenses_deactivate_request_from_dict = LicensesDeactivateRequest.from_dict(licenses_deactivate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


