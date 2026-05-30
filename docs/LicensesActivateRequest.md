# LicensesActivateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The license key. | 
**device_identifier** | **str** | Unique identifier of the device/machine being activated. | 
**name** | **str** | A user-friendly label/name for the instance. | 

## Example

```python
from solifyn.models.licenses_activate_request import LicensesActivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesActivateRequest from a JSON string
licenses_activate_request_instance = LicensesActivateRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesActivateRequest.to_json())

# convert the object into a dict
licenses_activate_request_dict = licenses_activate_request_instance.to_dict()
# create an instance of LicensesActivateRequest from a dict
licenses_activate_request_from_dict = LicensesActivateRequest.from_dict(licenses_activate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


