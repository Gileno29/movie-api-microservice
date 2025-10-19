import psycopg2
from psycopg2 import Error

# A classe é um Gerenciador de Contexto
class Connection:

    def __init__(self, dbname, user, password, host, port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cursor = None

    # Método __enter__ é chamado ao entrar no bloco 'with'
    def __enter__(self):
        try:
            # Tenta estabelecer a conexão
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            # Cria um cursor (objeto para executar comandos SQL)
            self.cursor = self.conn.cursor()
            return self

        except Error as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            raise # Re-lança a exceção para que o bloco 'with' saiba que falhou

    # Método __exit__ é chamado ao sair do bloco 'with' (mesmo em caso de erro)
    def __exit__(self, exc_type, exc_value, traceback):
        # 1. Commita ou Rollback
        if self.conn:
            if exc_type is None:
                # Se não houve exceção no bloco 'with', commita as alterações
                self.conn.commit()
            else:
                # Se houve exceção, desfaz as alterações
                self.conn.rollback()
        
        # 2. Fecha o cursor e a conexão
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            # print("Conexão com PostgreSQL fechada.")
            
    # Método auxiliar para executar consultas
    def execute(self, query, params=None, fetch_one=False):
        """Executa uma consulta SQL e retorna os resultados, se houver."""
        if not self.cursor:
            raise Exception("Cursor não está ativo. A conexão pode ter falhado.")

        self.cursor.execute(query, params)
        
        # Verifica se a consulta tem resultado para buscar (SELECT)
        if self.cursor.description:
            if fetch_one:
                return self.cursor.fetchone()
            return self.cursor.fetchall()
        
        return None