# RevokeSeatDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID of the addon (Whop Product ID or local ID). | 
**quantity** | **int** | The number of seats to revoke/deduct. | 

## Example

```python
from solifyn.models.revoke_seat_dto import RevokeSeatDto

# TODO update the JSON string below
json = "{}"
# create an instance of RevokeSeatDto from a JSON string
revoke_seat_dto_instance = RevokeSeatDto.from_json(json)
# print the JSON string representation of the object
print(RevokeSeatDto.to_json())

# convert the object into a dict
revoke_seat_dto_dict = revoke_seat_dto_instance.to_dict()
# create an instance of RevokeSeatDto from a dict
revoke_seat_dto_from_dict = RevokeSeatDto.from_dict(revoke_seat_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


