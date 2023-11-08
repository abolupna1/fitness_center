# Copyright (c) 2023, edom ibrahim and contributors
# For license information, please see license.txt
from frappe.utils import add_to_date

import frappe
from frappe.model.document import Document

class CustomerSubscriptions(Document):
    def before_insert(self):
        self.appointments = []
        d = self.start
        for i in range(int(self.month_cont)):
            scd = self.append("appointments",{
                'scheduled_date': d,
                'scheduled_time':self.scheduled_time,
                'scheduled_day' : self.scheduled_day
            })
            d =add_to_date(d, days=7)
        self.end=d
    def on_update(self):
        self.appointments = []
        d = self.start
        for i in range(int(self.month_cont)):
            scd = self.append("appointments",{
                'scheduled_date': d,
                'scheduled_time':self.scheduled_time,
                'scheduled_day' : self.scheduled_day
			})
            d =add_to_date(d, days=7)
        self.end=d

        
   
     
              

        
        
        


      

	
