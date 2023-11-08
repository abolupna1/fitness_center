# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt

import frappe
from frappe import _ 


def execute(filters=None):
	columns, data = [], []
	columns=get_columns(filters=filters)

	
	records=frappe.db.get_list("Customer Records")
	for rec in records:
		record = frappe.get_doc("Customer Records",rec['name'])
		d={"naming_series":rec['name']}
		d["name"]=record.customer_name
		d["mobile"]=record.customer_mobile
		d["free_total_visits"]=frappe.db.count('Customer Visits', filters={"customer_record_number":rec["name"],"status":"Free"})
		d["paid_total_visits"]=frappe.db.count('Customer Visits', filters={"customer_record_number":rec["name"],"status":"Paid"})
		d["subscriptions_total_visits"]=frappe.db.count('Customer Visits', filters={"customer_record_number":rec["name"],"status":"Subscription"})
		d["total_visits"]=frappe.db.count('Customer Visits', filters={"customer_record_number":rec["name"]})
		d["total_subscriptions"]=frappe.db.count('Customer Subscriptions', filters={"customer_record_number":rec["name"]})
	     
		data.append(d)

		print(frappe.db.count('Customer Visits', filters={"customer_record_number":rec["name"]}))
	#	d={"Customer Records":rec["name"]}
	#	total_visists = 

		

	
	return columns, data



def get_columns(filters=None):
	columns=[
		{"fieldname":"naming_series","label":_("Record Number"),"fieldtype":"link","options":"Customer Records"},
		{"fieldname":"name","label":_("Name"),"fieldtype":"Data"},
		{"fieldname":"mobile","label":_("Mobile"),"fieldtype":"Data"},
		{"fieldname":"free_total_visits","label":_("Free Visits"),"fieldtype":"int"},
		{"fieldname":"paid_total_visits","label":_("Paid Visits"),"fieldtype":"int"},
		{"fieldname":"subscriptions_total_visits","label":_("Subscriptions Visits"),"fieldtype":"int"},
		{"fieldname":"total_visits","label":_("Total Visits"),"fieldtype":"int"},
		{"fieldname":"total_subscriptions","label":_("Total Subscriptions"),"fieldtype":"int"},
	]
	return columns