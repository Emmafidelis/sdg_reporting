# Copyright (c) 2025, Emanuel Fidelis and contributors
# For license information, please see license.txt

import re

import frappe
from frappe import _
from frappe.query_builder import DocType, Order
from frappe.utils import flt


def execute(filters=None):
    """Execute SDG Progress Tracking Report"""
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart_data(data)
    return columns, data, None, chart


def get_columns():
    """Return report columns"""
    return [
        {
            "label": _("Metric"),
            "fieldname": "metric",
            "fieldtype": "Data",
            "width": 400,
        },
        {"label": _("Q1 Value"), "fieldname": "q1", "fieldtype": "Float", "width": 100},
        {"label": _("Q2 Value"), "fieldname": "q2", "fieldtype": "Float", "width": 100},
        {"label": _("Trend"), "fieldname": "trend", "fieldtype": "Data", "width": 100},
        {
            "label": _("Percent"),
            "fieldname": "change_percent",
            "fieldtype": "Percent",
            "width": 100,
        },
    ]


def get_data(filters):
    """Get report data using Query Builder"""

    SustainabilityMetric = DocType("Sustainability Metric")

    query = (
        frappe.qb.from_(SustainabilityMetric)
        .select(
            SustainabilityMetric.metric_name.as_("metric"),
            SustainabilityMetric.q1,
            SustainabilityMetric.q2,
        )
        .where(SustainabilityMetric.docstatus != 2)
        .where(
            (SustainabilityMetric.q1.isnotnull())
            | (SustainabilityMetric.q2.isnotnull())
        )
        .orderby(SustainabilityMetric.metric_name, order=Order.asc)
    )

    records = query.run(as_dict=True)
    return [build_row(record) for record in records]


def get_chart_data(data):
    """Prepare chart dataset for dashboard usage"""

    if not data:
        return None

    labels, q1_values, q2_values = [], [], []

    for row in data:
        if row.get("q1") is None and row.get("q2") is None:
            continue
        labels.append(row["metric"])
        q1_values.append(flt(row.get("q1") or 0))
        q2_values.append(flt(row.get("q2") or 0))

    if not labels:
        return None

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {"name": _("Q1"), "values": q1_values},
                {"name": _("Q2"), "values": q2_values},
            ],
        },
        "type": "line",
        "colors": ["#2563eb", "#fb923c"],
    }


def build_row(record):
    """Normalize raw row into report-friendly dict"""

    q1_value = parse_numeric(record.get("q1"))
    q2_value = parse_numeric(record.get("q2"))

    trend, change_percent = analyse_progress(q1_value, q2_value)

    return {
        "metric": record.get("metric"),
        "q1": q1_value,
        "q2": q2_value,
        "trend": trend,
        "change_percent": change_percent,
    }


def parse_numeric(value):
    """Extract numeric value from free-form strings"""

    if value is None:
        return None

    if isinstance(value, (int, float)):
        return flt(value)

    if isinstance(value, str):
        cleaned = value.strip().replace(",", "")
        match = re.search(r"-?\d+(?:\.\d+)?", cleaned)
        if match:
            return flt(match.group())

    return None


def analyse_progress(q1_value, q2_value):
    """Derive trend and percentage change for numeric inputs"""

    if q1_value is None and q2_value is None:
        return "no data", None

    if q1_value is None or q2_value is None:
        return "insufficient data", None

    if q2_value > q1_value:
        trend = "increase"
    elif q2_value < q1_value:
        trend = "decrease"
    else:
        trend = "stable"

    change_percent = None
    if q1_value:
        change_percent = flt(((q2_value - q1_value) / q1_value) * 100, 2)

    return trend, change_percent
