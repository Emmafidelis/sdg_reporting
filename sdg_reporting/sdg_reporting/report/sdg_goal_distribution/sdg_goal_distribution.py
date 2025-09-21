# Copyright (c) 2025, Emanuel Fidelis and contributors
# For license information, please see license.txt

import re
import frappe
from frappe import _
from frappe.utils import flt
from frappe.query_builder import DocType, Order


def execute(filters=None):
    """Execute SDG Goal Distribution Report"""
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart_data(data)
    return columns, data, None, chart


def get_columns():
    """Return report columns"""
    return [
        {
            "label": _("SDG Target"),
            "fieldname": "sdg_target",
            "fieldtype": "Link",
            "options": "SDG Target",
            "width": 300,
        },
        {
            "label": _("Employee Impact"),
            "fieldname": "employee_impact",
            "fieldtype": "Int",
            "width": 150,
        },
        {
            "label": _("Percentage"),
            "fieldname": "percentage",
            "fieldtype": "Float",
            "width": 120,
        },
        {
            "label": _("SDG Goal"),
            "fieldname": "sdg_goal",
            "fieldtype": "Link",
            "options": "SDG Goal",
            "width": 100,
        },
    ]


def get_data(filters):
    """Get report data using Query Builder"""

    SustainabilityMetric = DocType("Sustainability Metric")
    SDGGoal = DocType("SDG Goal")
    SDGTarget = DocType("SDG Target")

    query = (
        frappe.qb.from_(SustainabilityMetric)
        .left_join(SDGGoal)
        .on(SDGGoal.name == SustainabilityMetric.sdg_link)
        .left_join(SDGTarget)
        .on(SDGTarget.name == SustainabilityMetric.sdg_target)
        .select(
            SustainabilityMetric.metric_name,
            SustainabilityMetric.sdg_link,
            SustainabilityMetric.sdg_target,
            SustainabilityMetric.q1,
            SustainabilityMetric.q2,
            SDGGoal.goal_name,
            SDGTarget.target_no,
            SDGTarget.description.as_("target_description"),
        )
        .where(SustainabilityMetric.docstatus != 2)
        .orderby(SustainabilityMetric.sdg_link, order=Order.asc)
        .orderby(SustainabilityMetric.sdg_target, order=Order.asc)
        .orderby(SustainabilityMetric.metric_name, order=Order.asc)
    )

    metrics = query.run(as_dict=True)

    grouped = {}

    for metric in metrics:
        goal_no = metric.get("sdg_link")
        target_no = metric.get("sdg_target")
        key = (goal_no, target_no)

        impact = get_metric_impact(metric)

        if key not in grouped:
            grouped[key] = {
                "sdg_target": build_target_label(metric),
                "employee_impact": 0,
                "sdg_goal": goal_no,
                "metric_count": 0,
            }

        grouped[key]["employee_impact"] += impact
        grouped[key]["metric_count"] += 1

    distribution = list(grouped.values())

    for item in distribution:
        # fallback to metric count when no impact
        if not item.get("employee_impact") and item.get("metric_count"):
            item["employee_impact"] = item["metric_count"]

    total_value = sum(item.get("employee_impact", 0) for item in distribution)

    for item in distribution:
        if total_value > 0:
            item["percentage"] = flt(
                (item.get("employee_impact", 0) / total_value) * 100, 2
            )
        else:
            item["percentage"] = 0

    return distribution


def get_chart_data(data):
    """Generate chart data for the report"""
    if not data:
        return None

    return {
        "data": {
            "labels": [item["sdg_target"] for item in data],
            "datasets": [
                {
                    "name": _("Total Value"),
                    "values": [item.get("employee_impact", 0) for item in data],
                }
            ],
        },
        "type": "pie",
        "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4"],
    }


def get_metric_impact(metric):
    """Derive a numerical impact using the metric's values"""
    q1_value = parse_numeric(metric.get("q1"))
    q2_value = parse_numeric(metric.get("q2"))

    impact = 0
    if q1_value is not None:
        impact += q1_value
    if q2_value is not None:
        impact += q2_value

    return impact


def build_target_label(metric):
    """Construct a friendly label for the target/goal pair"""
    goal_name = metric.get("goal_name") or metric.get("sdg_link") or _("Unknown Goal")
    target_no = metric.get("sdg_target") or metric.get("target_no")
    target_label = target_no or _("Unassigned Target")

    description = metric.get("target_description")
    if description:
        return _("{target} - {goal}").format(target=target_label, goal=description)

    return _("{target} - {goal}").format(target=target_label, goal=goal_name)


def parse_numeric(value):
    """Extract numeric values from mixed data strings"""
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
