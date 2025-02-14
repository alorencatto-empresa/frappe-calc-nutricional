# Copyright (c) 2025, Augusto Lorencatto and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Refeicao(Document):
	pass
	
	# def before_insert(self):

	# 	table = frappe.qb.DocType(self.doctype)

	# 	q = (
	# 		frappe.qb.from_(table)
	# 		.select(table.name)
	# 		.where(table.nome == self.nome)
	# 		.where(table.prioridade == self.prioridade)
	# 	).run(as_dict=1)

	# 	# print(q[0])
  
	# 	if len(q) > 0:
	# 		frappe.throw(title="Erro de validação",msg=f"Refeição já inserida : ID : {q[0]['name']}!")
