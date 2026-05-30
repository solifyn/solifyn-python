# SupportedCurrenciesResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label display name of the currency | 
**value** | **str** | The currency code | 

## Example

```python
from solifyn.models.supported_currencies_response_dto import SupportedCurrenciesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedCurrenciesResponseDto from a JSON string
supported_currencies_response_dto_instance = SupportedCurrenciesResponseDto.from_json(json)
# print the JSON string representation of the object
print(SupportedCurrenciesResponseDto.to_json())

# convert the object into a dict
supported_currencies_response_dto_dict = supported_currencies_response_dto_instance.to_dict()
# create an instance of SupportedCurrenciesResponseDto from a dict
supported_currencies_response_dto_from_dict = SupportedCurrenciesResponseDto.from_dict(supported_currencies_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


