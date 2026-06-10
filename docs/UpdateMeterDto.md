# UpdateMeterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Meter display name. | [optional] 
**description** | **str** | Meter description. | [optional] 
**event_name** | **str** | The event name tracked by this meter. | [optional] 
**aggregation_type** | **str** | Aggregation strategy for usage events. | [optional] 
**aggregation_key** | **str** | Metadata key used by SUM, MAX, or LAST aggregation modes. | [optional] 
**unit** | **str** | Measurement unit label. | [optional] 
**filters** | **Dict[str, object]** | Optional filter definition for advanced matching. | [optional] 
**enable_filtering** | **bool** | Enable filtering on usage event ingestion. | [optional] 

## Example

```python
from solifyn.models.update_meter_dto import UpdateMeterDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMeterDto from a JSON string
update_meter_dto_instance = UpdateMeterDto.from_json(json)
# print the JSON string representation of the object
print(UpdateMeterDto.to_json())

# convert the object into a dict
update_meter_dto_dict = update_meter_dto_instance.to_dict()
# create an instance of UpdateMeterDto from a dict
update_meter_dto_from_dict = UpdateMeterDto.from_dict(update_meter_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


