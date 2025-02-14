# Copyright (c) 2025, Augusto Lorencatto and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Cardapio(Document):

	@frappe.whitelist()
	def dispara_integracao(self) -> None:
		print("Disparando integração...")

		frappe.msgprint(
			msg='Teste realizado com sucesso',
			title='Notificação',
			# raise_exception=FileNotFoundError
		)

		return {
			"chave":"Valor 1"
		}
