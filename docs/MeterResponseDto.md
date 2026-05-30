# MeterResponseDto

Represents a usage meter configured for event-based billing, including the tracked event name, aggregation strategy, optional filters, and archive status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique meter ID. | 
**business_id** | **str** | The business ID that owns this meter. | 
**name** | **str** | Meter display name. | 
**description** | **object** | Meter description. | [optional] 
**event_name** | **str** | The event name tracked by this meter. | 
**aggregation_type** | **str** | Aggregation strategy for usage events. | 
**aggregation_key** | **object** | Metadata key used for aggregation. | [optional] 
**unit** | **object** | Measurement unit label. | [optional] 
**filters** | **Dict[str, object]** | Optional filter definition for advanced matching. | [optional] 
**archived** | **bool** | Whether the meter is archived. | 
**created_at** | **datetime** | Creation timestamp. | 
**updated_at** | **datetime** | Last update timestamp. | 

## Example

```python
from solifyn.models.meter_response_dto import MeterResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterResponseDto from a JSON string
meter_response_dto_instance = MeterResponseDto.from_json(json)
# print the JSON string representation of the object
print(MeterResponseDto.to_json())

# convert the object into a dict
meter_response_dto_dict = meter_response_dto_instance.to_dict()
# create an instance of MeterResponseDto from a dict
meter_response_dto_from_dict = MeterResponseDto.from_dict(meter_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


