# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, validator
from raassdkpy.models.cip import CIP
from raassdkpy.models.i_phone_info import IPhoneInfo

class User(BaseModel):
    """
    User
    """
    id: StrictStr = Field(...)
    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(None, alias="firstName")
    last_name: Optional[StrictStr] = Field(None, alias="lastName")
    middle_name: Optional[StrictStr] = Field(None, alias="middleName")
    second_last_name: Optional[StrictStr] = Field(None, alias="secondLastName")
    address1: Optional[StrictStr] = None
    address2: Optional[StrictStr] = None
    place_id: Optional[StrictStr] = Field(None, alias="placeId")
    country: Optional[StrictStr] = None
    address_description: Optional[StrictStr] = Field(None, alias="addressDescription", description="Here we save some description about direcction for example: Local 304, next to the grocery store")
    gender: Optional[StrictStr] = None
    dob: Optional[datetime] = None
    country_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    phone_number: Optional[StrictStr] = Field(None, alias="phoneNumber")
    phone_verified: Optional[StrictBool] = Field(None, alias="phoneVerified")
    cip: Optional[CIP] = None
    first_time: Optional[StrictBool] = Field(None, alias="firstTime")
    country_code: Optional[StrictStr] = Field(None, alias="countryCode")
    city: Optional[StrictStr] = None
    zipcode: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    birth_state: Optional[StrictStr] = Field(None, alias="birthState")
    place_detail: Optional[StrictStr] = Field(None, alias="placeDetail", description="Here we save the google maps places address details")
    pincode: Optional[StrictStr] = Field(None, description="Pincode - used to validate user in Raas")
    has_pincode: Optional[StrictBool] = Field(None, alias="hasPincode")
    password: Optional[StrictStr] = Field(None, description="Used to store Numi Plat pincode. It's not used to validate  user in Raas")
    phone_info: Optional[IPhoneInfo] = Field(None, alias="phoneInfo")
    tenant_id: StrictStr = Field(..., alias="tenantId")
    tenant_code: StrictStr = Field(..., alias="tenantCode")
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    profile_picture_url: Optional[StrictStr] = Field(None, alias="profilePictureUrl")
    custom_country_code: Optional[StrictStr] = Field(None, alias="customCountryCode")
    facebook_public_user_name: Optional[StrictStr] = Field(None, alias="facebookPublicUserName")
    instagram_public_user_name: Optional[StrictStr] = Field(None, alias="instagramPublicUserName")
    account_code: Optional[StrictStr] = Field(None, alias="accountCode")
    __properties = ["id", "email", "firstName", "lastName", "middleName", "secondLastName", "address1", "address2", "placeId", "country", "addressDescription", "gender", "dob", "country_id", "status", "phoneNumber", "phoneVerified", "cip", "firstTime", "countryCode", "city", "zipcode", "state", "birthState", "placeDetail", "pincode", "hasPincode", "password", "phoneInfo", "tenantId", "tenantCode", "latitude", "longitude", "profilePictureUrl", "customCountryCode", "facebookPublicUserName", "instagramPublicUserName", "accountCode"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('new', 'ready'):
            raise ValueError("must be one of enum values ('new', 'ready')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cip
        if self.cip:
            _dict['cip'] = self.cip.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phone_info
        if self.phone_info:
            _dict['phoneInfo'] = self.phone_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "middle_name": obj.get("middleName"),
            "second_last_name": obj.get("secondLastName"),
            "address1": obj.get("address1"),
            "address2": obj.get("address2"),
            "place_id": obj.get("placeId"),
            "country": obj.get("country"),
            "address_description": obj.get("addressDescription"),
            "gender": obj.get("gender"),
            "dob": obj.get("dob"),
            "country_id": obj.get("country_id"),
            "status": obj.get("status"),
            "phone_number": obj.get("phoneNumber"),
            "phone_verified": obj.get("phoneVerified"),
            "cip": CIP.from_dict(obj.get("cip")) if obj.get("cip") is not None else None,
            "first_time": obj.get("firstTime"),
            "country_code": obj.get("countryCode"),
            "city": obj.get("city"),
            "zipcode": obj.get("zipcode"),
            "state": obj.get("state"),
            "birth_state": obj.get("birthState"),
            "place_detail": obj.get("placeDetail"),
            "pincode": obj.get("pincode"),
            "has_pincode": obj.get("hasPincode"),
            "password": obj.get("password"),
            "phone_info": IPhoneInfo.from_dict(obj.get("phoneInfo")) if obj.get("phoneInfo") is not None else None,
            "tenant_id": obj.get("tenantId"),
            "tenant_code": obj.get("tenantCode"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "profile_picture_url": obj.get("profilePictureUrl"),
            "custom_country_code": obj.get("customCountryCode"),
            "facebook_public_user_name": obj.get("facebookPublicUserName"),
            "instagram_public_user_name": obj.get("instagramPublicUserName"),
            "account_code": obj.get("accountCode")
        })
        return _obj


