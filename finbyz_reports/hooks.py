# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "finbyz_reports"
app_title = "finbyz"
app_publisher = "saurabh"
app_description = "finyz_reports"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@mntechnique.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/finbyz_reports/css/finbyz_reports.css"
# app_include_js = "/assets/finbyz_reports/js/finbyz_reports.js"

# include js, css files in header of web template
# web_include_css = "/assets/finbyz_reports/css/finbyz_reports.css"
# web_include_js = "/assets/finbyz_reports/js/finbyz_reports.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "finbyz_reports.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "finbyz_reports.install.before_install"
# after_install = "finbyz_reports.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "finbyz_reports.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"finbyz_reports.tasks.all"
# 	],
# 	"daily": [
# 		"finbyz_reports.tasks.daily"
# 	],
# 	"hourly": [
# 		"finbyz_reports.tasks.hourly"
# 	],
# 	"weekly": [
# 		"finbyz_reports.tasks.weekly"
# 	]
# 	"monthly": [
# 		"finbyz_reports.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "finbyz_reports.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "finbyz_reports.event.get_events"
# }

