# LicenseValidationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**valid** | **bool** |  | 
**license** | [**LicenseSubDto**](LicenseSubDto.md) |  | 

## Example

```python
from solifyn.models.license_validation_response import LicenseValidationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseValidationResponse from a JSON string
license_validation_response_instance = LicenseValidationResponse.from_json(json)
# print the JSON string representation of the object
print(LicenseValidationResponse.to_json())

# convert the object into a dict
license_validation_response_dict = license_validation_response_instance.to_dict()
# create an instance of LicenseValidationResponse from a dict
license_validation_response_from_dict = LicenseValidationResponse.from_dict(license_validation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


