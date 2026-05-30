# PricePreviewResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_price** | **float** | Original price of the product after discounts | 
**original_currency** | **str** | Original ISO currency code of the product | 
**converted_price** | **float** | Converted price of the product | 
**converted_currency** | **str** | Converted ISO currency code of the product | 

## Example

```python
from solifyn.models.price_preview_response_dto import PricePreviewResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of PricePreviewResponseDto from a JSON string
price_preview_response_dto_instance = PricePreviewResponseDto.from_json(json)
# print the JSON string representation of the object
print(PricePreviewResponseDto.to_json())

# convert the object into a dict
price_preview_response_dto_dict = price_preview_response_dto_instance.to_dict()
# create an instance of PricePreviewResponseDto from a dict
price_preview_response_dto_from_dict = PricePreviewResponseDto.from_dict(price_preview_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


