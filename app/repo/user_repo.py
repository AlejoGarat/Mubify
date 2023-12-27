class UserRepository:
    def __init__(self, conn):
        self.conn = conn 

    def get_user_count(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM users")
            count = cur.fetchone()[0]
            return count

    def get_first_10_user_names(self):
        with self.conn.cursor() as cur:
            cur.execute("SELECT username FROM users LIMIT 10")
            names = [row[0] for row in cur.fetchall()]
            return names