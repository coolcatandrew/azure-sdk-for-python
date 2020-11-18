# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class BillingFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The billing frequency.
    """

    MONTH = "Month"
    QUARTER = "Quarter"
    YEAR = "Year"

class Bound(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The boundary of the percentage, values could be 'Upper' or 'Lower'
    """

    UPPER = "Upper"
    LOWER = "Lower"

class BudgetOperatorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The operator to use for comparison.
    """

    IN_ENUM = "In"

class CategoryType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The category of the budget, whether the budget tracks cost or usage.
    """

    COST = "Cost"

class ChargeSummaryKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the kind of charge summary.
    """

    LEGACY = "legacy"
    MODERN = "modern"

class ChargeType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the charge. Could be actual or forecast
    """

    ACTUAL = "Actual"
    FORECAST = "Forecast"

class Datagrain(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DAILY_GRAIN = "daily"  #: Daily grain of data.
    MONTHLY_GRAIN = "monthly"  #: Monthly grain of data.

class EventType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of event.
    """

    SETTLED_CHARGES = "SettledCharges"
    PENDING_CHARGES = "PendingCharges"
    PENDING_ADJUSTMENTS = "PendingAdjustments"
    PENDING_NEW_CREDIT = "PendingNewCredit"
    PENDING_EXPIRED_CREDIT = "PendingExpiredCredit"
    UN_KNOWN = "UnKnown"
    NEW_CREDIT = "NewCredit"

class Grain(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The granularity of forecast.
    """

    DAILY = "Daily"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"

class LookBackPeriod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    LAST07_DAYS = "Last7Days"  #: Use 7 days of data for recommendations.
    LAST30_DAYS = "Last30Days"  #: Use 30 days of data for recommendations.
    LAST60_DAYS = "Last60Days"  #: Use 60 days of data for recommendations.

class LotSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Lot source.
    """

    PURCHASED_CREDIT = "PurchasedCredit"
    PROMOTIONAL_CREDIT = "PromotionalCredit"

class Metrictype(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTUAL_COST_METRIC_TYPE = "actualcost"  #: Actual cost data.
    AMORTIZED_COST_METRIC_TYPE = "amortizedcost"  #: Amortized cost data.
    USAGE_METRIC_TYPE = "usage"  #: Usage data.

class OperatorType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The comparison operator.
    """

    EQUAL_TO = "EqualTo"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"

class ReservationRecommendationKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the kind of reservation recommendation.
    """

    LEGACY = "legacy"
    MODERN = "modern"

class Scope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SINGLE = "Single"
    SHARED = "Shared"

class Term(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    P1_Y = "P1Y"  #: 1 year reservation term.
    P3_Y = "P3Y"  #: 3 year reservation term.

class ThresholdType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of threshold
    """

    ACTUAL = "Actual"

class TimeGrainType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The time covered by a budget. Tracking of the amount will be reset based on the time grain.
    BillingMonth, BillingQuarter, and BillingAnnual are only supported by WD customers
    """

    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    ANNUALLY = "Annually"
    BILLING_MONTH = "BillingMonth"
    BILLING_QUARTER = "BillingQuarter"
    BILLING_ANNUAL = "BillingAnnual"

class UsageDetailsKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the kind of usage details.
    """

    LEGACY = "legacy"
    MODERN = "modern"