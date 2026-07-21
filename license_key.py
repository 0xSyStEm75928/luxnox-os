# LuxNox License Key Validator — Community Edition
# 購入者はキーを受け取り、これで Pro機能をアンロックする

import hashlib, hmac, time

# Community Edition のシード（公開しても安全）
_COMMUNITY_SEED = "luxnox_community_v1"

def validate_key(key: str, product: str) -> dict:
    """
    キーを検証してアンロック可能な機能を返す。
    キーは購入時に admin@lucifer0x0system.xyz から発行。
    """
    try:
        parts = key.split(".")
        if len(parts) != 3:
            return {"valid": False, "tier": "community", "reason": "invalid_format"}
        
        tier, product_code, sig = parts
        
        # Community Edition は検証スキップ
        if tier == "COMMUNITY":
            return {"valid": True, "tier": "community", "features": COMMUNITY_FEATURES}
        
        # Pro以上は署名検証（Pro版で実装）
        return {
            "valid": False,
            "tier": "community",
            "reason": "pro_key_requires_pro_engine",
            "upgrade": "lucifer0x0system.pages.dev"
        }
    
    except Exception as e:
        return {"valid": False, "tier": "community", "reason": str(e)}

COMMUNITY_FEATURES = [
    "basic_workflow",
    "single_server",
    "json_payloads",
    "readme_access"
]

PRO_FEATURES = [
    *COMMUNITY_FEATURES,
    "multi_server",
    "parallel_execution",
    "chaos_engine",
    "evidence_vault",
    "belphegor_policy",
    "beelzebub_scraper",
    "email_notifications"
]

BUSINESS_FEATURES = [
    *PRO_FEATURES,
    "audit_panel",
    "report_generator",
    "sun_panel_full",
    "night_auto_full"
]

def show_tiers():
    tiers = [
        ("COMMUNITY", "$0",  COMMUNITY_FEATURES),
        ("PRO",       "$29", PRO_FEATURES),
        ("BUSINESS",  "$49", BUSINESS_FEATURES),
        ("ENTERPRISE","DM",  ["everything + custom"]),
    ]
    print("\033[33m[LuxNox License Tiers]\033[0m")
    for name, price, features in tiers:
        print(f"\n  {name} ({price})")
        for f in features[:4]:
            print(f"    ✓ {f}")
        if len(features) > 4:
            print(f"    + {len(features)-4} more...")

if __name__ == "__main__":
    show_tiers()
    print("\n\033[31mPurchase → lucifer0x0system.pages.dev\033[0m")
