python -c "import os; doc = '''# DOCUMENTAÇÃO DE ADMINISTRAÇÃO E GOVERNANÇA DO POSTGRESQL

**Projeto:** Escudo Digital  
**SGBD:** PostgreSQL  
**Banco de Dados:** `db_escudo_digital`  
**Autor:** Jeferson Leite da Silva  

---

## 1. POLÍTICA DE ACESSO E USUÁRIOS (ROLES)

| Usuário / Role | Tipo de Acesso | Finalidade / Aplicação | Nível de Privilégio |
| :--- | :--- | :--- | :--- |
| `postgres` | Administrador (Superuser) | Gestão do SGBD, criação de tabelas, ETL e manutenção. | Acesso Total (ALL PRIVILEGES) |
| `usr_powerbi` | Leitura (Read-Only) | Conexão segura para o Power BI e relatórios analíticos. | `CONNECT`, `USAGE`, `SELECT` na View |

---

## 2. SCRIPTS DE CONFIGURAÇÃO DE SEGURANÇA (DCL)

```sql
-- Criação de usuário exclusivo de BI
CREATE USER usr_powerbi WITH PASSWORD 'PowerBI_Seguro2026!';

-- Concessão de permissões restritas
GRANT CONNECT ON DATABASE db_escudo_digital TO usr_powerbi;
GRANT USAGE ON SCHEMA public TO usr_powerbi;
GRANT SELECT ON vw_fato_completa TO usr_powerbi;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO usr_powerbi;