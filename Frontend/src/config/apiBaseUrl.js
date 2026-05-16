// Variables soportadas para backend en frontend:
// - VITE_API_URLBackend (preferida)
// - VITE_BACKEND_URL
// - VITE_API_BASE_URL
const envBaseUrl = String(
  import.meta.env.VITE_API_URLBackend ||
    import.meta.env.VITE_BACKEND_URL ||
    import.meta.env.VITE_API_BASE_URL ||
    (import.meta.env.DEV ? import.meta.env.VITE_API_URL || "" : "")
).trim();

if (import.meta.env.PROD && !envBaseUrl) {
  throw new Error(
    "Define VITE_API_URLBackend (o VITE_BACKEND_URL / VITE_API_BASE_URL) en producción."
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
