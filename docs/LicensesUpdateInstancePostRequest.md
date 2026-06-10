# LicensesUpdateInstancePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_name** | **str** | A new human-readable display name for this instance. | [optional] 
**ip_address** | **str** | A new IP address to record for this instance. | [optional] 

## Example

```python
from solifyn.models.licenses_update_instance_post_request import LicensesUpdateInstancePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesUpdateInstancePostRequest from a JSON string
licenses_update_instance_post_request_instance = LicensesUpdateInstancePostRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesUpdateInstancePostRequest.to_json())

# convert the object into a dict
licenses_update_instance_post_request_dict = licenses_update_instance_post_request_instance.to_dict()
# create an instance of LicensesUpdateInstancePostRequest from a dict
licenses_update_instance_post_request_from_dict = LicensesUpdateInstancePostRequest.from_dict(licenses_update_instance_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


