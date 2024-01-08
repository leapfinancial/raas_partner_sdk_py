# OperationDetailResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**from_user** | [**OperationUserDetail**](OperationUserDetail.md) |  | 
**show_warning_screen** | **bool** |  | 
**recipient_amout** | **float** |  | 
**code** | **str** |  | 
**status** | **str** |  | 
**amount** | **float** |  | 
**created_at** | **datetime** |  | 
**type** | **str** |  | 
**correlation_id** | **str** |  | 
**id** | **str** |  | 
**tenantfee** | **float** |  | [optional] 
**ignored_data** | [**IgnoredOperationData**](IgnoredOperationData.md) |  | [optional] 
**is_ignored** | **bool** |  | [optional] 
**attribution_link** | **str** |  | [optional] 
**has_reference_code** | **bool** |  | [optional] 
**exchange_rate** | **float** |  | [optional] 
**destination_fee** | **float** |  | [optional] 
**transaction_fee** | **float** |  | [optional] 
**source_fee** | **float** |  | [optional] 
**destination_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**source_payment_method** | [**PaymentMethodResponse**](PaymentMethodResponse.md) |  | [optional] 
**recipient_currency** | **str** |  | [optional] 
**sender_currency** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**sender_amount** | **float** |  | [optional] 
**reason** | **str** |  | [optional] 
**mobile_status** | **str** |  | [optional] 
**status_details** | **str** |  | [optional] 
**plat_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


