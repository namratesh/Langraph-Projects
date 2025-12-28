# This simulates a database like Redis or Postgres
class InMemoryProfileStore:
    def __init__(self):
        # Key: user_id, Value: Dict of facts
        self.store = {}

    def save_fact(self, user_id: str, fact: str):
        if user_id not in self.store:
            self.store[user_id] = []
        self.store[user_id].append(fact)
        print(f"💾 DATABASE: Saved fact for {user_id} -> '{fact}'")

    def get_facts(self, user_id: str):
        return self.store.get(user_id, [])

# Global instance (Singleton)
profile_db = InMemoryProfileStore()