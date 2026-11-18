# Copyright (c) 2025-2026 Lacey Rae Castleberry. Dual-Licensed (AGPLv3 / Commercial). See COMMERCIAL_LICENSE.md
import os
import getpass
import stripe

api_key = os.environ.get("STRIPE_SECRET_KEY", "").strip()
if not api_key or "your_actual_key" in api_key:
    print("\n🔒 Paste your sk_live_... key below and press Enter (input is hidden):")
    api_key = getpass.getpass("Stripe Secret Key: ").strip()

if not api_key.startswith("sk_"):
    print("[ERROR] Invalid key format. Key must start with sk_live_ or rk_live_")
    exit(1)

stripe.api_key = api_key
redirect_url = "https://lovelaceyrae11.github.io/lovelaceyrae.github.io/?session_id={CHECKOUT_SESSION_ID}"

links = stripe.PaymentLink.list(limit=20)
matched = 0
for pl in links.auto_paging_iter():
    if pl.url in [
        "https://buy.stripe.com/00w4gz1Pu3aFdcQbyIgA801",
        "https://buy.stripe.com/aFadR9cu84eJ1u8eKUgA802"
    ]:
        updated = stripe.PaymentLink.modify(
            pl.id,
            after_completion={
                "type": "redirect",
                "redirect": {"url": redirect_url}
            }
        )
        matched += 1
        print(f"✅ Wired Auto-Unlock Redirect for: {updated.url}")
        print(f"   -> Redirects to: {redirect_url}\n")

if matched == 0:
    print("[INFO] Could not find matching links in list, verify account mode.")
