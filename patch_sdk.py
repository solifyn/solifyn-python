import os

filepath = r"F:\xampp\htdocs_payment\sdks\python\solifyn\api\default_api.py"

if os.path.exists(filepath):
    print("Patching default_api.py...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    replacements = {
        "webhook_dispute_payload:  = None": "webhook_dispute_payload: Optional[WebhookDisputePayload] = None",
        "webhook_entitlement_grant_payload:  = None": "webhook_entitlement_grant_payload: Optional[WebhookEntitlementGrantPayload] = None",
        "webhook_license_payload:  = None": "webhook_license_payload: Optional[WebhookLicensePayload] = None",
        "webhook_payment_payload:  = None": "webhook_payment_payload: Optional[WebhookPaymentPayload] = None",
        "order:  = None": "order: Optional[Order] = None",
        "webhook_refund_payload:  = None": "webhook_refund_payload: Optional[WebhookRefundPayload] = None",
        "webhook_subscription_payload:  = None": "webhook_subscription_payload: Optional[WebhookSubscriptionPayload] = None",
    }
    
    for target, replacement in replacements.items():
        content = content.replace(target, replacement)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("Done patching.")
else:
    print("File not found:", filepath)
