# Quantia Backend

## Variables de entorno (requeridas)

Para que el backend pueda resolver catálogos y simulaciones, se requiere:

```env
SUPABASE_URL=...
SUPABASE_SERVICE_ROLE_KEY=...
```

Alternativas aceptadas por código (menos recomendadas para admin):

- `SUPABASE_KEY`
- `SUPABASE_ANON_KEY`

Prioridad interna de clave admin:

1. `SUPABASE_SERVICE_ROLE_KEY`
2. `SUPABASE_KEY`
3. `SUPABASE_ANON_KEY`

## Prefijo de API

El backend monta rutas con prefijo:

`/api`

Por ejemplo:

- `POST /api/auth/login`
- `POST /api/motor/preliminares/simular`
- `POST /api/motor/modulos/{module_key}/simular`
- `POST /api/resultados/inferir`

## Endpoints de verificación

- `GET /health`
- `GET /docs`
- `GET /openapi.json`

Si `openapi.json` muestra rutas pero simulación responde `422` con mensaje de Supabase, el problema es de variables de entorno y no de routing.
