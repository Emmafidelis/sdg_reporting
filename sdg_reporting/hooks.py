app_name = "sdg_reporting"
app_title = "Sdg Reporting"
app_publisher = "Emanuel Fidelis"
app_description = "sdg reporting app"
app_email = "emanuelkagombora28@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sdg_reporting",
# 		"logo": "/assets/sdg_reporting/logo.png",
# 		"title": "Sdg Reporting",
# 		"route": "/sdg_reporting",
# 		"has_permission": "sdg_reporting.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sdg_reporting/css/sdg_reporting.css"
# app_include_js = "/assets/sdg_reporting/js/sdg_reporting.js"

# include js, css files in header of web template
# web_include_css = "/assets/sdg_reporting/css/sdg_reporting.css"
# web_include_js = "/assets/sdg_reporting/js/sdg_reporting.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sdg_reporting/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sdg_reporting/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sdg_reporting.utils.jinja_methods",
# 	"filters": "sdg_reporting.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sdg_reporting.install.before_install"
# after_install = "sdg_reporting.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sdg_reporting.uninstall.before_uninstall"
# after_uninstall = "sdg_reporting.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sdg_reporting.utils.before_app_install"
# after_app_install = "sdg_reporting.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sdg_reporting.utils.before_app_uninstall"
# after_app_uninstall = "sdg_reporting.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sdg_reporting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sdg_reporting.tasks.all"
# 	],
# 	"daily": [
# 		"sdg_reporting.tasks.daily"
# 	],
# 	"hourly": [
# 		"sdg_reporting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sdg_reporting.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sdg_reporting.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "sdg_reporting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sdg_reporting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sdg_reporting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sdg_reporting.utils.before_request"]
# after_request = ["sdg_reporting.utils.after_request"]

# Job Events
# ----------
# before_job = ["sdg_reporting.utils.before_job"]
# after_job = ["sdg_reporting.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sdg_reporting.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

