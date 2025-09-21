# Copyright (c) 2025, Emanuel Fidelis and contributors
# For license information, please see license.txt

from collections import Counter
import frappe
from frappe import _
from frappe.query_builder import DocType, Order
from frappe.query_builder.functions import Concat
from frappe.query_builder.custom import ConstantColumn


def execute(filters=None):
    """Execute SDG Metrics Mapping Report"""
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
            "fieldtype": "Link",
            "options": "Sustainability Metric",
            "width": 300,
        },
        {
            "label": _("SDG Goals"),
            "fieldname": "sdg_link",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("SDG Target"),
            "fieldname": "sdg_target",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("ESG Pillar"),
            "fieldname": "esg_pillar",
            "fieldtype": "Data",
            "width": 120,
        },
        {
            "label": _("GRI Mapping"),
            "fieldname": "gri_mapping",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": _("Metric Count"),
            "fieldname": "metric_count",
            "fieldtype": "Int",
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
            (Concat("SDG ", SustainabilityMetric.sdg_link)).as_("sdg_link"),
            SustainabilityMetric.sdg_target.as_("sdg_target"),
            SustainabilityMetric.esg_pillar.as_("esg_pillar"),
            SustainabilityMetric.gri_disclosure.as_("gri_mapping"),
            ConstantColumn(1).as_("metric_count"),
        )
        .where(SustainabilityMetric.docstatus != 2)
        .orderby(SustainabilityMetric.metric_name, order=Order.asc)
    )

    return query.run(as_dict=True)


def get_chart_data(data):
    """Build chart data showing coverage by ESG pillar"""

    if not data:
        return None

    pillar_counts = Counter(
        (row.get("esg_pillar") or _("Unspecified")).strip() for row in data
    )

    labels = list(pillar_counts.keys())
    values = [pillar_counts[label] for label in labels]

    return {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": _("Metric Count"),
                    "values": values,
                }
            ],
        },
        "type": "bar",
        "colors": ["#2563eb", "#10b981", "#f97316", "#7c3aed", "#dc2626"],
    }
