# SendMoneyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | RaaS Operation Id | 
**link** | **str** | kochava link | 

## Example

```python
from openapi_client.models.send_money_response import SendMoneyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SendMoneyResponse from a JSON string
send_money_response_instance = SendMoneyResponse.from_json(json)
# print the JSON string representation of the object
print SendMoneyResponse.to_json()

# convert the object into a dict
send_money_response_dict = send_money_response_instance.to_dict()
# create an instance of SendMoneyResponse from a dict
send_money_response_form_dict = send_money_response.from_dict(send_money_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


