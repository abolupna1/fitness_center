from __future__ import unicode_literals
import frappe
from frappe import _

def get_loyalty_amount(doc, method=None):
    amunt=0.0

    get_invoices =  frappe.get_all("Sales Invoice", filters = [
			["posa_pos_opening_shift","=" ,doc.pos_opening_shift],
			["status","=","Paid"]
		], 
		fields = ["*"])
    print(len(get_invoices))
    for inv in get_invoices:
        amunt+=inv.loyalty_amount
    doc.loyalty_amount = amunt


