# LicenseSubDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**status** | **str** |  | 
**activation_limit** | **float** |  | 
**activation_message** | **str** |  | 
**expires_at** | **str** |  | 
**product** | [**ProductSubDto**](ProductSubDto.md) |  | [optional] 

## Example

```python
from solifyn.models.license_sub_dto import LicenseSubDto

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseSubDto from a JSON string
license_sub_dto_instance = LicenseSubDto.from_json(json)
# print the JSON string representation of the object
print(LicenseSubDto.to_json())

# convert the object into a dict
license_sub_dto_dict = license_sub_dto_instance.to_dict()
# create an instance of LicenseSubDto from a dict
license_sub_dto_from_dict = LicenseSubDto.from_dict(license_sub_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


