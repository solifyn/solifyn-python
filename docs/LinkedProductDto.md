# LinkedProductDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique product ID | 
**name** | **str** | The product name | 

## Example

```python
from solifyn.models.linked_product_dto import LinkedProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedProductDto from a JSON string
linked_product_dto_instance = LinkedProductDto.from_json(json)
# print the JSON string representation of the object
print(LinkedProductDto.to_json())

# convert the object into a dict
linked_product_dto_dict = linked_product_dto_instance.to_dict()
# create an instance of LinkedProductDto from a dict
linked_product_dto_from_dict = LinkedProductDto.from_dict(linked_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


