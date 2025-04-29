import json
from pathlib import Path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # sube desde services/ hasta app/
PREFS_PATH = BASE_DIR / "database/user_prefs.json"

class UserPrefService:
    @staticmethod
    def _load_all():
        if not PREFS_PATH.exists():
            return {}
        try:
            with open(PREFS_PATH, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    @staticmethod
    def _save_all(all_prefs):
        print('subiendo archivo')
        with open(PREFS_PATH, "w") as f:
            json.dump(all_prefs, f, indent=2)

    @classmethod
    def add_pref(cls, id_email: str, node_id: str, weight: float = 1.0):
        print('miremos: ',id_email)
        print('miremos x2: ',node_id)
        all_prefs = cls._load_all()
        print('add pref',all_prefs)
        user_p = all_prefs.get(id_email, {})
        user_p[node_id] = user_p.get(node_id, 0) + weight
        # Normaliza para que sumen 1 (opcional pero recomendado)
        total = sum(user_p.values())
        for k in user_p:
            user_p[k] /= total
        all_prefs[id_email] = user_p
        cls._save_all(all_prefs)

    @classmethod
    def get_prefs(cls, id_email: str) -> dict:
        result = cls._load_all().get(id_email, {})
        return result
    