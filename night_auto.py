# LuxNox Night Jobs — Community Edition
# Full implementation: Lucifuge_Rofocale (private)

NIGHT_JOBS = [
    {"id": "N01", "title": "Batch Runner",     "schedule": "02:00"},
    {"id": "N02", "title": "Evidence Builder", "schedule": "03:00"},
    {"id": "N03", "title": "Archive",          "schedule": "04:00"},
    {"id": "N04", "title": "Backup",           "schedule": "05:00"},
    {"id": "N05", "title": "Revenue Tasks",    "schedule": "06:00"},
]

def run_night():
    print('\033[32m--- [ LuxNox Night Jobs — Community Edition ] ---\033[0m')
    for job in NIGHT_JOBS:
        print(f"  [{job['id']}] {job['title']:20s} @ {job['schedule']}")
    print('\033[33m  Pro版でフル実装 → lucifer0x0system.pages.dev\033[0m')

if __name__ == "__main__":
    run_night()
