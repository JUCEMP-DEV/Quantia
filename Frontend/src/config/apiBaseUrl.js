// Use VITE_BACKEND_URL en Vercel para apuntar al backend público.
// En producción no debe depender de un fallback a "/api".
const envBaseUrl = String(
  import.meta.env.VITE_BACKEND_URL ||
    (import.meta.env.DEV ? import.meta.env.VITE_API_URL || "" : "")
).trim();

if (import.meta.env.PROD && !envBaseUrl) {
  throw new Error(
    "VITE_BACKEND_URL no está definido en producción. El frontend necesita la URL del backend de Render."
  );
}

function normalizeApiBaseUrl(baseUrl) {
  const normalized = String(baseUrl || "").trim().replace(/\/+$, "");
  return normalized.includes("/api") ? normalized : `${normalized}/api`;
}

export const API_BASE_URL = envBaseUrl
  ? normalizeApiBaseUrl(envBaseUrl)
  : import.meta.env.DEV
  ? "/api"
  : "";
