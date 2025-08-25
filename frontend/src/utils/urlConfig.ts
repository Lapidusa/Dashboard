export const listUrl = import.meta.env.PROD
  ? {
    apiUrl: import.meta.env.VITE_API_URL,
    baseUrl: import.meta.env.VITE_BASE_URL
  }
  : {
    apiUrl: import.meta.env.VITE_API_URL,
    baseUrl: import.meta.env.VITE_BASE_URL
  };
