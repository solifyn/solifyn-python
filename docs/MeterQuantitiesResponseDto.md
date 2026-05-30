# MeterQuantitiesResponseDto

Represents aggregated usage quantities and calculated product costs for a meter within a selected date range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meter_id** | **str** | The unique meter ID. | 
**name** | **str** | Meter display name. | 
**total_usage** | **float** | Total usage within the selected time range. | 
**costs** | [**List[MeterQuantitiesCostDto]**](MeterQuantitiesCostDto.md) | Cost breakdown for products attached to the meter. | 

## Example

```python
from solifyn.models.meter_quantities_response_dto import MeterQuantitiesResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterQuantitiesResponseDto from a JSON string
meter_quantities_response_dto_instance = MeterQuantitiesResponseDto.from_json(json)
# print the JSON string representation of the object
print(MeterQuantitiesResponseDto.to_json())

# convert the object into a dict
meter_quantities_response_dto_dict = meter_quantities_response_dto_instance.to_dict()
# create an instance of MeterQuantitiesResponseDto from a dict
meter_quantities_response_dto_from_dict = MeterQuantitiesResponseDto.from_dict(meter_quantities_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


