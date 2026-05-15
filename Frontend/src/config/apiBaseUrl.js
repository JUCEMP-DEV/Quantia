const envBaseUrl = String(
  import.meta.env.VITE_API_URLBackend || import.meta.env.VITE_API_BASE_URL || ""
).trim();

export const API_BASE_URL = envBaseUrl ? envBaseUrl.replace(/\/+$/, "") : "/api";
