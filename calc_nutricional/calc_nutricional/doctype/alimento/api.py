import frappe
import json


@frappe.whitelist(method='POST')
def valida_alimento():
    print("Validando alimento...")

    data = json.loads(frappe.request.data)
    print(data)

    return { 
        "status_code": 200,
        "message" : "Alimento validado com sucesso"
    }