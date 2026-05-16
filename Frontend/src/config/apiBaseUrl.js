const envBaseUrl = String(import.meta.env.VITE_BACKEND_URL || "")
  .trim()
  .replace(/\/+$/, "");

if (import.meta.env.PROD && !envBaseUrl) {
  throw new Error("Define VITE_BACKEND_URL en produccion.");
}

export const API_BASE_URL = envBaseUrl;
