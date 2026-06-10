# CreateMeterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Meter display name. | 
**description** | **str** | Meter description. | [optional] 
**event_name** | **str** | The event name tracked by this meter. | 
**aggregation_type** | **str** | Aggregation strategy for usage events. | 
**aggregation_key** | **str** | Metadata key used by SUM, MAX, or LAST aggregation modes. | [optional] 
**unit** | **str** | Measurement unit label. | [optional] 
**filters** | **Dict[str, object]** | Optional filter definition for advanced matching. | [optional] 
**enable_filtering** | **bool** | Enable filtering on usage event ingestion. | [optional] [default to False]

## Example

```python
from solifyn.models.create_meter_dto import CreateMeterDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMeterDto from a JSON string
create_meter_dto_instance = CreateMeterDto.from_json(json)
# print the JSON string representation of the object
print(CreateMeterDto.to_json())

# convert the object into a dict
create_meter_dto_dict = create_meter_dto_instance.to_dict()
# create an instance of CreateMeterDto from a dict
create_meter_dto_from_dict = CreateMeterDto.from_dict(create_meter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


