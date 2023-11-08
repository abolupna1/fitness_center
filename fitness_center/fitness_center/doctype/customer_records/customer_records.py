# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class CustomerRecords(Document):
	def before_insert(self):
		check = frappe.db.exists('Customer',{"mobile_no": self.customer_mobile},cache=True)
		territory = frappe.db.exists('Territory',{"name": 'Saudi Arabia'},cache=True)
		if check:
			self.customer = check
		else:
			entry=frappe.new_doc("Customer")
			entry.customer_name = self.customer_name
			entry.customer_type = 'Individual'
			entry.customer_group = self.customer_group
			entry.territory = territory 
			entry.email_id = self.customer_email
			entry.insert()
			self.customer = entry.name
		

		
	def after_insert(self):
		vsit=frappe.new_doc("Customer Visits")
		vsit.status = 'Free'
		vsit.customer_record_number = self.name
		vsit.insert()

	def on_update(self):
		customer = frappe.get_doc('Customer',self.customer)
		
		if customer.mobile_no != self.customer_mobile:
			check = frappe.db.get_list('Customer',filters={"mobile_no":self.customer_mobile})
			if len(check)>0:
				frappe.throw("رقم الجوال مرتبط مع عميل سابق ")



			
		

