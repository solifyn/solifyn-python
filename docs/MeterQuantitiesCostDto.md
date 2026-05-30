# MeterQuantitiesCostDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID attached to the meter. | 
**total_usage** | **float** | Total usage in the requested date range. | 
**billable_usage** | **float** | Billable usage after free threshold is applied. | 
**cost** | **float** | Calculated cost for this product. | 
**currency** | **str** | Currency used for the cost calculation. | 

## Example

```python
from solifyn.models.meter_quantities_cost_dto import MeterQuantitiesCostDto

# TODO update the JSON string below
json = "{}"
# create an instance of MeterQuantitiesCostDto from a JSON string
meter_quantities_cost_dto_instance = MeterQuantitiesCostDto.from_json(json)
# print the JSON string representation of the object
print(MeterQuantitiesCostDto.to_json())

# convert the object into a dict
meter_quantities_cost_dto_dict = meter_quantities_cost_dto_instance.to_dict()
# create an instance of MeterQuantitiesCostDto from a dict
meter_quantities_cost_dto_from_dict = MeterQuantitiesCostDto.from_dict(meter_quantities_cost_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


