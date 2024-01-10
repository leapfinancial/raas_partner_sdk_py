# PlaidURLResponsePayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**status** | **str** |  | 
**status_message** | **object** |  | [optional] 
**redirect_uri** | **str** |  | 

## Example

```python
from openapi_client.models.plaid_url_response_payload import PlaidURLResponsePayload

# TODO update the JSON string below
json = "{}"
# create an instance of PlaidURLResponsePayload from a JSON string
plaid_url_response_payload_instance = PlaidURLResponsePayload.from_json(json)
# print the JSON string representation of the object
print PlaidURLResponsePayload.to_json()

# convert the object into a dict
plaid_url_response_payload_dict = plaid_url_response_payload_instance.to_dict()
# create an instance of PlaidURLResponsePayload from a dict
plaid_url_response_payload_form_dict = plaid_url_response_payload.from_dict(plaid_url_response_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


