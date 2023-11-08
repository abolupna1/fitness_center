# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 


def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters=filters)

	
	records=frappe.db.get_list("Customer Records")
	for rec in records:
		d={"customer":rec["name"]}
		data.append(d)
	#	d={"Customer Records":rec["name"]}
	#	total_visists = frappe.db.count('Customer Visits', {'name': rec.name})

		

	
	return columns, data



def get_columns(filters=None):
	columns=[
		{"fieldname":"customer","label":_("Customer"),"fieldtype":"link","options":"Customer Records"},
		{"fieldname":"total_lvisits","label":_("Total Visits"),"fieldtype":"int"},
	]
	return columns