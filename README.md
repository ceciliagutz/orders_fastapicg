Orders FastAPI - Cecilia Gutierrez
---
## Objetivo
---
Construir un servicio de Orders con dominio, casos de uso, puertos y adaptadores
- Exponer API FastAPI segura y documentada
- Asegurar calidad con pruebas, lint y tipado
- Facilitar delivery con Docker y preparación para CI/CD
- Documentar claramente la arquitectura y endpoints

⚠️ Las migraciones Alembic se omiten en esta entrega, pero la arquitectura y funcionalidad del servicio están completas.
## Estructura del proyecto
---
```plaintext
orders_fastapicg/
├── app/
│   ├── main.py           # Punto de entrada FastAPI
│   ├── domain/           # Entidades y lógica de negocio
│   ├── usecases/         # Casos de uso
│   ├── ports/            # Interfaces de entrada/salida
│   └── adapters/         # Implementaciones concretas (repos, API clients)
├── tests/                # Pruebas unitarias e integración
├── requirements.txt      # Dependencias
├── Dockerfile
└── README.md

```
---
## Entregables
---
- Código con capas (dominio, aplicación, infraestructura) y API
- Pruebas unitarias, de contrato, integración/E2E
- Migraciones Alembic omitidas en esta entrega
- Dockerfile multistage y pipeline CI/CD
- README y diagramas
- Evidencia de auditoría de dependencias

## Instalación
```bash
# Clonar repositorio
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Levantar app con Docker
docker build -t mi-fastapi .
docker run -p 8000:8000 mi-fastapi
```
---
# Uso
---
-Acceder a la API en [http://localhost:8000](http://localhost:8000)
-Documentación automática en [http://localhost:8000/docs](http://localhost:8000/docs)

# Notas importantes
- Este proyecto está diseñado siguiendo arquitectura hexagonal/limpia
- Las migraciones Alembic no se incluyen en esta entrega
- Listo para integración en CI/CD y contenedores Docker

