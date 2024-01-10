# openapi_client.DefaultApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bank_account**](DefaultApi.md#add_bank_account) | **POST** /user/funding/source/bank/add/{userToken} | 
[**add_card**](DefaultApi.md#add_card) | **POST** /user/funding/source/card/add/{userToken} | 
[**create_contact**](DefaultApi.md#create_contact) | **POST** /user/contacts/{userToken} | 
[**create_pin**](DefaultApi.md#create_pin) | **POST** /user/pin | 
[**delete_payment_method**](DefaultApi.md#delete_payment_method) | **POST** /user/funding/source/delete/{userToken} | 
[**get_available_operation_type**](DefaultApi.md#get_available_operation_type) | **GET** /user/corridors/available-operations/{userToken} | 
[**get_available_payment_methods**](DefaultApi.md#get_available_payment_methods) | **GET** /user/corridors/available-methods/{userToken} | 
[**get_cash_operators**](DefaultApi.md#get_cash_operators) | **POST** /user/funding/cash/operators/{userToken} | 
[**get_cip_info**](DefaultApi.md#get_cip_info) | **GET** /cip/process/{phoneNumber} | 
[**get_corridors**](DefaultApi.md#get_corridors) | **GET** /user/corridors | 
[**get_destination_sof_for_requet_money_operation**](DefaultApi.md#get_destination_sof_for_requet_money_operation) | **GET** /user/funding/source/request-money/{userToken} | 
[**get_exchange_rates**](DefaultApi.md#get_exchange_rates) | **GET** /user/exchange-rates/exchange-rates | 
[**get_in_and_out_operations**](DefaultApi.md#get_in_and_out_operations) | **GET** /user/operations/in-out/{userToken} | 
[**get_operation**](DefaultApi.md#get_operation) | **GET** /user/operations/detail/{id} | 
[**get_operation_quote**](DefaultApi.md#get_operation_quote) | **POST** /user/operations/quotation/{userToken} | 
[**get_payment_method**](DefaultApi.md#get_payment_method) | **GET** /user/funding/source/get-payment-method/{userToken} | 
[**get_payment_method_v2**](DefaultApi.md#get_payment_method_v2) | **GET** /user/funding/source/get-payment-method-v2/{userToken} | 
[**get_profile**](DefaultApi.md#get_profile) | **GET** /user/profile/{phone} | 
[**get_redis_status**](DefaultApi.md#get_redis_status) | **GET** /system/status/redis | 
[**get_session_link**](DefaultApi.md#get_session_link) | **POST** /auth/sessionlink | 
[**get_sof_for_send_money_operation**](DefaultApi.md#get_sof_for_send_money_operation) | **GET** /user/funding/source/send-money/{userToken} | 
[**get_user_token**](DefaultApi.md#get_user_token) | **POST** /auth/get-user-token | 
[**get_while_label_link**](DefaultApi.md#get_while_label_link) | **POST** /auth/white-label-link | 
[**is_phone_available**](DefaultApi.md#is_phone_available) | **POST** /auth/is-phone-available | 
[**list_contacts**](DefaultApi.md#list_contacts) | **GET** /user/contacts/{userToken} | 
[**perform_level_one**](DefaultApi.md#perform_level_one) | **POST** /cip/level/one/{phoneNumber} | 
[**perform_resubmit_upgrade_level**](DefaultApi.md#perform_resubmit_upgrade_level) | **POST** /cip/level/resubmit-upgrade | 
[**pre_quote**](DefaultApi.md#pre_quote) | **POST** /user/operations/pre-quote/{userToken} | 
[**receive**](DefaultApi.md#receive) | **POST** /user/operations/receive-money/{userToken} | 
[**register_user**](DefaultApi.md#register_user) | **POST** /auth/register-user | 
[**register_user_v2**](DefaultApi.md#register_user_v2) | **POST** /auth/register-user-v2 | 
[**request_otp**](DefaultApi.md#request_otp) | **POST** /auth/request-otp | 
[**request_v2**](DefaultApi.md#request_v2) | **POST** /user/operations/request-money-v2/{userToken} | 
[**send**](DefaultApi.md#send) | **POST** /user/operations/send-money/{userToken} | 
[**set_alternate_cip**](DefaultApi.md#set_alternate_cip) | **POST** /cip/alternate | 
[**set_level_two**](DefaultApi.md#set_level_two) | **POST** /cip/level/two/{phoneNumber} | 
[**set_reference_code**](DefaultApi.md#set_reference_code) | **POST** /user/funding/cash/reference-code/{userToken} | 
[**set_trusted_level_two**](DefaultApi.md#set_trusted_level_two) | **POST** /cip/level/two/{phoneNumber}/trusted | 
[**status**](DefaultApi.md#status) | **GET** /user/operations/status/{userToken}/{operationId} | 
[**update_profile**](DefaultApi.md#update_profile) | **PUT** /user/profile/{phone} | 
[**updated_contact**](DefaultApi.md#updated_contact) | **PUT** /user/contacts/{userToken} | 
[**validate_otp**](DefaultApi.md#validate_otp) | **POST** /auth/validate-otp | 
[**validate_phone_number**](DefaultApi.md#validate_phone_number) | **POST** /auth/validate-phone | 
[**validate_pin_code**](DefaultApi.md#validate_pin_code) | **POST** /user/validate-pincode | 


# **add_bank_account**
> add_bank_account(user_token, add_bank_account_params_base)



adds bank account to subscriber's source of funding

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from openapi_client.model.add_bank_account_params_base import AddBankAccountParamsBase
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    add_bank_account_params_base = AddBankAccountParamsBase(
        name="name_example",
        account_number="account_number_example",
        bank_account_type="CheckingAccount",
        bank_entity_number="bank_entity_number_example",
        is_primary=True,
        country="country_example",
        currency="currency_example",
    ) # AddBankAccountParamsBase | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.add_bank_account(user_token, add_bank_account_params_base)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_bank_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **add_bank_account_params_base** | [**AddBankAccountParamsBase**](AddBankAccountParamsBase.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_card**
> AddPaymentMethodResponse add_card(user_token, add_card_partner_params)



adds a card to subscriber's source of funding

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.add_payment_method_response import AddPaymentMethodResponse
from openapi_client.model.add_card_partner_params import AddCardPartnerParams
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    add_card_partner_params = AddCardPartnerParams(
        name="name_example",
        cardtype="DebitCard",
        number="number_example",
        is_primary=True,
        name_on_card="name_on_card_example",
        expiration_date="expiration_date_example",
        security_code="security_code_example",
        currency="currency_example",
        country="country_example",
        card_network="NotApplicable",
    ) # AddCardPartnerParams | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_card(user_token, add_card_partner_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **add_card_partner_params** | [**AddCardPartnerParams**](AddCardPartnerParams.md)|  |

### Return type

[**AddPaymentMethodResponse**](AddPaymentMethodResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> create_contact(user_token, create_contact_request_params_partner)



Create a contact for a user

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.create_contact_request_params_partner import CreateContactRequestParamsPartner
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.validate_error import ValidateError
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    create_contact_request_params_partner = CreateContactRequestParamsPartner(
        alias="alias_example",
        country_code=CountryAlpha2Code("AF"),
        phone="phone_example",
        last_name="last_name_example",
        first_name="first_name_example",
        email="email_example",
    ) # CreateContactRequestParamsPartner | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_contact(user_token, create_contact_request_params_partner)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. |
 **create_contact_request_params_partner** | [**CreateContactRequestParamsPartner**](CreateContactRequestParamsPartner.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pin**
> create_pin(set_pincode_params_partner)



Creates a pincode for the user.  The pincode must be 6 digits long and only numeric characters are allowed.  If the user already has a pincode, an error will be returned.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.set_pincode_params_partner import SetPincodeParamsPartner
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    set_pincode_params_partner = SetPincodeParamsPartner(None) # SetPincodeParamsPartner | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_pin(set_pincode_params_partner)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_pin: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_pincode_params_partner** | [**SetPincodeParamsPartner**](SetPincodeParamsPartner.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method**
> delete_payment_method(user_token, payment_method_id)



removes a payment method

### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    payment_method_id = "paymentMethodId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_payment_method(user_token, payment_method_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **payment_method_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_operation_type**
> [str] get_available_operation_type(user_token)



Gets available operation types by user country (as source country) and destination country. A corridor is a way to configure available operation between two subscribers.  NOTICE: if an operation is RequestFunds from A to B, you may search for a SendFunds from B to A to determine if operation is available. Probabily you'll not find a RequestFunds option as such.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    destination_country = "destinationCountry_example" # str | ISO 3166 2-alpha (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_available_operation_type(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_available_operation_type: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_available_operation_type(user_token, destination_country=destination_country)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_available_operation_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **destination_country** | **str**| ISO 3166 2-alpha | [optional]

### Return type

**[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_payment_methods**
> [str] get_available_payment_methods(user_token)



Gets available payment method types by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    destination_country = "destinationCountry_example" # str | ISO 3166 2-alpha (optional)
    operation_type = "SendFunds" # str | SendFunds | RequestFunds (optional) if omitted the server will use the default value of "SendFunds"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_available_payment_methods(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_available_payment_methods: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_available_payment_methods(user_token, destination_country=destination_country, operation_type=operation_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_available_payment_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **destination_country** | **str**| ISO 3166 2-alpha | [optional]
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] if omitted the server will use the default value of "SendFunds"

### Return type

**[str]**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | string[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_operators**
> [CashOperators] get_cash_operators(user_token, cash_operators_params_base)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.cash_operators_params_base import CashOperatorsParamsBase
from openapi_client.model.cash_operators import CashOperators
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    cash_operators_params_base = CashOperatorsParamsBase(
        operation_ammount=3.14,
    ) # CashOperatorsParamsBase | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cash_operators(user_token, cash_operators_params_base)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_cash_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **cash_operators_params_base** | [**CashOperatorsParamsBase**](CashOperatorsParamsBase.md)|  |

### Return type

[**[CashOperators]**](CashOperators.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cip_info**
> PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC get_cip_info(phone_number)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.pick_cip_exclude_keyof_cipid_or_attemps_or_is_valid_ofac import PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone_number = "phoneNumber_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_cip_info(phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_cip_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  |

### Return type

[**PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC**](PickCIPExcludeKeyofCIPIdOrAttempsOrIsValidOFAC.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_corridors**
> [CorridorDTO] get_corridors()



Gets corridors by source country, destination country and operation type. A corridor is a way to configure available operation between two subscribers.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.corridor_dto import CorridorDTO
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    source_country = "sourceCountry_example" # str | ISO 3166 2-alpha (optional)
    destination_country = "destinationCountry_example" # str | ISO 3166 2-alpha (optional)
    operation_type = "SendFunds" # str | SendFunds | RequestFunds (optional) if omitted the server will use the default value of "SendFunds"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_corridors(source_country=source_country, destination_country=destination_country, operation_type=operation_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_corridors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_country** | **str**| ISO 3166 2-alpha | [optional]
 **destination_country** | **str**| ISO 3166 2-alpha | [optional]
 **operation_type** | **str**| SendFunds | RequestFunds | [optional] if omitted the server will use the default value of "SendFunds"

### Return type

[**[CorridorDTO]**](CorridorDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CorridorDTO[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination_sof_for_requet_money_operation**
> [SourceOfFunding] get_destination_sof_for_requet_money_operation(user_token)



gets destination sources of funding for request funds

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.source_of_funding import SourceOfFunding
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    source_country = "sourceCountry_example" # str |  (optional)
    destination_country = "destinationCountry_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_destination_sof_for_requet_money_operation(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_destination_sof_for_requet_money_operation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_destination_sof_for_requet_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_destination_sof_for_requet_money_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **source_country** | **str**|  | [optional]
 **destination_country** | **str**|  | [optional]

### Return type

[**[SourceOfFunding]**](SourceOfFunding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_rates**
> [ExchangeRateDTO] get_exchange_rates()



Gets exchange rates between currencies

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.exchange_rate_dto import ExchangeRateDTO
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    currency_code_src = "currencyCodeSrc_example" # str | ISO 4217 3-alpha (optional)
    currency_code_dest = "currencyCodeDest_example" # str | ISO 4217 3-alpha (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_exchange_rates(currency_code_src=currency_code_src, currency_code_dest=currency_code_dest)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_exchange_rates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_code_src** | **str**| ISO 4217 3-alpha | [optional]
 **currency_code_dest** | **str**| ISO 4217 3-alpha | [optional]

### Return type

[**[ExchangeRateDTO]**](ExchangeRateDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ExchangeRate[] |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_in_and_out_operations**
> [OperationDetailResponse] get_in_and_out_operations(user_token)



Return all the in and outs operations for an user given his userId

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.operation_detail_response import OperationDetailResponse
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    to_phone_number = "toPhoneNumber_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_in_and_out_operations(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_in_and_out_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_in_and_out_operations(user_token, to_phone_number=to_phone_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_in_and_out_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **to_phone_number** | **str**|  | [optional]

### Return type

[**[OperationDetailResponse]**](OperationDetailResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation**
> OperationDetail get_operation(id)



Gets operation detail by id

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.operation_detail import OperationDetail
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | Operation Id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_operation(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Operation Id |

### Return type

[**OperationDetail**](OperationDetail.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_quote**
> RaasQuoteTransactionResponse get_operation_quote(user_token, quote_transaction_base)



 Retrieve quote for the operation

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.raas_quote_transaction_response import RaasQuoteTransactionResponse
from openapi_client.model.quote_transaction_base import QuoteTransactionBase
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    quote_transaction_base = QuoteTransactionBase(
        sender_user_id="sender_user_id_example",
        sender_country_code="sender_country_code_example",
        recipient_user_id="recipient_user_id_example",
        recipient_country_code="recipient_country_code_example",
        recipient_currency="recipient_currency_example",
        recipient_amount=3.14,
        is_sender_amount=True,
        amount_currency="amount_currency_example",
        amount=3.14,
        operation_type=None,
        source_payment_method=None,
        destination_payment_method=None,
        tennant_fee=3.14,
    ) # QuoteTransactionBase | {@link QuoteTransactionBase}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_operation_quote(user_token, quote_transaction_base)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_operation_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **quote_transaction_base** | [**QuoteTransactionBase**](QuoteTransactionBase.md)| {@link QuoteTransactionBase} |

### Return type

[**RaasQuoteTransactionResponse**](RaasQuoteTransactionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | quotation data |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> RaaSPaymentMethod get_payment_method(user_token)



Retrieve a payment method by number

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.raa_s_payment_method import RaaSPaymentMethod
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    number = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_payment_method(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_payment_method: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_payment_method(user_token, number=number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_payment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **number** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**RaaSPaymentMethod**](RaaSPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method_v2**
> RaaSPartnerPaymentMethod get_payment_method_v2(user_token)



Retrieve a payment method by ID

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from openapi_client.model.raa_s_partner_payment_method import RaaSPartnerPaymentMethod
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    id = "" # str |  (optional) if omitted the server will use the default value of ""

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_payment_method_v2(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_payment_method_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_payment_method_v2(user_token, id=id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_payment_method_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **id** | **str**|  | [optional] if omitted the server will use the default value of ""

### Return type

[**RaaSPartnerPaymentMethod**](RaaSPartnerPaymentMethod.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link PaymentMethod} |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> User get_profile(phone)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.validate_error import ValidateError
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone = "phone_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_profile(phone)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  |

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redis_status**
> InlineResponse200 get_redis_status()



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_redis_status()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_redis_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session_link**
> SessionLinkResponse get_session_link(session_link_params)



Generates Partner API Link Token.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.session_link_response import SessionLinkResponse
from openapi_client.model.inline_response400 import InlineResponse400
from openapi_client.model.session_link_params import SessionLinkParams
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    session_link_params = SessionLinkParams(
        phone_number="phone_number_example",
        last_name="last_name_example",
        last_name2="last_name2_example",
        gender="Male",
        dob=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        first_name="first_name_example",
        middle_name="middle_name_example",
        address1="address1_example",
        address2="address2_example",
        country_code=CountryAlpha2Code("AF"),
        city="city_example",
        zip_code="zip_code_example",
        state="state_example",
        birth_state="birth_state_example",
        add_card_params=AddCardSessionParams(
            name="name_example",
            cardtype="DebitCard",
            number="number_example",
            name_on_card="name_on_card_example",
            expiration_date="expiration_date_example",
            security_code="security_code_example",
            currency="currency_example",
            country="country_example",
            card_network="NotApplicable",
        ),
    ) # SessionLinkParams | {@link SessionLinkParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_session_link(session_link_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_session_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_link_params** | [**SessionLinkParams**](SessionLinkParams.md)| {@link SessionLinkParams} |

### Return type

[**SessionLinkResponse**](SessionLinkResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sof_for_send_money_operation**
> [SourceOfFunding] get_sof_for_send_money_operation(user_token)



gets sources of funding for send funds

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.source_of_funding import SourceOfFunding
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    source_country = "sourceCountry_example" # str |  (optional)
    destination_country = "destinationCountry_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_sof_for_send_money_operation(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_sof_for_send_money_operation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_sof_for_send_money_operation(user_token, source_country=source_country, destination_country=destination_country)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_sof_for_send_money_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **source_country** | **str**|  | [optional]
 **destination_country** | **str**|  | [optional]

### Return type

[**[SourceOfFunding]**](SourceOfFunding.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token**
> UserTokenResponse get_user_token(get_user_token_params)



Partner API Token.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_user_token_params import GetUserTokenParams
from openapi_client.model.user_token_response import UserTokenResponse
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    get_user_token_params = GetUserTokenParams(
        phone_number="phone_number_example",
    ) # GetUserTokenParams | {@link GetUserTokenParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_token(get_user_token_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_user_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_user_token_params** | [**GetUserTokenParams**](GetUserTokenParams.md)| {@link GetUserTokenParams} |

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_while_label_link**
> SessionLinkResponse get_while_label_link()



Generates Partner API White Label Link Token.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.session_link_response import SessionLinkResponse
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_while_label_link()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_while_label_link: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionLinkResponse**](SessionLinkResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_phone_available**
> IsPhoneAvailableResponse is_phone_available(is_phone_available_request)



Verify is the phone number is available for registration.  It is used to check if the phone number is already registered. Returns true if the phone number is available.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.is_phone_available_request import IsPhoneAvailableRequest
from openapi_client.model.inline_response404 import InlineResponse404
from openapi_client.model.is_phone_available_response import IsPhoneAvailableResponse
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    is_phone_available_request = IsPhoneAvailableRequest(
        phone="phone_example",
    ) # IsPhoneAvailableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.is_phone_available(is_phone_available_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->is_phone_available: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_phone_available_request** | [**IsPhoneAvailableRequest**](IsPhoneAvailableRequest.md)|  |

### Return type

[**IsPhoneAvailableResponse**](IsPhoneAvailableResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contacts**
> [ContactInfo] list_contacts(user_token)



Retrieve all contacts for a user

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.contact_info import ContactInfo
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | User token, used to retrieve the user's contacts. A.k.a. userId.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_contacts(user_token)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. |

### Return type

[**[ContactInfo]**](ContactInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact List |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_level_one**
> perform_level_one(phone_number, perform_level_one_params)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.perform_level_one_params import PerformLevelOneParams
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone_number = "phoneNumber_example" # str | 
    perform_level_one_params = PerformLevelOneParams(
        address_description="address_description_example",
        country_code="country_code_example",
        call_location_longitude=3.14,
        call_location_latitude=3.14,
        city="city_example",
        birth_state="birth_state_example",
        state="state_example",
        zip_code="zip_code_example",
        gender="Male",
        place_detail="place_detail_example",
        address2="address2_example",
        address1="address1_example",
        date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        second_last_name="second_last_name_example",
        middle_name="middle_name_example",
        last_name="last_name_example",
        first_name="first_name_example",
    ) # PerformLevelOneParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.perform_level_one(phone_number, perform_level_one_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->perform_level_one: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  |
 **perform_level_one_params** | [**PerformLevelOneParams**](PerformLevelOneParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_resubmit_upgrade_level**
> perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.perform_resubmit_upgrade_level_params import PerformResubmitUpgradeLevelParams
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    perform_resubmit_upgrade_level_params = PerformResubmitUpgradeLevelParams(
        level=3.14,
        level_status_detail="level_status_detail_example",
        call_location_longitude=3.14,
        call_location_latitude=3.14,
        address1="address1_example",
        address2="address2_example",
        address3="address3_example",
        address4="address4_example",
        state="state_example",
        city="city_example",
        zip_code="zip_code_example",
        place_detail="place_detail_example",
        email="email_example",
        country_code="country_code_example",
        date_of_birth="date_of_birth_example",
        nationality="nationality_example",
        birth_state="birth_state_example",
        gender="gender_example",
        documents=[
            UserDocument(
                id="id_example",
                type={},
                sub_type=3.14,
                number="number_example",
                expiration_date="expiration_date_example",
                issued_country="issued_country_example",
                issued_date="issued_date_example",
                user_identity_data={
                    "key": None,
                },
                date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        first_name="first_name_example",
        last_name="last_name_example",
        last_name2="last_name2_example",
        is_id_address_different=True,
    ) # PerformResubmitUpgradeLevelParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.perform_resubmit_upgrade_level(perform_resubmit_upgrade_level_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->perform_resubmit_upgrade_level: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perform_resubmit_upgrade_level_params** | [**PerformResubmitUpgradeLevelParams**](PerformResubmitUpgradeLevelParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pre_quote**
> RaasPreQuoteResponse pre_quote(user_token, raas_pre_quote_request)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.raas_pre_quote_response import RaasPreQuoteResponse
from openapi_client.model.raas_pre_quote_request import RaasPreQuoteRequest
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    raas_pre_quote_request = RaasPreQuoteRequest(
        recipient_id="recipient_id_example",
        subscriber_id="subscriber_id_example",
        destination_payment_method=None,
        sender_country_code="sender_country_code_example",
        is_sender_amount=True,
        amount=3.14,
        operation_type="SendFunds",
        product_type="Fund",
        tennant_fee=3.14,
    ) # RaasPreQuoteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.pre_quote(user_token, raas_pre_quote_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->pre_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **raas_pre_quote_request** | [**RaasPreQuoteRequest**](RaasPreQuoteRequest.md)|  |

### Return type

[**RaasPreQuoteResponse**](RaasPreQuoteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive**
> receive(user_token, receive_money_params)



Receive funds

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.receive_money_params import ReceiveMoneyParams
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    receive_money_params = ReceiveMoneyParams(
        destination_payment_method=None,
        correlation_id="correlation_id_example",
    ) # ReceiveMoneyParams | {@link ReceiveMoneyParams}

    # example passing only required values which don't have defaults set
    try:
        api_instance.receive(user_token, receive_money_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->receive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **receive_money_params** | [**ReceiveMoneyParams**](ReceiveMoneyParams.md)| {@link ReceiveMoneyParams} |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user**
> UserTokenResponse register_user(register_user_params)



Registers Partner user. If user exists, return its id.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.register_user_params import RegisterUserParams
from openapi_client.model.user_token_response import UserTokenResponse
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    register_user_params = RegisterUserParams(
        phone_number="phone_number_example",
        last_name="last_name_example",
        last_name2="last_name2_example",
        gender="Male",
        dob=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        first_name="first_name_example",
        middle_name="middle_name_example",
        address1="address1_example",
        address2="address2_example",
        country_code=CountryAlpha2Code("AF"),
        city="city_example",
        zip_code="zip_code_example",
        state="state_example",
        birth_state="birth_state_example",
    ) # RegisterUserParams | {@link RegisterUserParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.register_user(register_user_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->register_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_params** | [**RegisterUserParams**](RegisterUserParams.md)| {@link RegisterUserParams} |

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_user_v2**
> UserTokenResponse register_user_v2(register_user_params)



Registers Partner user. If user exists, return its id.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.register_user_params import RegisterUserParams
from openapi_client.model.user_token_response import UserTokenResponse
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    register_user_params = RegisterUserParams(
        phone_number="phone_number_example",
        last_name="last_name_example",
        last_name2="last_name2_example",
        gender="Male",
        dob=dateutil_parser('1970-01-01T00:00:00.00Z'),
        email="email_example",
        first_name="first_name_example",
        middle_name="middle_name_example",
        address1="address1_example",
        address2="address2_example",
        country_code=CountryAlpha2Code("AF"),
        city="city_example",
        zip_code="zip_code_example",
        state="state_example",
        birth_state="birth_state_example",
    ) # RegisterUserParams | {@link RegisterUserParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.register_user_v2(register_user_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->register_user_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user_params** | [**RegisterUserParams**](RegisterUserParams.md)| {@link RegisterUserParams} |

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_otp**
> request_otp(request_otp_params)



Request OTP for phone number. The phone number must be registered. Using /register endpoint.

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.request_otp_params import RequestOTPParams
from openapi_client.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    request_otp_params = RequestOTPParams(
        lang=Language("en"),
        phone="phone_example",
    ) # RequestOTPParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.request_otp(request_otp_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->request_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_otp_params** | [**RequestOTPParams**](RequestOTPParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Code Sent |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_v2**
> PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen request_v2(user_token, request_money_partner_params)



Request money to a contact

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.request_money_partner_params import RequestMoneyPartnerParams
from openapi_client.model.pick_operation_detail_response_exclude_keyof_operation_detail_response_id_or_type_or_show_warning_screen import PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    request_money_partner_params = RequestMoneyPartnerParams(
        request_to="request_to_example",
        correlation_id="correlation_id_example",
        destination_payment_method_id="destination_payment_method_id_example",
        recipient_amount=3.14,
        recipient_currency="recipient_currency_example",
        reason="reason_example",
    ) # RequestMoneyPartnerParams | {@link RequestMoneyParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.request_v2(user_token, request_money_partner_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->request_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **request_money_partner_params** | [**RequestMoneyPartnerParams**](RequestMoneyPartnerParams.md)| {@link RequestMoneyParams} |

### Return type

[**PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen**](PickOperationDetailResponseExcludeKeyofOperationDetailResponseIdOrTypeOrShowWarningScreen.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {@link RequestMoneyResponse} |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> SendMoneyResponse send(user_token, send_money_params)



Send funds to a requester

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.send_money_response import SendMoneyResponse
from openapi_client.model.inline_response400 import InlineResponse400
from openapi_client.model.send_money_params import SendMoneyParams
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    send_money_params = SendMoneyParams(None) # SendMoneyParams | {@link SendMoneyParams}

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.send(user_token, send_money_params)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **send_money_params** | [**SendMoneyParams**](SendMoneyParams.md)| {@link SendMoneyParams} |

### Return type

[**SendMoneyResponse**](SendMoneyResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_alternate_cip**
> set_alternate_cip(type)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.alternate_flow import AlternateFlow
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    type = AlternateFlow("ssn") # AlternateFlow | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_alternate_cip(type)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->set_alternate_cip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **AlternateFlow**|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_level_two**
> set_level_two(phone_number, level_two_params)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.level_two_params import LevelTwoParams
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone_number = "phoneNumber_example" # str | 
    level_two_params = LevelTwoParams(
        ssn="ssn_example",
        call_location_longitude=3.14,
        call_location_latitude=3.14,
    ) # LevelTwoParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_level_two(phone_number, level_two_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->set_level_two: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  |
 **level_two_params** | [**LevelTwoParams**](LevelTwoParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_reference_code**
> GetReferenceCodeResponse set_reference_code(user_token, set_reference_code_params_base)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.set_reference_code_params_base import SetReferenceCodeParamsBase
from openapi_client.model.get_reference_code_response import GetReferenceCodeResponse
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    set_reference_code_params_base = SetReferenceCodeParamsBase(
        operation_id="operation_id_example",
        operation_code="operation_code_example",
        amount=3.14,
        currency="currency_example",
        sender_name="sender_name_example",
        receiver_name="receiver_name_example",
        network_id="network_id_example",
        operation_type="operation_type_example",
        cash_provider="cash_provider_example",
    ) # SetReferenceCodeParamsBase | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_reference_code(user_token, set_reference_code_params_base)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->set_reference_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **set_reference_code_params_base** | [**SetReferenceCodeParamsBase**](SetReferenceCodeParamsBase.md)|  |

### Return type

[**GetReferenceCodeResponse**](GetReferenceCodeResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_trusted_level_two**
> set_trusted_level_two(phone_number)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone_number = "phoneNumber_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.set_trusted_level_two(phone_number)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->set_trusted_level_two: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status**
> str status(user_token, operation_id)



Gets operation status

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | 
    operation_id = "operationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.status(user_token, operation_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**|  |
 **operation_id** | **str**|  |

### Return type

**str**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile**
> update_profile(phone, user_update_params)



Updates user profile

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user_update_params import UserUpdateParams
from openapi_client.model.validate_error import ValidateError
from openapi_client.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    phone = "phone_example" # str | 
    user_update_params = UserUpdateParams(
        email="email_example",
        first_name="first_name_example",
        last_name="last_name_example",
        middle_name="middle_name_example",
        second_last_name="second_last_name_example",
        address1="address1_example",
        address2="address2_example",
        place_id="place_id_example",
        country="country_example",
        gender="gender_example",
        dob=dateutil_parser('1970-01-01T00:00:00.00Z'),
        country_id="country_id_example",
        status="new",
        first_time=True,
    ) # UserUpdateParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_profile(phone, user_update_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  |
 **user_update_params** | [**UserUpdateParams**](UserUpdateParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**404** |  |  -  |
**422** | Validation Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updated_contact**
> updated_contact(user_token, update_contact_request_params)



Update a contact for a user

### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.validate_error import ValidateError
from openapi_client.model.update_contact_request_params import UpdateContactRequestParams
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    user_token = "userToken_example" # str | User token, used to retrieve the user's contacts. A.k.a. userId.
    update_contact_request_params = UpdateContactRequestParams(
        alias="alias_example",
        country_code="country_code_example",
        last_name="last_name_example",
        first_name="first_name_example",
        email="email_example",
        phone="phone_example",
    ) # UpdateContactRequestParams | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.updated_contact(user_token, update_contact_request_params)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->updated_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| User token, used to retrieve the user&#39;s contacts. A.k.a. userId. |
 **update_contact_request_params** | [**UpdateContactRequestParams**](UpdateContactRequestParams.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |
**422** | Validation Failed |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_otp**
> validate_otp(body)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.inline_response404 import InlineResponse404
from openapi_client.model.inline_response500 import InlineResponse500
from openapi_client.model.pick_validate_otp_params_exclude_keyof_validate_otp_params_device_id import PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    body = PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId(
        phone="phone_example",
        otp_code="otp_code_example",
    ) # PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.validate_otp(body)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->validate_otp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId**](PickValidateOTPParamsExcludeKeyofValidateOTPParamsDeviceId.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_phone_number**
> str validate_phone_number(inline_object)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    inline_object = InlineObject(
        phone="phone_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.validate_phone_number(inline_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->validate_phone_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**204** | No content |  -  |
**400** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_pin_code**
> validate_pin_code(body)



### Example

* Api Key Authentication (api_key):

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response403 import InlineResponse403
from openapi_client.model.pick_validate_pin_code_params_exclude_keyof_validate_pin_code_params_device_id import PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId
from openapi_client.model.inline_response500 import InlineResponse500
from openapi_client.model.validate_error import ValidateError
from pprint import pprint
# Defining the host is optional and defaults to /v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    body = PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId(
        phone="phone_example",
        pincode="pincode_example",
    ) # PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.validate_pin_code(body)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->validate_pin_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId**](PickValidatePINCodeParamsExcludeKeyofValidatePINCodeParamsDeviceId.md)|  |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid pincode |  -  |
**403** |  |  -  |
**404** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

